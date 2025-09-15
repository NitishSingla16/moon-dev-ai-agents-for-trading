'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  BarChart3, 
  TrendingUp, 
  TrendingDown, 
  Activity,
  PieChart,
  LineChart,
  Calendar,
  Filter,
  Download,
  RefreshCw
} from 'lucide-react'

export default function DataVisualization() {
  const [activeTab, setActiveTab] = useState('portfolio')
  const [timeRange, setTimeRange] = useState('7d')
  const [isLoading, setIsLoading] = useState(false)

  const tabs = [
    { id: 'portfolio', label: 'Portfolio', icon: PieChart },
    { id: 'performance', label: 'Performance', icon: LineChart },
    { id: 'agents', label: 'Agents', icon: Activity },
    { id: 'market', label: 'Market Data', icon: BarChart3 }
  ]

  const timeRanges = [
    { value: '1d', label: '1 Day' },
    { value: '7d', label: '7 Days' },
    { value: '30d', label: '30 Days' },
    { value: '90d', label: '90 Days' },
    { value: '1y', label: '1 Year' }
  ]

  const portfolioData = [
    { name: 'SOL', value: 45000, percentage: 36, color: 'bg-blue-500' },
    { name: 'BTC', value: 35000, percentage: 28, color: 'bg-orange-500' },
    { name: 'ETH', value: 25000, percentage: 20, color: 'bg-purple-500' },
    { name: 'Other', value: 20000, percentage: 16, color: 'bg-gray-500' }
  ]

  const performanceData = [
    { date: '2024-01-01', value: 100000, pnl: 0 },
    { date: '2024-01-02', value: 102500, pnl: 2500 },
    { date: '2024-01-03', value: 101200, pnl: 1200 },
    { date: '2024-01-04', value: 103800, pnl: 3800 },
    { date: '2024-01-05', value: 105600, pnl: 5600 },
    { date: '2024-01-06', value: 104200, pnl: 4200 },
    { date: '2024-01-07', value: 106800, pnl: 6800 }
  ]

  const agentPerformance = [
    { name: 'Trading Agent', trades: 45, winRate: 68, pnl: 2400, color: 'bg-green-500' },
    { name: 'Risk Agent', trades: 12, winRate: 92, pnl: 1800, color: 'bg-blue-500' },
    { name: 'Strategy Agent', trades: 28, winRate: 73, pnl: 1600, color: 'bg-purple-500' },
    { name: 'Sentiment Agent', trades: 35, winRate: 61, pnl: 1200, color: 'bg-yellow-500' },
    { name: 'Whale Agent', trades: 8, winRate: 75, pnl: 800, color: 'bg-red-500' }
  ]

  const marketData = [
    { symbol: 'SOL', price: 102.30, change: 3.86, volume: 1250000, marketCap: 45000000000 },
    { symbol: 'BTC', price: 44150.00, change: 2.20, volume: 25000000000, marketCap: 870000000000 },
    { symbol: 'ETH', price: 2580.00, change: -2.64, volume: 15000000000, marketCap: 310000000000 },
    { symbol: 'BNB', price: 315.50, change: 1.45, volume: 800000000, marketCap: 48000000000 }
  ]

  const refreshData = () => {
    setIsLoading(true)
    setTimeout(() => {
      setIsLoading(false)
    }, 1000)
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-white">Analytics & Data</h2>
          <p className="text-gray-400">Comprehensive trading analytics and market insights</p>
        </div>
        
        <div className="flex items-center space-x-4">
          <select
            value={timeRange}
            onChange={(e) => setTimeRange(e.target.value)}
            className="px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500"
          >
            {timeRanges.map((range) => (
              <option key={range.value} value={range.value}>
                {range.label}
              </option>
            ))}
          </select>
          
          <button
            onClick={refreshData}
            disabled={isLoading}
            className="flex items-center space-x-2 px-4 py-2 bg-moon-600 hover:bg-moon-700 disabled:opacity-50 text-white rounded-lg transition-colors"
          >
            <RefreshCw size={16} className={isLoading ? 'animate-spin' : ''} />
            <span>Refresh</span>
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
          {activeTab === 'portfolio' && (
            <div className="space-y-6">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* Portfolio Allocation */}
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
                >
                  <h3 className="text-lg font-semibold text-white mb-4">Portfolio Allocation</h3>
                  <div className="space-y-4">
                    {portfolioData.map((item, index) => (
                      <div key={item.name} className="flex items-center justify-between">
                        <div className="flex items-center space-x-3">
                          <div className={`w-4 h-4 rounded-full ${item.color}`} />
                          <span className="text-white font-medium">{item.name}</span>
                        </div>
                        <div className="text-right">
                          <div className="text-white font-semibold">${item.value.toLocaleString()}</div>
                          <div className="text-sm text-gray-400">{item.percentage}%</div>
                        </div>
                      </div>
                    ))}
                  </div>
                  
                  <div className="mt-6 pt-4 border-t border-white/10">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-400">Total Value</span>
                      <span className="text-white font-semibold">$125,000</span>
                    </div>
                  </div>
                </motion.div>

                {/* Performance Metrics */}
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
                >
                  <h3 className="text-lg font-semibold text-white mb-4">Performance Metrics</h3>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-400">Total Return</span>
                      <span className="text-green-400 font-semibold">+12.5%</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-400">Sharpe Ratio</span>
                      <span className="text-white font-semibold">1.85</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-400">Max Drawdown</span>
                      <span className="text-red-400 font-semibold">-8.2%</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-400">Win Rate</span>
                      <span className="text-white font-semibold">68.5%</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-gray-400">Avg Trade Duration</span>
                      <span className="text-white font-semibold">4.2h</span>
                    </div>
                  </div>
                </motion.div>
              </div>

              {/* Portfolio Performance Chart */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Portfolio Performance</h3>
                <div className="h-64 bg-gradient-to-r from-moon-500/20 to-primary-500/20 rounded-lg flex items-center justify-center">
                  <div className="text-center">
                    <LineChart size={48} className="text-moon-400 mx-auto mb-4" />
                    <p className="text-white font-medium">Performance Chart</p>
                    <p className="text-gray-400 text-sm">Portfolio value over time</p>
                  </div>
                </div>
              </motion.div>
            </div>
          )}

          {activeTab === 'performance' && (
            <div className="space-y-6">
              {/* Performance Overview */}
              <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10 text-center"
                >
                  <TrendingUp size={32} className="text-green-400 mx-auto mb-2" />
                  <div className="text-2xl font-bold text-green-400 mb-1">+12.5%</div>
                  <div className="text-sm text-gray-400">Total Return</div>
                </motion.div>

                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10 text-center"
                >
                  <Activity size={32} className="text-blue-400 mx-auto mb-2" />
                  <div className="text-2xl font-bold text-blue-400 mb-1">1.85</div>
                  <div className="text-sm text-gray-400">Sharpe Ratio</div>
                </motion.div>

                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.2 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10 text-center"
                >
                  <TrendingDown size={32} className="text-red-400 mx-auto mb-2" />
                  <div className="text-2xl font-bold text-red-400 mb-1">-8.2%</div>
                  <div className="text-sm text-gray-400">Max Drawdown</div>
                </motion.div>

                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.3 }}
                  className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10 text-center"
                >
                  <BarChart3 size={32} className="text-purple-400 mx-auto mb-2" />
                  <div className="text-2xl font-bold text-purple-400 mb-1">68.5%</div>
                  <div className="text-sm text-gray-400">Win Rate</div>
                </motion.div>
              </div>

              {/* Performance Chart */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.4 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Performance Over Time</h3>
                <div className="h-80 bg-gradient-to-r from-moon-500/20 to-primary-500/20 rounded-lg flex items-center justify-center">
                  <div className="text-center">
                    <LineChart size={64} className="text-moon-400 mx-auto mb-4" />
                    <p className="text-white font-medium text-lg">Performance Chart</p>
                    <p className="text-gray-400">Detailed performance metrics and trends</p>
                  </div>
                </div>
              </motion.div>
            </div>
          )}

          {activeTab === 'agents' && (
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Agent Performance</h3>
                <div className="space-y-4">
                  {agentPerformance.map((agent, index) => (
                    <motion.div
                      key={agent.name}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.1 }}
                      className="flex items-center justify-between p-4 bg-white/5 rounded-lg border border-white/10"
                    >
                      <div className="flex items-center space-x-4">
                        <div className={`w-4 h-4 rounded-full ${agent.color}`} />
                        <div>
                          <div className="text-white font-medium">{agent.name}</div>
                          <div className="text-sm text-gray-400">{agent.trades} trades</div>
                        </div>
                      </div>
                      
                      <div className="flex items-center space-x-6">
                        <div className="text-center">
                          <div className="text-white font-semibold">{agent.winRate}%</div>
                          <div className="text-xs text-gray-400">Win Rate</div>
                        </div>
                        <div className="text-center">
                          <div className="text-green-400 font-semibold">+${agent.pnl.toLocaleString()}</div>
                          <div className="text-xs text-gray-400">P&L</div>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </motion.div>
            </div>
          )}

          {activeTab === 'market' && (
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Market Data</h3>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr className="border-b border-white/10">
                        <th className="text-left py-3 px-4 text-gray-400 font-medium">Symbol</th>
                        <th className="text-right py-3 px-4 text-gray-400 font-medium">Price</th>
                        <th className="text-right py-3 px-4 text-gray-400 font-medium">Change</th>
                        <th className="text-right py-3 px-4 text-gray-400 font-medium">Volume</th>
                        <th className="text-right py-3 px-4 text-gray-400 font-medium">Market Cap</th>
                      </tr>
                    </thead>
                    <tbody>
                      {marketData.map((item, index) => (
                        <motion.tr
                          key={item.symbol}
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: index * 0.1 }}
                          className="border-b border-white/5 hover:bg-white/5 transition-colors"
                        >
                          <td className="py-3 px-4">
                            <div className="text-white font-medium">{item.symbol}</div>
                          </td>
                          <td className="py-3 px-4 text-right">
                            <div className="text-white font-semibold">${item.price.toLocaleString()}</div>
                          </td>
                          <td className="py-3 px-4 text-right">
                            <div className={`font-semibold ${item.change >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                              {item.change >= 0 ? '+' : ''}{item.change}%
                            </div>
                          </td>
                          <td className="py-3 px-4 text-right">
                            <div className="text-white">${(item.volume / 1000000).toFixed(1)}M</div>
                          </td>
                          <td className="py-3 px-4 text-right">
                            <div className="text-white">${(item.marketCap / 1000000000).toFixed(1)}B</div>
                          </td>
                        </motion.tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </motion.div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}