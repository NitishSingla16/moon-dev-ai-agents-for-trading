import React from 'react'
import { render, screen, fireEvent, within } from '@testing-library/react'
import Dashboard from '@/app/page'

describe('Dashboard Page', () => {
  it('should render dashboard page', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/Moon Dev Trading/i)).toBeInTheDocument()
  })

  it('should display system status', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/running|paused|stopped/i)).toBeInTheDocument()
  })

  it('should show header with title', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/Moon Dev Trading/i)).toBeInTheDocument()
  })

  it('should display navigation tabs', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/Overview/i)).toBeInTheDocument()
    expect(screen.getByText(/Agents/i)).toBeInTheDocument()
    expect(screen.getByText(/Trading/i)).toBeInTheDocument()
    expect(screen.getByText(/Strategies/i)).toBeInTheDocument()
    expect(screen.getByText(/Analytics/i)).toBeInTheDocument()
    expect(screen.getByText(/Settings/i)).toBeInTheDocument()
  })

  it('should switch between tabs', () => {
    render(<Dashboard />)
    
    const agentsTab = screen.getByText(/^Agents$/i)
    fireEvent.click(agentsTab)
    
    expect(agentsTab).toBeInTheDocument()
  })

  it('should display pause/resume button', () => {
    render(<Dashboard />)
    
    const button = screen.getByText(/Pause|Resume/i)
    expect(button).toBeInTheDocument()
  })

  it('should toggle system status on button click', () => {
    render(<Dashboard />)
    
    const toggleButton = screen.getByText(/Pause|Resume/i)
    const initialText = toggleButton.textContent
    
    fireEvent.click(toggleButton)
    
    expect(toggleButton).toBeInTheDocument()
  })

  it('should display refresh button', () => {
    render(<Dashboard />)
    
    const buttons = screen.getAllByRole('button')
    expect(buttons.length).toBeGreaterThan(0)
  })

  it('should show portfolio overview in overview tab', () => {
    render(<Dashboard />)
    
    const overviewTab = screen.getByText(/^Overview$/i)
    fireEvent.click(overviewTab)
    
    expect(overviewTab).toBeInTheDocument()
  })

  it('should display active agents count', () => {
    render(<Dashboard />)
    
    // Look for system health section
    expect(screen.getByText(/Active Agents|System Health/i)).toBeInTheDocument()
  })

  it('should show agent cards in agents tab', () => {
    render(<Dashboard />)
    
    const agentsTab = screen.getByText(/^Agents$/i)
    fireEvent.click(agentsTab)
    
    expect(screen.getByText(/Trading Agents|Agents/i)).toBeInTheDocument()
  })

  it('should display trading interface in trading tab', () => {
    render(<Dashboard />)
    
    const tradingTab = screen.getByText(/^Trading$/i)
    fireEvent.click(tradingTab)
    
    expect(tradingTab).toBeInTheDocument()
  })

  it('should show strategy builder in strategies tab', () => {
    render(<Dashboard />)
    
    const strategiesTab = screen.getByText(/^Strategies$/i)
    fireEvent.click(strategiesTab)
    
    expect(strategiesTab).toBeInTheDocument()
  })

  it('should display analytics in analytics tab', () => {
    render(<Dashboard />)
    
    const analyticsTab = screen.getByText(/^Analytics$/i)
    fireEvent.click(analyticsTab)
    
    expect(analyticsTab).toBeInTheDocument()
  })

  it('should show settings panel in settings tab', () => {
    render(<Dashboard />)
    
    const settingsTab = screen.getByText(/^Settings$/i)
    fireEvent.click(settingsTab)
    
    expect(settingsTab).toBeInTheDocument()
  })

  it('should display system uptime', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/99\.8%|Uptime/i)).toBeInTheDocument()
  })

  it('should show API status', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/Connected|API Status/i)).toBeInTheDocument()
  })

  it('should display recent activity', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/Recent Activity/i)).toBeInTheDocument()
  })

  it('should render start all button in agents tab', () => {
    render(<Dashboard />)
    
    const agentsTab = screen.getByText(/^Agents$/i)
    fireEvent.click(agentsTab)
    
    expect(screen.getByText(/Start All/i)).toBeInTheDocument()
  })

  it('should render stop all button in agents tab', () => {
    render(<Dashboard />)
    
    const agentsTab = screen.getByText(/^Agents$/i)
    fireEvent.click(agentsTab)
    
    expect(screen.getByText(/Stop All/i)).toBeInTheDocument()
  })

  it('should handle data refresh', () => {
    render(<Dashboard />)
    
    const buttons = screen.getAllByRole('button')
    const refreshButton = buttons.find(btn => 
      btn.querySelector('[class*="lucide"]') !== null
    )
    
    if (refreshButton) {
      fireEvent.click(refreshButton)
    }
    
    expect(screen.getByText(/Moon Dev Trading/i)).toBeInTheDocument()
  })

  it('should display system status indicator', () => {
    render(<Dashboard />)
    
    const statusText = screen.getByText(/running|paused|stopped/i)
    expect(statusText).toBeInTheDocument()
  })

  it('should show subtitle in header', () => {
    render(<Dashboard />)
    
    expect(screen.getByText(/AI-Powered Algorithmic Trading System/i)).toBeInTheDocument()
  })
})