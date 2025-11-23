import React from 'react'
import { render, screen } from '@testing-library/react'
import PortfolioOverview from '@/components/PortfolioOverview'
import { TradingData } from '@/types/trading'

describe('PortfolioOverview Component', () => {
  const mockData: TradingData = {
    totalValue: 125000,
    dailyPnL: 2400,
    totalPnL: 15600,
    activePositions: 8,
    riskLevel: 'Low'
  }

  it('should render total portfolio value', () => {
    render(<PortfolioOverview data={mockData} />)
    
    expect(screen.getByText(/125,000/)).toBeInTheDocument()
  })

  it('should display daily PnL', () => {
    render(<PortfolioOverview data={mockData} />)
    
    expect(screen.getByText(/2,400/)).toBeInTheDocument()
  })

  it('should display total PnL', () => {
    render(<PortfolioOverview data={mockData} />)
    
    expect(screen.getByText(/15,600/)).toBeInTheDocument()
  })

  it('should show number of active positions', () => {
    render(<PortfolioOverview data={mockData} />)
    
    expect(screen.getByText('8')).toBeInTheDocument()
  })

  it('should display risk level', () => {
    render(<PortfolioOverview data={mockData} />)
    
    expect(screen.getByText('Low')).toBeInTheDocument()
  })

  it('should handle negative daily PnL', () => {
    const negativeData = { ...mockData, dailyPnL: -1500 }
    render(<PortfolioOverview data={negativeData} />)
    
    expect(screen.getByText(/-1,500/)).toBeInTheDocument()
  })

  it('should handle negative total PnL', () => {
    const negativeData = { ...mockData, totalPnL: -5000 }
    render(<PortfolioOverview data={negativeData} />)
    
    expect(screen.getByText(/-5,000/)).toBeInTheDocument()
  })

  it('should handle zero positions', () => {
    const zeroPositions = { ...mockData, activePositions: 0 }
    render(<PortfolioOverview data={zeroPositions} />)
    
    expect(screen.getByText('0')).toBeInTheDocument()
  })

  it('should handle medium risk level', () => {
    const mediumRisk = { ...mockData, riskLevel: 'Medium' as const }
    render(<PortfolioOverview data={mediumRisk} />)
    
    expect(screen.getByText('Medium')).toBeInTheDocument()
  })

  it('should handle high risk level', () => {
    const highRisk = { ...mockData, riskLevel: 'High' as const }
    render(<PortfolioOverview data={highRisk} />)
    
    expect(screen.getByText('High')).toBeInTheDocument()
  })

  it('should format large numbers correctly', () => {
    const largeData = { ...mockData, totalValue: 1500000 }
    render(<PortfolioOverview data={largeData} />)
    
    expect(screen.getByText(/1,500,000/)).toBeInTheDocument()
  })

  it('should handle zero PnL', () => {
    const zeroData = { ...mockData, dailyPnL: 0, totalPnL: 0 }
    render(<PortfolioOverview data={zeroData} />)
    
    const zeros = screen.getAllByText(/^0$|^\$0\.00$/)
    expect(zeros.length).toBeGreaterThanOrEqual(1)
  })

  it('should render with different portfolio values', () => {
    const values = [50000, 100000, 250000, 1000000]
    
    values.forEach(value => {
      const data = { ...mockData, totalValue: value }
      const { rerender } = render(<PortfolioOverview data={data} />)
      expect(screen.getByText(new RegExp(value.toLocaleString()))).toBeInTheDocument()
      rerender(<></>)
    })
  })

  it('should display percentage changes when positive', () => {
    render(<PortfolioOverview data={mockData} />)
    
    // Check for positive indicators (could be + sign, green color, up arrow)
    const positiveIndicators = screen.queryAllByText(/\+|%/)
    expect(positiveIndicators.length).toBeGreaterThan(0)
  })

  it('should handle fractional PnL values', () => {
    const fractionalData = { ...mockData, dailyPnL: 1234.56, totalPnL: 9876.54 }
    render(<PortfolioOverview data={fractionalData} />)
    
    expect(screen.getByText(/1,234/)).toBeInTheDocument()
  })

  it('should render all main sections', () => {
    const { container } = render(<PortfolioOverview data={mockData} />)
    
    expect(container.querySelector('.bg-white\\/5, .backdrop-blur-md')).toBeTruthy()
  })
})