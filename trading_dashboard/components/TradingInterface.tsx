'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  TrendingUp, 
  TrendingDown, 
  DollarSign, 
  Target, 
  Clock,
  AlertTriangle,
  CheckCircle,
  X,
  Play,
  Pause,
  RefreshCw
} from 'lucide-react'
import { Position, Trade } from '@/types/trading'

export default function TradingInterface() {
  const [activeTab, setActiveTab] = useState('positions')
  const [positions, setPositions] = useState<Position[]>([
    {
      id: '1',
      symbol: 'SOL',
      amount: 150.5,
      entryPrice: 98.50,
      currentPrice: 102.30,
      pnl: 572.25,
      pnlPercent: 3.86,
      side: 'long',
      timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000)
    },
    {
      id: '2',
      symbol: 'BTC',
      amount: 0.25,
      entryPrice: 43200.00,
      currentPrice: 44150.00,
      pnl: 237.50,
      pnlPercent: 2.20,
      side: 'long',
      timestamp: new Date(Date.now() - 4 * 60 * 60 * 1000)
    },
    {
      id: '3',
      symbol: 'ETH',
      amount: 2.1,
      entryPrice: 2650.00,
      currentPrice: 2580.00,
      pnl: -147.00,
      pnlPercent: -2.64,
      side: 'short',
      timestamp: new Date(Date.now() - 1 * 60 * 60 * 1000)
    }
  ])

  const [recentTrades, setRecentTrades] = useState<Trade[]>([
    {
      id: '1',
      symbol: 'SOL',
      side: 'buy',
      amount: 50.0,
      price: 101.80,
      timestamp: new Date(Date.now() - 30 * 60 * 1000),
      agent: 'Trading Agent',
      confidence: 85
    },
    {
      id: '2',
      symbol: 'BTC',
      side: 'sell',
      amount: 0.1,
      price: 44000.00,
      timestamp: new Date(Date.now() - 45 * 60 * 1000),
      agent: 'Risk Agent',
      confidence: 92
    },
    {
      id: '3',
      symbol: 'ETH',
      side: 'buy',
      amount: 1.5,
      price: 2590.00,
      timestamp: new Date(Date.now() - 60 * 60 * 1000),
      agent: 'Strategy Agent',
      confidence: 78
    }
  ])

  const [isTradingActive, setIsTradingActive] = useState(true)

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    }).format(amount)
  }

  const formatPercent = (amount: number) => {
    return `${amount >= 0 ? '+' : ''}${amount.toFixed(2)}%`
  }

  const formatTime = (date: Date) => {
    const now = new Date()
    const diff = now.getTime() - date.getTime()
    const minutes = Math.floor(diff / 60000)
    
    if (minutes < 1) return 'Just now'
    if (minutes < 60) return `${minutes}m ago`
    const hours = Math.floor(minutes / 60)
    if (hours < 24) return `${hours}h ago`
    const days = Math.floor(hours / 24)
    return `${days}d ago`
  }

  const totalPnL = positions.reduce((sum, pos) => sum + pos.pnl, 0)
  const totalValue = positions.reduce((sum, pos) => sum + (pos.amount * pos.currentPrice), 0)

  const tabs = [
    { id: 'positions', label: 'Positions', icon: Target },
    { id: 'trades', label: 'Recent Trades', icon: Clock },
    { id: 'orders', label: 'Open Orders', icon: AlertTriangle },
    { id: 'manual', label: 'Manual Trade', icon: DollarSign }
  ]

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-white">Trading Interface</h2>
          <p className="text-gray-400">Monitor and manage your trading positions</p>
        </div>
        
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <div className={`w-3 h-3 rounded-full ${isTradingActive ? 'bg-green-500 animate-pulse' : 'bg-red-500'}`} />
            <span className="text-sm text-gray-300">
              {isTradingActive ? 'Trading Active' : 'Trading Paused'}
            </span>
          </div>
          
          <button
            onClick={() => setIsTradingActive(!isTradingActive)}
            className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-colors ${
              isTradingActive 
                ? 'bg-red-600 hover:bg-red-700 text-white' 
                : 'bg-green-600 hover:bg-green-700 text-white'
            }`}
          >
            {isTradingActive ? <Pause size={16} /> : <Play size={16} />}
            <span>{isTradingActive ? 'Pause Trading' : 'Resume Trading'}</span>
          </button>
          
          <button className="p-2 bg-gray-700 hover:bg-gray-600 text-white rounded-lg transition-colors">
            <RefreshCw size={16} />
          </button>
        </div>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-blue-400/20 rounded-lg">
              <DollarSign size={24} className="text-blue-400" />
            </div>
            <div className="text-right">
              <div className="text-sm text-gray-400">Total Value</div>
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{formatCurrency(totalValue)}</div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10"
        >
          <div className="flex items-center justify-between mb-4">
            <div className={`p-3 rounded-lg ${totalPnL >= 0 ? 'bg-green-400/20' : 'bg-red-400/20'}`}>
              {totalPnL >= 0 ? <TrendingUp size={24} className="text-green-400" /> : <TrendingDown size={24} className="text-red-400" />}
            </div>
            <div className="text-right">
              <div className="text-sm text-gray-400">Total P&L</div>
            </div>
          </div>
          <div className={`text-2xl font-bold ${totalPnL >= 0 ? 'text-green-400' : 'text-red-400'}`}>
            {formatCurrency(totalPnL)}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-purple-400/20 rounded-lg">
              <Target size={24} className="text-purple-400" />
            </div>
            <div className="text-right">
              <div className="text-sm text-gray-400">Positions</div>
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{positions.length}</div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10"
        >
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-yellow-400/20 rounded-lg">
              <Clock size={24} className="text-yellow-400" />
            </div>
            <div className="text-right">
              <div className="text-sm text-gray-400">Today's Trades</div>
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{recentTrades.length}</div>
        </motion.div>
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
          {activeTab === 'positions' && (
            <div className="space-y-4">
              {positions.map((position, index) => (
                <motion.div
                  key={position.id}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-4 border border-white/10 hover:border-white/20 transition-all duration-300"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-4">
                      <div className="text-center">
                        <div className="text-lg font-semibold text-white">{position.symbol}</div>
                        <div className="text-xs text-gray-400">{position.side.toUpperCase()}</div>
                      </div>
                      
                      <div className="text-center">
                        <div className="text-sm text-gray-400">Amount</div>
                        <div className="text-white font-medium">{position.amount}</div>
                      </div>
                      
                      <div className="text-center">
                        <div className="text-sm text-gray-400">Entry Price</div>
                        <div className="text-white font-medium">{formatCurrency(position.entryPrice)}</div>
                      </div>
                      
                      <div className="text-center">
                        <div className="text-sm text-gray-400">Current Price</div>
                        <div className="text-white font-medium">{formatCurrency(position.currentPrice)}</div>
                      </div>
                    </div>
                    
                    <div className="flex items-center space-x-6">
                      <div className="text-right">
                        <div className={`text-lg font-semibold ${position.pnl >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                          {formatCurrency(position.pnl)}
                        </div>
                        <div className={`text-sm ${position.pnl >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                          {formatPercent(position.pnlPercent)}
                        </div>
                      </div>
                      
                      <div className="text-right">
                        <div className="text-xs text-gray-400">Opened</div>
                        <div className="text-sm text-white">{formatTime(position.timestamp)}</div>
                      </div>
                      
                      <div className="flex space-x-2">
                        <button className="p-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors">
                          <CheckCircle size={16} />
                        </button>
                        <button className="p-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors">
                          <X size={16} />
                        </button>
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          )}

          {activeTab === 'trades' && (
            <div className="space-y-4">
              {recentTrades.map((trade, index) => (
                <motion.div
                  key={trade.id}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-4 border border-white/10"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-4">
                      <div className={`p-2 rounded-lg ${trade.side === 'buy' ? 'bg-green-400/20' : 'bg-red-400/20'}`}>
                        {trade.side === 'buy' ? <TrendingUp size={16} className="text-green-400" /> : <TrendingDown size={16} className="text-red-400" />}
                      </div>
                      
                      <div>
                        <div className="text-lg font-semibold text-white">{trade.symbol}</div>
                        <div className="text-sm text-gray-400">{trade.agent}</div>
                      </div>
                      
                      <div className="text-center">
                        <div className="text-sm text-gray-400">Amount</div>
                        <div className="text-white font-medium">{trade.amount}</div>
                      </div>
                      
                      <div className="text-center">
                        <div className="text-sm text-gray-400">Price</div>
                        <div className="text-white font-medium">{formatCurrency(trade.price)}</div>
                      </div>
                    </div>
                    
                    <div className="flex items-center space-x-6">
                      <div className="text-right">
                        <div className="text-sm text-gray-400">Confidence</div>
                        <div className="text-white font-medium">{trade.confidence}%</div>
                      </div>
                      
                      <div className="text-right">
                        <div className="text-xs text-gray-400">Time</div>
                        <div className="text-sm text-white">{formatTime(trade.timestamp)}</div>
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          )}

          {activeTab === 'orders' && (
            <div className="text-center py-12">
              <AlertTriangle size={48} className="text-gray-400 mx-auto mb-4" />
              <h3 className="text-lg font-semibold text-white mb-2">No Open Orders</h3>
              <p className="text-gray-400">All orders have been executed or cancelled</p>
            </div>
          )}

          {activeTab === 'manual' && (
            <div className="max-w-md mx-auto">
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Symbol</label>
                  <input
                    type="text"
                    placeholder="e.g., SOL, BTC, ETH"
                    className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Side</label>
                  <select className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500">
                    <option value="buy">Buy</option>
                    <option value="sell">Sell</option>
                  </select>
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Amount</label>
                  <input
                    type="number"
                    placeholder="0.00"
                    className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                  />
                </div>
                
                <button className="w-full py-3 bg-moon-600 hover:bg-moon-700 text-white font-semibold rounded-lg transition-colors">
                  Execute Trade
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}