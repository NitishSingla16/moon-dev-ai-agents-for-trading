import React from 'react'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import AgentCard from '@/components/AgentCard'
import { Agent } from '@/types/trading'
import { TrendingUp } from 'lucide-react'

describe('AgentCard Component', () => {
  const mockAgent: Agent = {
    id: 'test-agent',
    name: 'Test Trading Agent',
    description: 'A test agent for unit testing',
    icon: TrendingUp,
    status: 'active',
    confidence: 85,
    lastUpdate: new Date('2024-01-01T12:00:00'),
    metrics: {
      signals: 12,
      trades: 8,
      pnl: 2.4,
      winRate: 68
    }
  }

  it('should render agent name and description', () => {
    render(<AgentCard agent={mockAgent} />)
    
    expect(screen.getByText('Test Trading Agent')).toBeInTheDocument()
    expect(screen.getByText('A test agent for unit testing')).toBeInTheDocument()
  })

  it('should display agent status correctly', () => {
    render(<AgentCard agent={mockAgent} />)
    
    expect(screen.getByText('active')).toBeInTheDocument()
  })

  it('should show confidence score with progress bar', () => {
    render(<AgentCard agent={mockAgent} />)
    
    expect(screen.getByText('85%')).toBeInTheDocument()
    expect(screen.getByText('Confidence')).toBeInTheDocument()
  })

  it('should display metrics correctly', () => {
    render(<AgentCard agent={mockAgent} />)
    
    expect(screen.getByText('12')).toBeInTheDocument()
    expect(screen.getByText('8')).toBeInTheDocument()
    expect(screen.getByText('2.4')).toBeInTheDocument()
  })

  it('should render different status colors', () => {
    const statuses: Array<Agent['status']> = ['active', 'inactive', 'error', 'paused']
    
    statuses.forEach(status => {
      const agent = { ...mockAgent, status }
      const { rerender } = render(<AgentCard agent={agent} />)
      expect(screen.getByText(status)).toBeInTheDocument()
      rerender(<></>)
    })
  })

  it('should show live indicator for active agents', () => {
    render(<AgentCard agent={mockAgent} />)
    
    expect(screen.getByText('Live')).toBeInTheDocument()
  })

  it('should not show live indicator for inactive agents', () => {
    const inactiveAgent = { ...mockAgent, status: 'inactive' as const }
    render(<AgentCard agent={inactiveAgent} />)
    
    expect(screen.queryByText('Live')).not.toBeInTheDocument()
  })

  it('should render in detailed mode when specified', () => {
    const agentWithMoreMetrics = {
      ...mockAgent,
      metrics: {
        ...mockAgent.metrics,
        extraMetric1: 'value1',
        extraMetric2: 100
      }
    }
    
    render(<AgentCard agent={agentWithMoreMetrics} detailed />)
    
    expect(screen.getByText('Test Trading Agent')).toBeInTheDocument()
  })

  it('should handle agents with different confidence levels', () => {
    const confidenceLevels = [0, 25, 50, 75, 100]
    
    confidenceLevels.forEach(confidence => {
      const agent = { ...mockAgent, confidence }
      const { rerender } = render(<AgentCard agent={agent} />)
      expect(screen.getByText(`${confidence}%`)).toBeInTheDocument()
      rerender(<></>)
    })
  })

  it('should format time correctly', () => {
    const now = new Date()
    const agent = { ...mockAgent, lastUpdate: now }
    
    render(<AgentCard agent={agent} />)
    
    expect(screen.getByText(/Just now|ago/)).toBeInTheDocument()
  })

  it('should handle agents with minimal metrics', () => {
    const minimalAgent = {
      ...mockAgent,
      metrics: {}
    }
    
    render(<AgentCard agent={minimalAgent} />)
    
    expect(screen.getByText('Test Trading Agent')).toBeInTheDocument()
  })

  it('should display settings and control buttons', () => {
    render(<AgentCard agent={mockAgent} />)
    
    const buttons = screen.getAllByRole('button')
    expect(buttons.length).toBeGreaterThanOrEqual(2)
  })

  it('should handle different metric value types', () => {
    const agentWithMixedMetrics = {
      ...mockAgent,
      metrics: {
        number: 100,
        string: 'High',
        float: 2.4,
        percentage: 68
      }
    }
    
    render(<AgentCard agent={agentWithMixedMetrics} />)
    
    expect(screen.getByText('100')).toBeInTheDocument()
    expect(screen.getByText('High')).toBeInTheDocument()
  })

  it('should format large numbers with commas', () => {
    const agentWithLargeNumbers = {
      ...mockAgent,
      metrics: {
        trades: 1000000,
        volume: 5000000
      }
    }
    
    render(<AgentCard agent={agentWithLargeNumbers} />)
    
    expect(screen.getByText('1,000,000')).toBeInTheDocument()
  })

  it('should handle paused status correctly', () => {
    const pausedAgent = { ...mockAgent, status: 'paused' as const }
    render(<AgentCard agent={pausedAgent} />)
    
    expect(screen.getByText('paused')).toBeInTheDocument()
  })

  it('should handle error status correctly', () => {
    const errorAgent = { ...mockAgent, status: 'error' as const }
    render(<AgentCard agent={errorAgent} />)
    
    expect(screen.getByText('error')).toBeInTheDocument()
  })

  it('should render agent icon', () => {
    const { container } = render(<AgentCard agent={mockAgent} />)
    
    // Check for icon container
    const iconContainer = container.querySelector('.bg-moon-500\\/20')
    expect(iconContainer).toBeInTheDocument()
  })

  it('should handle zero confidence', () => {
    const zeroConfidenceAgent = { ...mockAgent, confidence: 0 }
    render(<AgentCard agent={zeroConfidenceAgent} />)
    
    expect(screen.getByText('0%')).toBeInTheDocument()
  })

  it('should handle 100% confidence', () => {
    const maxConfidenceAgent = { ...mockAgent, confidence: 100 }
    render(<AgentCard agent={maxConfidenceAgent} />)
    
    expect(screen.getByText('100%')).toBeInTheDocument()
  })
})