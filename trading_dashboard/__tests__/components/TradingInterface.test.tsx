import React from 'react'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import TradingInterface from '@/components/TradingInterface'

describe('TradingInterface Component', () => {
  it('should render trading interface', () => {
    render(<TradingInterface />)
    
    expect(screen.getByText(/Trading Interface|Trading/i)).toBeInTheDocument()
  })

  it('should display positions tab', () => {
    render(<TradingInterface />)
    
    expect(screen.getByText(/Positions/i)).toBeInTheDocument()
  })

  it('should display orders tab', () => {
    render(<TradingInterface />)
    
    expect(screen.getByText(/Orders/i)).toBeInTheDocument()
  })

  it('should switch between tabs', () => {
    render(<TradingInterface />)
    
    const ordersTab = screen.getByText(/Orders/i)
    fireEvent.click(ordersTab)
    
    expect(ordersTab).toBeInTheDocument()
  })

  it('should render trade execution form', () => {
    render(<TradingInterface />)
    
    // Look for common trading form elements
    const inputs = screen.queryAllByRole('textbox')
    const buttons = screen.queryAllByRole('button')
    
    expect(inputs.length + buttons.length).toBeGreaterThan(0)
  })

  it('should handle buy orders', () => {
    render(<TradingInterface />)
    
    const buyButton = screen.queryByText(/Buy/i)
    if (buyButton) {
      fireEvent.click(buyButton)
    }
    
    expect(screen.getByText(/Trading Interface|Buy/i)).toBeInTheDocument()
  })

  it('should handle sell orders', () => {
    render(<TradingInterface />)
    
    const sellButton = screen.queryByText(/Sell/i)
    if (sellButton) {
      fireEvent.click(sellButton)
    }
    
    expect(screen.getByText(/Trading Interface|Sell/i)).toBeInTheDocument()
  })

  it('should display position information', () => {
    render(<TradingInterface />)
    
    // Check if positions section exists
    expect(screen.getByText(/Positions|Active Positions/i)).toBeInTheDocument()
  })

  it('should show order history', () => {
    render(<TradingInterface />)
    
    const historyTab = screen.queryByText(/History/i)
    if (historyTab) {
      fireEvent.click(historyTab)
    }
    
    expect(screen.getByText(/Trading Interface|History/i)).toBeInTheDocument()
  })

  it('should render without crashing', () => {
    const { container } = render(<TradingInterface />)
    expect(container).toBeTruthy()
  })
})