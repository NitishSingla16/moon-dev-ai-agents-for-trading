'use client'

import { motion } from 'framer-motion'
import { 
  TrendingUp, 
  TrendingDown, 
  DollarSign, 
  Target, 
  Shield,
  Activity
} from 'lucide-react'
import { TradingData } from '@/types/trading'

interface PortfolioOverviewProps {
  data: TradingData
}

export default function PortfolioOverview({ data }: PortfolioOverviewProps) {
  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(amount)
  }

  const formatPercent = (amount: number) => {
    return `${amount >= 0 ? '+' : ''}${amount.toFixed(2)}%`
  }

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case 'Low': return 'text-green-400 bg-green-400/20'
      case 'Medium': return 'text-yellow-400 bg-yellow-400/20'
      case 'High': return 'text-orange-400 bg-orange-400/20'
      case 'Critical': return 'text-red-400 bg-red-400/20'
      default: return 'text-gray-400 bg-gray-400/20'
    }
  }

  const stats = [
    {
      title: 'Total Portfolio Value',
      value: formatCurrency(data.totalValue),
      change: formatPercent((data.totalPnL / (data.totalValue - data.totalPnL)) * 100),
      icon: DollarSign,
      color: 'text-blue-400',
      bgColor: 'bg-blue-400/20'
    },
    {
      title: 'Daily P&L',
      value: formatCurrency(data.dailyPnL),
      change: formatPercent((data.dailyPnL / data.totalValue) * 100),
      icon: data.dailyPnL >= 0 ? TrendingUp : TrendingDown,
      color: data.dailyPnL >= 0 ? 'text-green-400' : 'text-red-400',
      bgColor: data.dailyPnL >= 0 ? 'bg-green-400/20' : 'bg-red-400/20'
    },
    {
      title: 'Total P&L',
      value: formatCurrency(data.totalPnL),
      change: formatPercent((data.totalPnL / (data.totalValue - data.totalPnL)) * 100),
      icon: data.totalPnL >= 0 ? TrendingUp : TrendingDown,
      color: data.totalPnL >= 0 ? 'text-green-400' : 'text-red-400',
      bgColor: data.totalPnL >= 0 ? 'bg-green-400/20' : 'bg-red-400/20'
    },
    {
      title: 'Active Positions',
      value: data.activePositions.toString(),
      change: 'Live',
      icon: Target,
      color: 'text-purple-400',
      bgColor: 'bg-purple-400/20'
    }
  ]

  return (
    <div className="space-y-6">
      {/* Main Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => {
          const Icon = stat.icon
          return (
            <motion.div
              key={stat.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10 hover:border-white/20 transition-all duration-300"
            >
              <div className="flex items-center justify-between mb-4">
                <div className={`p-3 rounded-lg ${stat.bgColor}`}>
                  <Icon size={24} className={stat.color} />
                </div>
                <div className="text-right">
                  <div className="text-sm text-gray-400">{stat.change}</div>
                </div>
              </div>
              
              <div>
                <h3 className="text-2xl font-bold text-white mb-1">{stat.value}</h3>
                <p className="text-sm text-gray-400">{stat.title}</p>
              </div>
            </motion.div>
          )
        })}
      </div>

      {/* Risk Overview */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10"
      >
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-semibold text-white">Risk Overview</h2>
          <div className={`px-3 py-1 rounded-full text-sm font-medium ${getRiskColor(data.riskLevel)}`}>
            {data.riskLevel} Risk
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="text-3xl font-bold text-green-400 mb-2">2.4%</div>
            <div className="text-sm text-gray-400">Max Drawdown</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-blue-400 mb-2">1.85</div>
            <div className="text-sm text-gray-400">Sharpe Ratio</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-purple-400 mb-2">0.12</div>
            <div className="text-sm text-gray-400">Beta</div>
          </div>
        </div>

        <div className="mt-6 pt-6 border-t border-white/10">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Shield size={20} className="text-green-400" />
              <span className="text-white font-medium">Risk Management Active</span>
            </div>
            <div className="flex items-center space-x-4 text-sm text-gray-400">
              <span>Stop Loss: 5%</span>
              <span>Take Profit: 15%</span>
              <span>Max Position: 10%</span>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Performance Chart Placeholder */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10"
      >
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-semibold text-white">Portfolio Performance</h2>
          <div className="flex items-center space-x-2 text-sm text-gray-400">
            <Activity size={16} />
            <span>Last 30 days</span>
          </div>
        </div>

        <div className="h-64 bg-gradient-to-r from-moon-500/20 to-primary-500/20 rounded-lg flex items-center justify-center">
          <div className="text-center">
            <TrendingUp size={48} className="text-moon-400 mx-auto mb-4" />
            <p className="text-white font-medium">Performance Chart</p>
            <p className="text-gray-400 text-sm">Real-time portfolio tracking</p>
          </div>
        </div>
      </motion.div>
    </div>
  )
}