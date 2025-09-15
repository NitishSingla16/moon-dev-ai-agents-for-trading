'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  TrendingUp, 
  Shield, 
  Brain, 
  Twitter, 
  Whale, 
  DollarSign, 
  AlertTriangle, 
  Target, 
  BarChart3, 
  Zap, 
  Copy, 
  Focus, 
  Activity,
  Settings,
  Play,
  Pause,
  RefreshCw
} from 'lucide-react'
import AgentCard from '@/components/AgentCard'
import TradingInterface from '@/components/TradingInterface'
import StrategyBuilder from '@/components/StrategyBuilder'
import DataVisualization from '@/components/DataVisualization'
import SettingsPanel from '@/components/SettingsPanel'
import PortfolioOverview from '@/components/PortfolioOverview'
import { Agent, AgentStatus, TradingData } from '@/types/trading'

const agents: Agent[] = [
  {
    id: 'trading',
    name: 'Trading Agent',
    description: 'Core LLM-based trading decisions with market analysis',
    icon: TrendingUp,
    status: 'active',
    confidence: 85,
    lastUpdate: new Date(),
    metrics: { signals: 12, trades: 8, pnl: 2.4 }
  },
  {
    id: 'risk',
    name: 'Risk Agent',
    description: 'Portfolio risk management and capital protection',
    icon: Shield,
    status: 'active',
    confidence: 92,
    lastUpdate: new Date(),
    metrics: { positions: 5, risk: 'Low', pnl: 1.8 }
  },
  {
    id: 'strategy',
    name: 'Strategy Agent',
    description: 'Integrates rule-based strategies with AI oversight',
    icon: Brain,
    status: 'active',
    confidence: 78,
    lastUpdate: new Date(),
    metrics: { strategies: 3, signals: 15, accuracy: 73 }
  },
  {
    id: 'sentiment',
    name: 'Sentiment Agent',
    description: 'Social sentiment analysis for trading decisions',
    icon: Twitter,
    status: 'active',
    confidence: 67,
    lastUpdate: new Date(),
    metrics: { tokens: 8, sentiment: 'Bullish', change: 12 }
  },
  {
    id: 'whale',
    name: 'Whale Agent',
    description: 'Detects large capital movements and whale activity',
    icon: Whale,
    status: 'active',
    confidence: 81,
    lastUpdate: new Date(),
    metrics: { alerts: 3, oi_change: 15, volume: 'High' }
  },
  {
    id: 'funding',
    name: 'Funding Agent',
    description: 'Monitors funding rates for arbitrage opportunities',
    icon: DollarSign,
    status: 'active',
    confidence: 89,
    lastUpdate: new Date(),
    metrics: { rates: 12, arbitrage: 2, profit: 0.8 }
  },
  {
    id: 'liquidation',
    name: 'Liquidation Agent',
    description: 'Tracks liquidation events for market insights',
    icon: AlertTriangle,
    status: 'active',
    confidence: 76,
    lastUpdate: new Date(),
    metrics: { events: 45, spikes: 2, impact: 'Medium' }
  },
  {
    id: 'listing',
    name: 'Listing Arbitrage',
    description: 'Discovers early-stage tokens before major listings',
    icon: Target,
    status: 'active',
    confidence: 71,
    lastUpdate: new Date(),
    metrics: { tokens: 25, analyzed: 8, opportunities: 3 }
  },
  {
    id: 'rbi',
    name: 'RBI Agent',
    description: 'Research-Backtest-Implement pipeline automation',
    icon: BarChart3,
    status: 'active',
    confidence: 83,
    lastUpdate: new Date(),
    metrics: { ideas: 5, backtests: 3, strategies: 2 }
  },
  {
    id: 'chart',
    name: 'Chart Analysis',
    description: 'Automated technical analysis using AI vision',
    icon: Activity,
    status: 'active',
    confidence: 79,
    lastUpdate: new Date(),
    metrics: { charts: 12, patterns: 6, signals: 4 }
  },
  {
    id: 'funding-arb',
    name: 'Funding Arbitrage',
    description: 'Identifies funding rate arbitrage opportunities',
    icon: Zap,
    status: 'active',
    confidence: 86,
    lastUpdate: new Date(),
    metrics: { scans: 24, opportunities: 1, profit: 0.3 }
  },
  {
    id: 'copybot',
    name: 'Copy Bot Agent',
    description: 'AI-driven oversight of copy trading positions',
    icon: Copy,
    status: 'active',
    confidence: 74,
    lastUpdate: new Date(),
    metrics: { positions: 7, analysis: 12, actions: 3 }
  },
  {
    id: 'focus',
    name: 'Focus Agent',
    description: 'Concentration on specific market opportunities',
    icon: Focus,
    status: 'inactive',
    confidence: 0,
    lastUpdate: new Date(),
    metrics: { focus: 0, opportunities: 0, actions: 0 }
  }
]

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview')
  const [systemStatus, setSystemStatus] = useState<'running' | 'paused' | 'stopped'>('running')
  const [tradingData, setTradingData] = useState<TradingData>({
    totalValue: 125000,
    dailyPnL: 2400,
    totalPnL: 15600,
    activePositions: 8,
    riskLevel: 'Low'
  })

  const toggleSystemStatus = () => {
    if (systemStatus === 'running') {
      setSystemStatus('paused')
    } else if (systemStatus === 'paused') {
      setSystemStatus('running')
    } else {
      setSystemStatus('running')
    }
  }

  const refreshData = () => {
    // Simulate data refresh
    setTradingData(prev => ({
      ...prev,
      dailyPnL: prev.dailyPnL + (Math.random() - 0.5) * 1000,
      totalValue: prev.totalValue + (Math.random() - 0.5) * 5000
    }))
  }

  const tabs = [
    { id: 'overview', label: 'Overview', icon: BarChart3 },
    { id: 'agents', label: 'Agents', icon: Brain },
    { id: 'trading', label: 'Trading', icon: TrendingUp },
    { id: 'strategies', label: 'Strategies', icon: Target },
    { id: 'analytics', label: 'Analytics', icon: Activity },
    { id: 'settings', label: 'Settings', icon: Settings }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-violet-900">
      {/* Header */}
      <header className="bg-black/20 backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-4">
              <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ type: "spring", stiffness: 200 }}
                className="text-2xl font-bold gradient-text"
              >
                🌙 Moon Dev Trading
              </motion.div>
              <div className="hidden md:block text-sm text-gray-300">
                AI-Powered Algorithmic Trading System
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <div className={`w-3 h-3 rounded-full ${
                  systemStatus === 'running' ? 'bg-green-500 animate-pulse' :
                  systemStatus === 'paused' ? 'bg-yellow-500' : 'bg-red-500'
                }`} />
                <span className="text-sm text-gray-300 capitalize">{systemStatus}</span>
              </div>
              
              <button
                onClick={toggleSystemStatus}
                className="flex items-center space-x-2 px-4 py-2 bg-moon-600 hover:bg-moon-700 text-white rounded-lg transition-colors"
              >
                {systemStatus === 'running' ? <Pause size={16} /> : <Play size={16} />}
                <span>{systemStatus === 'running' ? 'Pause' : 'Resume'}</span>
              </button>
              
              <button
                onClick={refreshData}
                className="p-2 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors"
              >
                <RefreshCw size={16} />
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Navigation Tabs */}
      <nav className="bg-black/10 backdrop-blur-md border-b border-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-8">
            {tabs.map((tab) => {
              const Icon = tab.icon
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center space-x-2 py-4 px-1 border-b-2 font-medium text-sm transition-colors ${
                    activeTab === tab.id
                      ? 'border-moon-500 text-moon-400'
                      : 'border-transparent text-gray-400 hover:text-gray-300 hover:border-gray-300'
                  }`}
                >
                  <Icon size={16} />
                  <span>{tab.label}</span>
                </button>
              )
            })}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'overview' && (
          <div className="space-y-8">
            <PortfolioOverview data={tradingData} />
            
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              <div className="lg:col-span-2">
                <h2 className="text-2xl font-bold text-white mb-6">Active Agents</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {agents.filter(agent => agent.status === 'active').map((agent, index) => (
                    <motion.div
                      key={agent.id}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: index * 0.1 }}
                    >
                      <AgentCard agent={agent} />
                    </motion.div>
                  ))}
                </div>
              </div>
              
              <div className="space-y-6">
                <div className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10">
                  <h3 className="text-lg font-semibold text-white mb-4">System Health</h3>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-300">Active Agents</span>
                      <span className="text-green-400 font-semibold">
                        {agents.filter(a => a.status === 'active').length}/13
                      </span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-300">System Uptime</span>
                      <span className="text-blue-400 font-semibold">99.8%</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-300">API Status</span>
                      <span className="text-green-400 font-semibold">Connected</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-300">Risk Level</span>
                      <span className="text-yellow-400 font-semibold">Low</span>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10">
                  <h3 className="text-lg font-semibold text-white mb-4">Recent Activity</h3>
                  <div className="space-y-3">
                    <div className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                      <span className="text-sm text-gray-300">Trading Agent executed BUY order</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                      <span className="text-sm text-gray-300">Whale Agent detected large OI change</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-yellow-500 rounded-full"></div>
                      <span className="text-sm text-gray-300">Risk Agent adjusted position size</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                      <span className="text-sm text-gray-300">Sentiment Agent updated analysis</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'agents' && (
          <div className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-bold text-white">Trading Agents</h2>
              <div className="flex space-x-4">
                <button className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors">
                  Start All
                </button>
                <button className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors">
                  Stop All
                </button>
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {agents.map((agent, index) => (
                <motion.div
                  key={agent.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                >
                  <AgentCard agent={agent} detailed />
                </motion.div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'trading' && <TradingInterface />}
        {activeTab === 'strategies' && <StrategyBuilder />}
        {activeTab === 'analytics' && <DataVisualization />}
        {activeTab === 'settings' && <SettingsPanel />}
      </main>
    </div>
  )
}