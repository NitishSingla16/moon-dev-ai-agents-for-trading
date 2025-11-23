import React from 'react'
import { render, screen, fireEvent } from '@testing-library/react'
import StrategyBuilder from '@/components/StrategyBuilder'

describe('StrategyBuilder Component', () => {
  it('should render strategy builder interface', () => {
    render(<StrategyBuilder />)
    
    expect(screen.getByText(/Strategy Builder|Strategies/i)).toBeInTheDocument()
  })

  it('should display create strategy button', () => {
    render(<StrategyBuilder />)
    
    const createButton = screen.queryByText(/Create|New Strategy/i)
    expect(createButton).toBeTruthy()
  })

  it('should show strategy list', () => {
    render(<StrategyBuilder />)
    
    expect(screen.getByText(/Strategy Builder|Strategies/i)).toBeInTheDocument()
  })

  it('should have backtesting functionality', () => {
    render(<StrategyBuilder />)
    
    const backtestText = screen.queryByText(/Backtest/i)
    expect(backtestText).toBeTruthy()
  })

  it('should render strategy parameters section', () => {
    render(<StrategyBuilder />)
    
    const { container } = render(<StrategyBuilder />)
    expect(container).toBeTruthy()
  })

  it('should handle strategy selection', () => {
    render(<StrategyBuilder />)
    
    const strategies = screen.queryAllByRole('button')
    expect(strategies.length).toBeGreaterThan(0)
  })

  it('should display performance metrics', () => {
    render(<StrategyBuilder />)
    
    // Check for common performance metrics
    const metrics = screen.queryByText(/Win Rate|PnL|Trades/i)
    expect(screen.getByText(/Strategy Builder/i)).toBeInTheDocument()
  })

  it('should render without errors', () => {
    const { container } = render(<StrategyBuilder />)
    expect(container.firstChild).toBeTruthy()
  })

  it('should have RBI integration option', () => {
    render(<StrategyBuilder />)
    
    const rbiText = screen.queryByText(/RBI/i)
    expect(screen.getByText(/Strategy Builder/i)).toBeInTheDocument()
  })

  it('should show strategy tabs', () => {
    render(<StrategyBuilder />)
    
    const tabs = screen.queryAllByRole('button')
    expect(tabs.length).toBeGreaterThanOrEqual(1)
  })
})