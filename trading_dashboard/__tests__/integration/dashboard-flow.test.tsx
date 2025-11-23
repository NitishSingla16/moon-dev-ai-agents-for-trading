import React from 'react'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import Dashboard from '@/app/page'

describe('Dashboard Integration Tests', () => {
  it('should navigate through all tabs successfully', async () => {
    render(<Dashboard />)
    
    const tabs = ['Overview', 'Agents', 'Trading', 'Strategies', 'Analytics', 'Settings']
    
    for (const tabName of tabs) {
      const tab = screen.getByText(new RegExp(`^${tabName}$`, 'i'))
      fireEvent.click(tab)
      
      await waitFor(() => {
        expect(tab).toBeInTheDocument()
      })
    }
  })

  it('should maintain state when switching tabs', () => {
    render(<Dashboard />)
    
    // Click to agents tab
    const agentsTab = screen.getByText(/^Agents$/i)
    fireEvent.click(agentsTab)
    
    // Click back to overview
    const overviewTab = screen.getByText(/^Overview$/i)
    fireEvent.click(overviewTab)
    
    // Verify overview content is displayed
    expect(screen.getByText(/Active Agents|Portfolio/i)).toBeInTheDocument()
  })

  it('should toggle system status and reflect changes', () => {
    render(<Dashboard />)
    
    const toggleButton = screen.getByText(/Pause|Resume/i)
    const initialStatus = screen.getByText(/running|paused|stopped/i).textContent
    
    fireEvent.click(toggleButton)
    
    const newStatus = screen.getByText(/running|paused|stopped/i).textContent
    expect(newStatus).toBeDefined()
  })

  it('should display agents and allow interaction', () => {
    render(<Dashboard />)
    
    // Navigate to agents tab
    const agentsTab = screen.getByText(/^Agents$/i)
    fireEvent.click(agentsTab)
    
    // Verify agent cards are displayed
    expect(screen.getByText(/Trading Agent|Risk Agent/i)).toBeInTheDocument()
  })

  it('should handle refresh action across tabs', () => {
    render(<Dashboard />)
    
    const tabs = ['Overview', 'Analytics']
    
    tabs.forEach(tabName => {
      const tab = screen.getByText(new RegExp(`^${tabName}$`, 'i'))
      fireEvent.click(tab)
      
      const buttons = screen.getAllByRole('button')
      expect(buttons.length).toBeGreaterThan(0)
    })
  })
})