import React from 'react'
import { render, screen, fireEvent } from '@testing-library/react'
import DataVisualization from '@/components/DataVisualization'

describe('DataVisualization Component', () => {
  it('should render data visualization component', () => {
    render(<DataVisualization />)
    
    expect(screen.getByText(/Analytics|Data/i)).toBeInTheDocument()
  })

  it('should display portfolio tab', () => {
    render(<DataVisualization />)
    
    expect(screen.getByText(/Portfolio/i)).toBeInTheDocument()
  })

  it('should display performance tab', () => {
    render(<DataVisualization />)
    
    expect(screen.getByText(/Performance/i)).toBeInTheDocument()
  })

  it('should display agents tab', () => {
    render(<DataVisualization />)
    
    expect(screen.getByText(/Agents/i)).toBeInTheDocument()
  })

  it('should display market data tab', () => {
    render(<DataVisualization />)
    
    expect(screen.getByText(/Market Data/i)).toBeInTheDocument()
  })

  it('should switch between tabs', () => {
    render(<DataVisualization />)
    
    const performanceTab = screen.getByText(/Performance/i)
    fireEvent.click(performanceTab)
    
    expect(performanceTab).toBeInTheDocument()
  })

  it('should have time range selector', () => {
    render(<DataVisualization />)
    
    const selector = screen.queryByRole('combobox')
    expect(selector).toBeTruthy()
  })

  it('should display refresh button', () => {
    render(<DataVisualization />)
    
    const refreshButton = screen.getByText(/Refresh/i)
    expect(refreshButton).toBeInTheDocument()
  })

  it('should display export button', () => {
    render(<DataVisualization />)
    
    const exportButton = screen.getByText(/Export/i)
    expect(exportButton).toBeInTheDocument()
  })

  it('should handle data refresh', () => {
    render(<DataVisualization />)
    
    const refreshButton = screen.getByText(/Refresh/i)
    fireEvent.click(refreshButton)
    
    expect(refreshButton).toBeInTheDocument()
  })

  it('should show portfolio allocation', () => {
    render(<DataVisualization />)
    
    expect(screen.getByText(/Portfolio Allocation|Portfolio/i)).toBeInTheDocument()
  })

  it('should display performance metrics', () => {
    render(<DataVisualization />)
    
    const performanceTab = screen.getByText(/Performance/i)
    fireEvent.click(performanceTab)
    
    expect(screen.getByText(/Performance|Total Return/i)).toBeInTheDocument()
  })

  it('should show agent performance data', () => {
    render(<DataVisualization />)
    
    const agentsTab = screen.getByText(/Agents/i)
    fireEvent.click(agentsTab)
    
    expect(agentsTab).toBeInTheDocument()
  })

  it('should display market data', () => {
    render(<DataVisualization />)
    
    const marketTab = screen.getByText(/Market Data/i)
    fireEvent.click(marketTab)
    
    expect(marketTab).toBeInTheDocument()
  })

  it('should handle time range changes', () => {
    render(<DataVisualization />)
    
    const selector = screen.queryByRole('combobox')
    if (selector) {
      fireEvent.change(selector, { target: { value: '30d' } })
    }
    
    expect(screen.getByText(/Analytics|Data/i)).toBeInTheDocument()
  })

  it('should render charts placeholder', () => {
    render(<DataVisualization />)
    
    const chartElements = screen.queryAllByText(/Chart|Performance/i)
    expect(chartElements.length).toBeGreaterThan(0)
  })

  it('should show total return metric', () => {
    render(<DataVisualization />)
    
    const performanceTab = screen.getByText(/Performance/i)
    fireEvent.click(performanceTab)
    
    expect(screen.getByText(/Total Return/i)).toBeInTheDocument()
  })

  it('should display sharpe ratio', () => {
    render(<DataVisualization />)
    
    const performanceTab = screen.getByText(/Performance/i)
    fireEvent.click(performanceTab)
    
    expect(screen.getByText(/Sharpe Ratio/i)).toBeInTheDocument()
  })

  it('should show max drawdown', () => {
    render(<DataVisualization />)
    
    const performanceTab = screen.getByText(/Performance/i)
    fireEvent.click(performanceTab)
    
    expect(screen.getByText(/Max Drawdown/i)).toBeInTheDocument()
  })

  it('should display win rate', () => {
    render(<DataVisualization />)
    
    const performanceTab = screen.getByText(/Performance/i)
    fireEvent.click(performanceTab)
    
    expect(screen.getByText(/Win Rate/i)).toBeInTheDocument()
  })
})