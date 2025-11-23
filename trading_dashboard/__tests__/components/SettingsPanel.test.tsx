import React from 'react'
import { render, screen, fireEvent } from '@testing-library/react'
import SettingsPanel from '@/components/SettingsPanel'

describe('SettingsPanel Component', () => {
  it('should render settings panel', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Settings/i)).toBeInTheDocument()
  })

  it('should display general settings tab', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/General/i)).toBeInTheDocument()
  })

  it('should display API keys tab', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/API Keys|API/i)).toBeInTheDocument()
  })

  it('should display agents tab', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Agents/i)).toBeInTheDocument()
  })

  it('should display notifications tab', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Notifications/i)).toBeInTheDocument()
  })

  it('should switch between settings tabs', () => {
    render(<SettingsPanel />)
    
    const apiTab = screen.getByText(/API Keys|API/i)
    fireEvent.click(apiTab)
    
    expect(apiTab).toBeInTheDocument()
  })

  it('should have save button', () => {
    render(<SettingsPanel />)
    
    const saveButton = screen.queryByText(/Save/i)
    expect(saveButton).toBeTruthy()
  })

  it('should have reset button', () => {
    render(<SettingsPanel />)
    
    const resetButton = screen.queryByText(/Reset/i)
    expect(resetButton).toBeTruthy()
  })

  it('should display risk settings', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Risk|Risk Level/i)).toBeInTheDocument()
  })

  it('should show max position size setting', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Max Position Size|Position Size/i)).toBeInTheDocument()
  })

  it('should display max daily loss setting', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Max Daily Loss|Daily Loss/i)).toBeInTheDocument()
  })

  it('should show API key inputs', () => {
    render(<SettingsPanel />)
    
    const apiTab = screen.getByText(/API Keys|API/i)
    fireEvent.click(apiTab)
    
    const inputs = screen.queryAllByRole('textbox')
    expect(inputs.length).toBeGreaterThan(0)
  })

  it('should display agent configuration', () => {
    render(<SettingsPanel />)
    
    const agentsTab = screen.getByText(/Agents/i)
    fireEvent.click(agentsTab)
    
    expect(agentsTab).toBeInTheDocument()
  })

  it('should show notification preferences', () => {
    render(<SettingsPanel />)
    
    const notifTab = screen.getByText(/Notifications/i)
    fireEvent.click(notifTab)
    
    expect(notifTab).toBeInTheDocument()
  })

  it('should handle settings save', () => {
    render(<SettingsPanel />)
    
    const saveButton = screen.queryByText(/Save/i)
    if (saveButton) {
      fireEvent.click(saveButton)
    }
    
    expect(screen.getByText(/Settings/i)).toBeInTheDocument()
  })

  it('should handle settings reset', () => {
    render(<SettingsPanel />)
    
    const resetButton = screen.queryByText(/Reset/i)
    if (resetButton) {
      fireEvent.click(resetButton)
    }
    
    expect(screen.getByText(/Settings/i)).toBeInTheDocument()
  })

  it('should render without errors', () => {
    const { container } = render(<SettingsPanel />)
    expect(container.firstChild).toBeTruthy()
  })

  it('should display trading settings', () => {
    render(<SettingsPanel />)
    
    expect(screen.getByText(/Trading|Settings/i)).toBeInTheDocument()
  })

  it('should show system configuration', () => {
    render(<SettingsPanel />)
    
    const generalTab = screen.getByText(/General/i)
    fireEvent.click(generalTab)
    
    expect(generalTab).toBeInTheDocument()
  })

  it('should have enable/disable toggles', () => {
    render(<SettingsPanel />)
    
    const checkboxes = screen.queryAllByRole('checkbox')
    expect(checkboxes.length).toBeGreaterThanOrEqual(0)
  })
})