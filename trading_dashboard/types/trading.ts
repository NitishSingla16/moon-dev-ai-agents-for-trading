export interface Agent {
  id: string
  name: string
  description: string
  icon: any
  status: 'active' | 'inactive' | 'error' | 'paused'
  confidence: number
  lastUpdate: Date
  metrics: Record<string, any>
}

export interface AgentStatus {
  id: string
  status: 'active' | 'inactive' | 'error' | 'paused'
  lastUpdate: Date
  uptime: number
  errorCount: number
}

export interface TradingData {
  totalValue: number
  dailyPnL: number
  totalPnL: number
  activePositions: number
  riskLevel: 'Low' | 'Medium' | 'High' | 'Critical'
}

export interface Position {
  id: string
  symbol: string
  amount: number
  entryPrice: number
  currentPrice: number
  pnl: number
  pnlPercent: number
  side: 'long' | 'short'
  timestamp: Date
}

export interface Trade {
  id: string
  symbol: string
  side: 'buy' | 'sell'
  amount: number
  price: number
  timestamp: Date
  agent: string
  confidence: number
}

export interface Strategy {
  id: string
  name: string
  description: string
  type: 'technical' | 'fundamental' | 'sentiment' | 'arbitrage'
  status: 'active' | 'inactive' | 'testing'
  performance: {
    totalReturn: number
    sharpeRatio: number
    maxDrawdown: number
    winRate: number
  }
  parameters: Record<string, any>
}

export interface MarketData {
  symbol: string
  price: number
  change24h: number
  volume24h: number
  marketCap: number
  timestamp: Date
}

export interface SentimentData {
  token: string
  sentiment: 'bullish' | 'bearish' | 'neutral'
  score: number
  change: number
  source: 'twitter' | 'reddit' | 'news'
  timestamp: Date
}

export interface RiskMetrics {
  portfolioValue: number
  maxDrawdown: number
  var95: number
  sharpeRatio: number
  beta: number
  correlation: number
}

export interface Alert {
  id: string
  type: 'info' | 'warning' | 'error' | 'success'
  title: string
  message: string
  timestamp: Date
  agent: string
  acknowledged: boolean
}

export interface Configuration {
  trading: {
    maxPositionSize: number
    maxDailyLoss: number
    riskLevel: 'Low' | 'Medium' | 'High'
    enableAI: boolean
  }
  agents: {
    [key: string]: {
      enabled: boolean
      parameters: Record<string, any>
    }
  }
  apis: {
    birdeye: string
    hyperliquid: string
    coingecko: string
    twitter: string
  }
}