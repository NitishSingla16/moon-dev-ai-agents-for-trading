'use client'

import { motion } from 'framer-motion'
import { 
  Play, 
  Pause, 
  Settings, 
  TrendingUp, 
  TrendingDown,
  AlertCircle,
  CheckCircle,
  Clock
} from 'lucide-react'
import { Agent } from '@/types/trading'

interface AgentCardProps {
  agent: Agent
  detailed?: boolean
}

export default function AgentCard({ agent, detailed = false }: AgentCardProps) {
  const Icon = agent.icon
  
  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'text-green-400 bg-green-400/20'
      case 'inactive': return 'text-gray-400 bg-gray-400/20'
      case 'error': return 'text-red-400 bg-red-400/20'
      case 'paused': return 'text-yellow-400 bg-yellow-400/20'
      default: return 'text-gray-400 bg-gray-400/20'
    }
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'active': return <CheckCircle size={16} />
      case 'inactive': return <Clock size={16} />
      case 'error': return <AlertCircle size={16} />
      case 'paused': return <Pause size={16} />
      default: return <Clock size={16} />
    }
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

  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="bg-white/5 backdrop-blur-md rounded-xl p-6 border border-white/10 hover:border-white/20 transition-all duration-300"
    >
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-3">
          <div className="p-2 bg-moon-500/20 rounded-lg">
            <Icon size={20} className="text-moon-400" />
          </div>
          <div>
            <h3 className="text-lg font-semibold text-white">{agent.name}</h3>
            <div className={`flex items-center space-x-1 px-2 py-1 rounded-full text-xs ${getStatusColor(agent.status)}`}>
              {getStatusIcon(agent.status)}
              <span className="capitalize">{agent.status}</span>
            </div>
          </div>
        </div>
        
        <div className="flex items-center space-x-2">
          <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
            <Settings size={16} className="text-gray-400" />
          </button>
          <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
            {agent.status === 'active' ? <Pause size={16} className="text-gray-400" /> : <Play size={16} className="text-gray-400" />}
          </button>
        </div>
      </div>

      {/* Description */}
      <p className="text-gray-300 text-sm mb-4">{agent.description}</p>

      {/* Confidence Score */}
      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm text-gray-400">Confidence</span>
          <span className="text-sm font-semibold text-white">{agent.confidence}%</span>
        </div>
        <div className="w-full bg-gray-700 rounded-full h-2">
          <div 
            className="bg-gradient-to-r from-moon-500 to-primary-500 h-2 rounded-full transition-all duration-500"
            style={{ width: `${agent.confidence}%` }}
          />
        </div>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-2 gap-4 mb-4">
        {Object.entries(agent.metrics).slice(0, 4).map(([key, value]) => (
          <div key={key} className="text-center">
            <div className="text-lg font-semibold text-white">
              {typeof value === 'number' ? value.toLocaleString() : value}
            </div>
            <div className="text-xs text-gray-400 capitalize">
              {key.replace(/([A-Z])/g, ' $1').trim()}
            </div>
          </div>
        ))}
      </div>

      {/* Last Update */}
      <div className="flex items-center justify-between text-xs text-gray-400">
        <span>Last update: {formatTime(agent.lastUpdate)}</span>
        {agent.status === 'active' && (
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
            <span>Live</span>
          </div>
        )}
      </div>

      {/* Detailed View */}
      {detailed && (
        <div className="mt-4 pt-4 border-t border-white/10">
          <div className="grid grid-cols-1 gap-3">
            {Object.entries(agent.metrics).slice(4).map(([key, value]) => (
              <div key={key} className="flex justify-between items-center">
                <span className="text-sm text-gray-400 capitalize">
                  {key.replace(/([A-Z])/g, ' $1').trim()}
                </span>
                <span className="text-sm font-medium text-white">
                  {typeof value === 'number' ? value.toLocaleString() : value}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </motion.div>
  )
}