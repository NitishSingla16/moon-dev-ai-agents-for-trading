import { 
  Agent, 
  AgentStatus, 
  TradingData, 
  Position, 
  Order, 
  Strategy 
} from '@/types/trading'

describe('Trading Types', () => {
  describe('AgentStatus', () => {
    it('should have all required status values', () => {
      const statuses: AgentStatus[] = ['active', 'inactive', 'error', 'paused']
      expect(statuses).toHaveLength(4)
      expect(statuses).toContain('active')
      expect(statuses).toContain('inactive')
      expect(statuses).toContain('error')
      expect(statuses).toContain('paused')
    })
  })

  describe('Agent interface', () => {
    it('should create a valid agent object', () => {
      const mockAgent: Agent = {
        id: 'test-agent',
        name: 'Test Agent',
        description: 'A test agent for unit testing',
        icon: () => null,
        status: 'active',
        confidence: 85,
        lastUpdate: new Date('2024-01-01'),
        metrics: { trades: 10, pnl: 100 }
      }

      expect(mockAgent.id).toBe('test-agent')
      expect(mockAgent.status).toBe('active')
      expect(mockAgent.confidence).toBeGreaterThanOrEqual(0)
      expect(mockAgent.confidence).toBeLessThanOrEqual(100)
    })

    it('should handle different status types', () => {
      const statuses: AgentStatus[] = ['active', 'inactive', 'error', 'paused']
      
      statuses.forEach(status => {
        const agent: Agent = {
          id: `agent-${status}`,
          name: `Agent ${status}`,
          description: 'Test',
          icon: () => null,
          status,
          confidence: 50,
          lastUpdate: new Date(),
          metrics: {}
        }
        expect(agent.status).toBe(status)
      })
    })

    it('should handle metrics with various data types', () => {
      const agent: Agent = {
        id: 'metrics-agent',
        name: 'Metrics Test',
        description: 'Testing metrics',
        icon: () => null,
        status: 'active',
        confidence: 75,
        lastUpdate: new Date(),
        metrics: {
          trades: 100,
          pnl: 1500.50,
          winRate: 68.5,
          volume: 'High',
          risk: 'Low'
        }
      }

      expect(typeof agent.metrics.trades).toBe('number')
      expect(typeof agent.metrics.pnl).toBe('number')
      expect(typeof agent.metrics.volume).toBe('string')
    })
  })

  describe('TradingData interface', () => {
    it('should create valid trading data', () => {
      const tradingData: TradingData = {
        totalValue: 125000,
        dailyPnL: 2400,
        totalPnL: 15600,
        activePositions: 8,
        riskLevel: 'Low'
      }

      expect(tradingData.totalValue).toBeGreaterThan(0)
      expect(tradingData.activePositions).toBeGreaterThanOrEqual(0)
      expect(['Low', 'Medium', 'High']).toContain(tradingData.riskLevel)
    })

    it('should handle negative PnL values', () => {
      const tradingData: TradingData = {
        totalValue: 95000,
        dailyPnL: -1500,
        totalPnL: -5000,
        activePositions: 3,
        riskLevel: 'High'
      }

      expect(tradingData.dailyPnL).toBeLessThan(0)
      expect(tradingData.totalPnL).toBeLessThan(0)
    })

    it('should handle zero positions', () => {
      const tradingData: TradingData = {
        totalValue: 100000,
        dailyPnL: 0,
        totalPnL: 0,
        activePositions: 0,
        riskLevel: 'Low'
      }

      expect(tradingData.activePositions).toBe(0)
    })
  })

  describe('Position interface', () => {
    it('should create valid long position', () => {
      const position: Position = {
        id: 'pos-1',
        symbol: 'SOL',
        side: 'long',
        size: 100,
        entryPrice: 102.50,
        currentPrice: 105.00,
        pnl: 250,
        pnlPercentage: 2.44
      }

      expect(position.side).toBe('long')
      expect(position.pnl).toBeGreaterThan(0)
      expect(position.currentPrice).toBeGreaterThan(position.entryPrice)
    })

    it('should create valid short position', () => {
      const position: Position = {
        id: 'pos-2',
        symbol: 'BTC',
        side: 'short',
        size: 0.5,
        entryPrice: 44000,
        currentPrice: 43500,
        pnl: 250,
        pnlPercentage: 1.14
      }

      expect(position.side).toBe('short')
      expect(position.pnl).toBeGreaterThan(0)
      expect(position.currentPrice).toBeLessThan(position.entryPrice)
    })

    it('should handle losing positions', () => {
      const position: Position = {
        id: 'pos-3',
        symbol: 'ETH',
        side: 'long',
        size: 10,
        entryPrice: 2600,
        currentPrice: 2550,
        pnl: -500,
        pnlPercentage: -1.92
      }

      expect(position.pnl).toBeLessThan(0)
      expect(position.pnlPercentage).toBeLessThan(0)
    })
  })

  describe('Order interface', () => {
    it('should create valid market order', () => {
      const order: Order = {
        id: 'order-1',
        symbol: 'SOL',
        side: 'buy',
        type: 'market',
        size: 50,
        price: 102.50,
        status: 'filled',
        timestamp: new Date()
      }

      expect(order.type).toBe('market')
      expect(order.status).toBe('filled')
      expect(['buy', 'sell']).toContain(order.side)
    })

    it('should create valid limit order', () => {
      const order: Order = {
        id: 'order-2',
        symbol: 'BTC',
        side: 'sell',
        type: 'limit',
        size: 0.1,
        price: 45000,
        status: 'pending',
        timestamp: new Date()
      }

      expect(order.type).toBe('limit')
      expect(order.status).toBe('pending')
    })

    it('should handle stop-loss orders', () => {
      const order: Order = {
        id: 'order-3',
        symbol: 'ETH',
        side: 'sell',
        type: 'stop-loss',
        size: 5,
        price: 2500,
        status: 'pending',
        timestamp: new Date()
      }

      expect(order.type).toBe('stop-loss')
    })

    it('should handle cancelled orders', () => {
      const order: Order = {
        id: 'order-4',
        symbol: 'SOL',
        side: 'buy',
        type: 'limit',
        size: 100,
        price: 100,
        status: 'cancelled',
        timestamp: new Date()
      }

      expect(order.status).toBe('cancelled')
    })
  })

  describe('Strategy interface', () => {
    it('should create valid strategy', () => {
      const strategy: Strategy = {
        id: 'strat-1',
        name: 'Momentum Trading',
        description: 'Buy on momentum, sell on weakness',
        status: 'active',
        performance: {
          totalTrades: 150,
          winRate: 65.5,
          pnl: 15000,
          sharpeRatio: 1.8
        }
      }

      expect(strategy.status).toBe('active')
      expect(strategy.performance.winRate).toBeGreaterThan(0)
      expect(strategy.performance.winRate).toBeLessThanOrEqual(100)
    })

    it('should handle inactive strategies', () => {
      const strategy: Strategy = {
        id: 'strat-2',
        name: 'Grid Trading',
        description: 'Automated grid trading',
        status: 'inactive',
        performance: {
          totalTrades: 0,
          winRate: 0,
          pnl: 0,
          sharpeRatio: 0
        }
      }

      expect(strategy.status).toBe('inactive')
      expect(strategy.performance.totalTrades).toBe(0)
    })

    it('should handle strategy with negative PnL', () => {
      const strategy: Strategy = {
        id: 'strat-3',
        name: 'Failed Strategy',
        description: 'Underperforming strategy',
        status: 'active',
        performance: {
          totalTrades: 50,
          winRate: 35,
          pnl: -2500,
          sharpeRatio: -0.5
        }
      }

      expect(strategy.performance.pnl).toBeLessThan(0)
      expect(strategy.performance.sharpeRatio).toBeLessThan(0)
    })
  })
})