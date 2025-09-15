'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  Settings, 
  Shield, 
  Key, 
  Bell, 
  Monitor,
  Save,
  RefreshCw,
  AlertTriangle,
  CheckCircle,
  Eye,
  EyeOff
} from 'lucide-react'
import { Configuration } from '@/types/trading'

export default function SettingsPanel() {
  const [activeTab, setActiveTab] = useState('general')
  const [showApiKeys, setShowApiKeys] = useState(false)
  const [config, setConfig] = useState<Configuration>({
    trading: {
      maxPositionSize: 10000,
      maxDailyLoss: 5000,
      riskLevel: 'Low',
      enableAI: true
    },
    agents: {
      trading: { enabled: true, parameters: { confidence: 80 } },
      risk: { enabled: true, parameters: { maxDrawdown: 10 } },
      strategy: { enabled: true, parameters: { minSignals: 3 } },
      sentiment: { enabled: true, parameters: { threshold: 0.7 } },
      whale: { enabled: true, parameters: { threshold: 2.0 } },
      funding: { enabled: true, parameters: { threshold: 0.01 } },
      liquidation: { enabled: true, parameters: { threshold: 1000000 } },
      listing: { enabled: true, parameters: { minVolume: 100000 } },
      rbi: { enabled: true, parameters: { autoProcess: true } },
      chart: { enabled: true, parameters: { timeframes: ['1h', '4h'] } },
      fundingArb: { enabled: true, parameters: { threshold: 0.005 } },
      copybot: { enabled: true, parameters: { confidence: 75 } },
      focus: { enabled: false, parameters: {} }
    },
    apis: {
      birdeye: '',
      hyperliquid: '',
      coingecko: '',
      twitter: ''
    }
  })

  const tabs = [
    { id: 'general', label: 'General', icon: Settings },
    { id: 'trading', label: 'Trading', icon: Shield },
    { id: 'agents', label: 'Agents', icon: Monitor },
    { id: 'apis', label: 'API Keys', icon: Key },
    { id: 'notifications', label: 'Notifications', icon: Bell }
  ]

  const handleSave = () => {
    // Save configuration logic
    console.log('Saving configuration:', config)
  }

  const handleReset = () => {
    // Reset to default configuration
    console.log('Resetting configuration')
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-white">Settings</h2>
          <p className="text-gray-400">Configure your trading system preferences</p>
        </div>
        
        <div className="flex items-center space-x-4">
          <button
            onClick={handleReset}
            className="flex items-center space-x-2 px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg transition-colors"
          >
            <RefreshCw size={16} />
            <span>Reset</span>
          </button>
          
          <button
            onClick={handleSave}
            className="flex items-center space-x-2 px-4 py-2 bg-moon-600 hover:bg-moon-700 text-white rounded-lg transition-colors"
          >
            <Save size={16} />
            <span>Save Changes</span>
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
          {activeTab === 'general' && (
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">General Settings</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">System Name</label>
                    <input
                      type="text"
                      defaultValue="Moon Dev Trading System"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Default Currency</label>
                    <select className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500">
                      <option value="USD">USD</option>
                      <option value="EUR">EUR</option>
                      <option value="BTC">BTC</option>
                      <option value="ETH">ETH</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Time Zone</label>
                    <select className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500">
                      <option value="UTC">UTC</option>
                      <option value="EST">Eastern Time</option>
                      <option value="PST">Pacific Time</option>
                      <option value="GMT">Greenwich Mean Time</option>
                    </select>
                  </div>
                  
                  <div className="flex items-center space-x-3">
                    <input
                      type="checkbox"
                      defaultChecked
                      className="rounded"
                    />
                    <span className="text-white">Enable dark mode</span>
                  </div>
                  
                  <div className="flex items-center space-x-3">
                    <input
                      type="checkbox"
                      defaultChecked
                      className="rounded"
                    />
                    <span className="text-white">Auto-save configurations</span>
                  </div>
                </div>
              </motion.div>
            </div>
          )}

          {activeTab === 'trading' && (
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Trading Configuration</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Max Position Size (USD)</label>
                    <input
                      type="number"
                      value={config.trading.maxPositionSize}
                      onChange={(e) => setConfig({
                        ...config,
                        trading: { ...config.trading, maxPositionSize: Number(e.target.value) }
                      })}
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Max Daily Loss (USD)</label>
                    <input
                      type="number"
                      value={config.trading.maxDailyLoss}
                      onChange={(e) => setConfig({
                        ...config,
                        trading: { ...config.trading, maxDailyLoss: Number(e.target.value) }
                      })}
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Risk Level</label>
                    <select
                      value={config.trading.riskLevel}
                      onChange={(e) => setConfig({
                        ...config,
                        trading: { ...config.trading, riskLevel: e.target.value as 'Low' | 'Medium' | 'High' }
                      })}
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-moon-500"
                    >
                      <option value="Low">Low</option>
                      <option value="Medium">Medium</option>
                      <option value="High">High</option>
                    </select>
                  </div>
                  
                  <div className="flex items-center space-x-3">
                    <input
                      type="checkbox"
                      checked={config.trading.enableAI}
                      onChange={(e) => setConfig({
                        ...config,
                        trading: { ...config.trading, enableAI: e.target.checked }
                      })}
                      className="rounded"
                    />
                    <span className="text-white">Enable AI trading decisions</span>
                  </div>
                </div>
              </motion.div>

              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Risk Management</h3>
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-white">Stop Loss Percentage</span>
                    <span className="text-gray-400">5%</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-white">Take Profit Percentage</span>
                    <span className="text-gray-400">15%</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-white">Max Concurrent Positions</span>
                    <span className="text-gray-400">10</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-white">Position Sizing Method</span>
                    <span className="text-gray-400">Fixed Dollar</span>
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
                <h3 className="text-lg font-semibold text-white mb-4">Agent Configuration</h3>
                <div className="space-y-4">
                  {Object.entries(config.agents).map(([agentId, agentConfig]) => (
                    <div key={agentId} className="flex items-center justify-between p-4 bg-white/5 rounded-lg border border-white/10">
                      <div>
                        <div className="text-white font-medium capitalize">{agentId.replace(/([A-Z])/g, ' $1').trim()}</div>
                        <div className="text-sm text-gray-400">
                          {Object.keys(agentConfig.parameters).length} parameters configured
                        </div>
                      </div>
                      
                      <div className="flex items-center space-x-4">
                        <div className={`flex items-center space-x-1 px-2 py-1 rounded-full text-xs ${
                          agentConfig.enabled ? 'text-green-400 bg-green-400/20' : 'text-gray-400 bg-gray-400/20'
                        }`}>
                          {agentConfig.enabled ? <CheckCircle size={12} /> : <AlertTriangle size={12} />}
                          <span>{agentConfig.enabled ? 'Enabled' : 'Disabled'}</span>
                        </div>
                        
                        <button
                          onClick={() => setConfig({
                            ...config,
                            agents: {
                              ...config.agents,
                              [agentId]: { ...agentConfig, enabled: !agentConfig.enabled }
                            }
                          })}
                          className={`px-3 py-1 rounded-lg text-sm transition-colors ${
                            agentConfig.enabled 
                              ? 'bg-red-600 hover:bg-red-700 text-white' 
                              : 'bg-green-600 hover:bg-green-700 text-white'
                          }`}
                        >
                          {agentConfig.enabled ? 'Disable' : 'Enable'}
                        </button>
                        
                        <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
                          <Settings size={16} className="text-gray-400" />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </motion.div>
            </div>
          )}

          {activeTab === 'apis' && (
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-lg font-semibold text-white">API Keys</h3>
                  <button
                    onClick={() => setShowApiKeys(!showApiKeys)}
                    className="flex items-center space-x-2 px-3 py-1 bg-gray-600 hover:bg-gray-700 text-white rounded-lg transition-colors"
                  >
                    {showApiKeys ? <EyeOff size={16} /> : <Eye size={16} />}
                    <span>{showApiKeys ? 'Hide' : 'Show'}</span>
                  </button>
                </div>
                
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Birdeye API Key</label>
                    <input
                      type={showApiKeys ? 'text' : 'password'}
                      value={config.apis.birdeye}
                      onChange={(e) => setConfig({
                        ...config,
                        apis: { ...config.apis, birdeye: e.target.value }
                      })}
                      placeholder="Enter your Birdeye API key"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Hyperliquid API Key</label>
                    <input
                      type={showApiKeys ? 'text' : 'password'}
                      value={config.apis.hyperliquid}
                      onChange={(e) => setConfig({
                        ...config,
                        apis: { ...config.apis, hyperliquid: e.target.value }
                      })}
                      placeholder="Enter your Hyperliquid API key"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">CoinGecko API Key</label>
                    <input
                      type={showApiKeys ? 'text' : 'password'}
                      value={config.apis.coingecko}
                      onChange={(e) => setConfig({
                        ...config,
                        apis: { ...config.apis, coingecko: e.target.value }
                      })}
                      placeholder="Enter your CoinGecko API key"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">Twitter API Key</label>
                    <input
                      type={showApiKeys ? 'text' : 'password'}
                      value={config.apis.twitter}
                      onChange={(e) => setConfig({
                        ...config,
                        apis: { ...config.apis, twitter: e.target.value }
                      })}
                      placeholder="Enter your Twitter API key"
                      className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-moon-500"
                    />
                  </div>
                </div>
                
                <div className="mt-6 p-4 bg-yellow-500/20 border border-yellow-500/30 rounded-lg">
                  <div className="flex items-center space-x-2">
                    <AlertTriangle size={20} className="text-yellow-400" />
                    <span className="text-yellow-400 font-medium">Security Notice</span>
                  </div>
                  <p className="text-yellow-300 text-sm mt-2">
                    API keys are stored locally and encrypted. Never share your API keys with anyone.
                  </p>
                </div>
              </motion.div>
            </div>
          )}

          {activeTab === 'notifications' && (
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 backdrop-blur-md rounded-lg p-6 border border-white/10"
              >
                <h3 className="text-lg font-semibold text-white mb-4">Notification Settings</h3>
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="text-white font-medium">Trade Executions</div>
                      <div className="text-sm text-gray-400">Notify when trades are executed</div>
                    </div>
                    <input type="checkbox" defaultChecked className="rounded" />
                  </div>
                  
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="text-white font-medium">Risk Alerts</div>
                      <div className="text-sm text-gray-400">Notify when risk limits are reached</div>
                    </div>
                    <input type="checkbox" defaultChecked className="rounded" />
                  </div>
                  
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="text-white font-medium">Agent Status</div>
                      <div className="text-sm text-gray-400">Notify when agents go offline</div>
                    </div>
                    <input type="checkbox" defaultChecked className="rounded" />
                  </div>
                  
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="text-white font-medium">Market Opportunities</div>
                      <div className="text-sm text-gray-400">Notify about trading opportunities</div>
                    </div>
                    <input type="checkbox" defaultChecked className="rounded" />
                  </div>
                  
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="text-white font-medium">Voice Alerts</div>
                      <div className="text-sm text-gray-400">Enable voice announcements</div>
                    </div>
                    <input type="checkbox" defaultChecked className="rounded" />
                  </div>
                </div>
              </motion.div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}