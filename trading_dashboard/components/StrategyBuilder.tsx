'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  Plus, 
  Play, 
  Pause, 
  Settings, 
  BarChart3, 
  Target,
  TrendingUp,
  Brain,
  Zap,
  AlertTriangle,
  CheckCircle,
  Clock,
  Download
} from 'lucide-react'
import { Strategy } from '@/types/trading'

export default function StrategyBuilder() {
  const [activeTab, setActiveTab] = useState('strategies')
  const [strategies, setStrategies] = useState<Strategy[]>([
    {
      id: '1',
      name: 'MA Crossover Strategy',
      description: 'Moving Average Crossover with 20/50 periods',
      type: 'technical',
      status: 'active',
      performance: {
        totalReturn: 24.5,
        sharpeRatio: 1.85,
        maxDrawdown: 8.2,
        winRate: 68.5
      },
      parameters: {
        fastMA: 20,
        slowMA: 50,
        timeframe: '1h'
      }
    },
    {
      id: '2',
      name: 'RSI Mean Reversion',
      description: 'RSI-based mean reversion strategy',
      type: 'technical',
      status: 'testing',
      performance: {
        totalReturn: 18.3,
        sharpeRatio: 1.42,
        maxDrawdown: 12.1,
        winRate: 61.2
      },
      parameters: {
        rsiPeriod: 14,
        oversold: 30,
        overbought: 70
      }
    },
    {
      id: '3',
      name: 'Sentiment Momentum',
      description: 'Twitter sentiment-based momentum strategy',
      type: 'sentiment',
      status: 'active',
      performance: {
        totalReturn: 31.2,
        sharpeRatio: 2.1,
        maxDrawdown: 6.8,
        winRate: 72.3
      },
      parameters: {
        sentimentThreshold: 0.7,
        volumeMultiplier: 2.0,
        timeframe: '4h'
      }
    }
  ])

  const [newStrategy, setNewStrategy] = useState({
    name: '',
    description: '',
    type: 'technical',
    parameters: {}
  })

  const tabs = [
    { id: 'strategies', label: 'My Strategies', icon: BarChart3 },
    { id: 'builder', label: 'Strategy Builder', icon: Plus },
    { id: 'backtest', label: 'Backtesting', icon: Play },
    { id: 'rbi', label: 'RBI Pipeline', icon: Brain }
  ]

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'technical': return 'text-blue-400 bg-blue-400/20'
      case 'fundamental': return 'text-green-400 bg-green-400/20'
      case 'sentiment': return 'text-purple-400 bg-purple-400/20'
      case 'arbitrage': return 'text-yellow-400 bg-yellow-400/20'
      default: return 'text-gray-400 bg-gray-400/20'
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'text-green-400 bg-green-400/20'
      case 'inactive': return 'text-gray-400 bg-gray-400/20'
      case 'testing': return 'text-yellow-400 bg-yellow-400/20'
      default: return 'text-gray-400 bg-gray-400/20'
    }
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'active': return <CheckCircle size={16} />
      case 'inactive': return <Pause size={16} />
      case 'testing': return <Clock size={16} />
      default: return <AlertTriangle size={16} />
    }
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-white">Strategy Builder</h2>
          <p className="text-gray-400">Create, test, and deploy trading strategies</p>
        </div>
        
        <div className="flex items-center space-x-4">
          <button className="flex items-center space-x-2 px-4 py-2 bg-moon-600 hover:bg-moon-700 text-white rounded-lg transition-colors">
            <Plus size={16} />
            <span>New Strategy</span>
          </button>
          
          <button className="flex items-center space-x-2 px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors">
            <Download size={16} />
            <span>Export</span>
          </button>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white/5 backdrop-blur-md rounded-xl border border-white/10">
        <div className="flex border-b border-white/10">
          {tabs.map((tab) => {
            const Icon = tab.icon
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center space-x-2 px-6 py-4 font-medium text-sm transition-colors ${
                  activeTab === tab.id
                    ? 'text-moon-400 border-b-2 border-moon-500'
                    : 'text-gray-400 hover:text-gray-300'
                }`}
              >
                <Icon size={16} />
                <span>{tab.label}</span>
              </button>
            )
          })}
        </div>

        <div className="p-6">
          {activeTab === 'strategies' && (
            <div className="space-y-6">
              {strategies.map((strategy, index) => (
                <motion.div
                  key={strategy.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10 hover:border-white/20 transition-all duration-300"
                >
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex items-center space-x-3 mb-2">
                        <h3 className="text-xl font-semibold text-white">{strategy.name}</h3>
                        <div className={`flex items-center space-x-1 px-2 py-1 rounded-full text-xs ${getTypeColor(strategy.type)}`}>
                          <span className="capitalize">{strategy.type}</span>
                        </div>
                        <div className={`flex items-center space-x-1 px-2 py-1 rounded-full text-xs ${getStatusColor(strategy.status)}`}>
                          {getStatusIcon(strategy.status)}
                          <span className="capitalize">{strategy.status}</span>
                        </div>
                      </div>
                      <p className="text-gray-300 mb-4">{strategy.description}</p>
                    </div>
                    
                    <div className="flex items-center space-x-2">
                      <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
                        <Settings size={16} className="text-gray-400" />
                      </button>
                      <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
                        <Play size={16} className="text-gray-400" />
                      </button>
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-4">
                    <div className="text-center">
                      <div className="text-2xl font-bold text-green-400 mb-1">
                        +{strategy.performance.totalReturn}%
                      </div>
                      <div className="text-sm text-gray-400">Total Return</div>
                    </div>
                    <div className="text-center">
                      <div className="text-2xl font-bold text-blue-400 mb-1">
                        {strategy.performance.sharpeRatio}
                      </div>
                      <div className="text-sm text-gray-400">Sharpe Ratio</div>
                    </div>
                    <div className="text-center">
                      <div className="text-2xl font-bold text-red-400 mb-1">
                        -{strategy.performance.maxDrawdown}%
                      </div>
                      <div className="text-sm text-gray-400">Max Drawdown</div>
                    </div>
                    <div className="text-center">
                      <div className="text-2xl font-bold text-purple-400 mb-1">
                        {strategy.performance.winRate}%
                      </div>
                      <div className="text-sm text-gray-400">Win Rate</div>
                    </div>
                  </div>

                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-4 text-sm text-gray-400">
                      <span>Parameters: {Object.keys(strategy.parameters).length}</span>
                      <span>Last Updated: 2 hours ago</span>
                    </div>
                    
                    <div className="flex space-x-2">
                      <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors">
                        Backtest
                      </button>
                      <button className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors">
                        Deploy
                      </button>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          )}

          {activeTab === 'builder' && (
            <div className="max-w-2xl mx-auto">
              <div className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Strategy Name</label>
                  <input
                    type="text"
                    placeholder="Enter strategy name"
                    className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    value={newStrategy.name}
                    onChange={(e) => setNewStrategy({...newStrategy, name: e.target.value})}
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Description</label>
                  <textarea
                    placeholder="Describe your strategy"
                    rows={3}
                    className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    value={newStrategy.description}
                    onChange={(e) => setNewStrategy({...newStrategy, description: e.target.value})}
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Strategy Type</label>
                  <select
                    className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500"
                    value={newStrategy.type}
                    onChange={(e) => setNewStrategy({...newStrategy, type: e.target.value})}
                  >
                    <option value="technical">Technical Analysis</option>
                    <option value="fundamental">Fundamental Analysis</option>
                    <option value="sentiment">Sentiment Analysis</option>
                    <option value="arbitrage">Arbitrage</option>
                  </select>
                </div>

                <div className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10">
                  <h3 className="text-lg font-semibold text-white mb-4">Strategy Template</h3>
                  <div className="space-y-4">
                    <div className="flex items-center space-x-3">
                      <input type="checkbox" className="rounded" />
                      <span className="text-white">Moving Average Crossover</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <input type="checkbox" className="rounded" />
                      <span className="text-white">RSI Mean Reversion</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <input type="checkbox" className="rounded" />
                      <span className="text-white">Bollinger Bands</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <input type="checkbox" className="rounded" />
                      <span className="text-white">MACD Signal</span>
                    </div>
                  </div>
                </div>
                
                <button className="w-full py-3 bg-moon-600 hover:bg-moon-700 text-white font-semibold rounded-lg transition-colors">
                  Create Strategy
                </button>
              </div>
            </div>
          )}

          {activeTab === 'backtest' && (
            <div className="space-y-6">
              <div className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10">
                <h3 className="text-lg font-semibold text-white mb-4">Backtest Configuration</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Strategy</label>
                    <select className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500">
                      <option>MA Crossover Strategy</option>
                      <option>RSI Mean Reversion</option>
                      <option>Sentiment Momentum</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Time Period</label>
                    <select className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500">
                      <option>Last 30 days</option>
                      <option>Last 90 days</option>
                      <option>Last 6 months</option>
                      <option>Last year</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Initial Capital</label>
                    <input
                      type="number"
                      placeholder="10000"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Symbols</label>
                    <input
                      type="text"
                      placeholder="SOL, BTC, ETH"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                </div>
                
                <div className="mt-6">
                  <button className="flex items-center space-x-2 px-6 py-3 bg-green-600 hover:bg-green-700 text-white font-semibold rounded-lg transition-colors">
                    <Play size={16} />
                    <span>Run Backtest</span>
                  </button>
                </div>
              </div>

              <div className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10">
                <h3 className="text-lg font-semibold text-white mb-4">Backtest Results</h3>
                <div className="text-center py-12">
                  <BarChart3 size={48} className="text-gray-400 mx-auto mb-4" />
                  <h4 className="text-lg font-semibold text-white mb-2">No Backtest Results</h4>
                  <p className="text-gray-400">Run a backtest to see performance metrics and charts</p>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'rbi' && (
            <div className="space-y-6">
              <div className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10">
                <h3 className="text-lg font-semibold text-white mb-4">RBI Pipeline</h3>
                <p className="text-gray-300 mb-6">
                  Research-Backtest-Implement pipeline for automated strategy development from trading ideas.
                </p>
                
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Trading Ideas</label>
                    <textarea
                      placeholder="Paste YouTube URLs, PDF links, or describe your trading idea..."
                      rows={4}
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <button className="flex items-center space-x-2 px-6 py-3 bg-moon-600 hover:bg-moon-700 text-white font-semibold rounded-lg transition-colors">
                    <Brain size={16} />
                    <span>Process with AI</span>
                  </button>
                </div>
              </div>

              <div className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10">
                <h3 className="text-lg font-semibold text-white mb-4">Generated Strategies</h3>
                <div className="text-center py-12">
                  <Zap size={48} className="text-gray-400 mx-auto mb-4" />
                  <h4 className="text-lg font-semibold text-white mb-2">No Generated Strategies</h4>
                  <p className="text-gray-400">Submit trading ideas to generate automated strategies</p>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}