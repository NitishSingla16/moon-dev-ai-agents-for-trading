"""
🌙 Moon Dev's Advanced Base Agent
Enhanced base class for all advanced trading agents, building on existing architecture
"""

import os
import sys
import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import logging

# Import existing base agent with fallback
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    from src.agents.base_agent import BaseAgent
except ImportError:
    # Fallback base agent if src is not available or has dependency issues
    class BaseAgent:
        def __init__(self, agent_type):
            self.type = agent_type
            self.start_time = datetime.now()
        
        def run(self):
            raise NotImplementedError("Each agent must implement its own run method")

class AdvancedBaseAgent(BaseAgent):
    """
    Enhanced base agent with advanced capabilities:
    - Multi-asset support
    - Self-improvement mechanisms
    - Advanced data processing
    - Performance tracking
    - Integration with multiple brokers
    """
    
    def __init__(self, agent_type: str, config: Dict[str, Any] = None):
        super().__init__(agent_type)
        
        # Enhanced configuration
        self.config = config or {}
        self.supported_assets = ["FOREX", "CRYPTO", "STOCKS", "OPTIONS", "FUTURES"]
        self.supported_brokers = ["BINANCE", "OANDA", "ALPACA", "INTERACTIVE_BROKERS"]
        
        # Performance tracking
        self.performance_metrics = {
            "total_trades": 0,
            "successful_trades": 0,
            "total_pnl": 0.0,
            "win_rate": 0.0,
            "sharpe_ratio": 0.0,
            "max_drawdown": 0.0,
            "last_updated": datetime.now()
        }
        
        # Self-improvement capabilities
        self.learning_data = []
        self.strategy_updates = []
        self.technology_monitor = {}
        
        # Enhanced logging
        self.setup_advanced_logging()
        
        # Data storage paths
        self.data_path = Path("trading_system/data") / self.type
        self.data_path.mkdir(parents=True, exist_ok=True)
        
    def setup_advanced_logging(self):
        """Setup enhanced logging for the agent"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'logs/{self.type}_agent.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(f"{self.type}_agent")
        
    def update_performance_metrics(self, trade_result: Dict[str, Any]):
        """Update performance metrics based on trade results"""
        self.performance_metrics["total_trades"] += 1
        
        if trade_result.get("success", False):
            self.performance_metrics["successful_trades"] += 1
            
        pnl = trade_result.get("pnl", 0.0)
        self.performance_metrics["total_pnl"] += pnl
        
        # Calculate win rate
        if self.performance_metrics["total_trades"] > 0:
            self.performance_metrics["win_rate"] = (
                self.performance_metrics["successful_trades"] / 
                self.performance_metrics["total_trades"]
            )
            
        self.performance_metrics["last_updated"] = datetime.now()
        
        # Save metrics
        self.save_performance_metrics()
        
    def save_performance_metrics(self):
        """Save performance metrics to file"""
        metrics_file = self.data_path / "performance_metrics.json"
        with open(metrics_file, 'w') as f:
            # Convert datetime to string for JSON serialization
            metrics_copy = self.performance_metrics.copy()
            metrics_copy["last_updated"] = metrics_copy["last_updated"].isoformat()
            json.dump(metrics_copy, f, indent=2)
            
    def load_performance_metrics(self):
        """Load performance metrics from file"""
        metrics_file = self.data_path / "performance_metrics.json"
        if metrics_file.exists():
            with open(metrics_file, 'r') as f:
                loaded_metrics = json.load(f)
                # Convert string back to datetime
                loaded_metrics["last_updated"] = datetime.fromisoformat(loaded_metrics["last_updated"])
                self.performance_metrics.update(loaded_metrics)
                
    def learn_from_market_data(self, market_data: Dict[str, Any]):
        """Process and learn from market data"""
        learning_entry = {
            "timestamp": datetime.now().isoformat(),
            "market_data": market_data,
            "agent_state": self.get_agent_state(),
            "performance": self.performance_metrics.copy()
        }
        
        self.learning_data.append(learning_entry)
        
        # Keep only recent learning data (last 1000 entries)
        if len(self.learning_data) > 1000:
            self.learning_data = self.learning_data[-1000:]
            
        # Trigger self-improvement analysis
        if len(self.learning_data) % 100 == 0:  # Every 100 entries
            self.analyze_and_improve()
            
    def analyze_and_improve(self):
        """Analyze performance and implement improvements"""
        if len(self.learning_data) < 50:  # Need minimum data
            return
            
        # Analyze recent performance trends
        recent_data = self.learning_data[-50:]
        
        # Simple improvement logic (can be enhanced with ML)
        recent_success_rate = sum(1 for entry in recent_data 
                                if entry.get("performance", {}).get("win_rate", 0) > 0.6) / len(recent_data)
        
        if recent_success_rate < 0.4:  # If performance is declining
            self.implement_strategy_adjustment()
            
        self.logger.info(f"Self-improvement analysis completed. Recent success rate: {recent_success_rate:.2f}")
        
    def implement_strategy_adjustment(self):
        """Implement strategy adjustments based on analysis"""
        adjustment = {
            "timestamp": datetime.now().isoformat(),
            "type": "performance_decline_adjustment",
            "adjustments": {
                "risk_multiplier": 0.8,  # Reduce risk
                "confidence_threshold": 0.75,  # Increase confidence requirement
                "analysis_depth": "enhanced"  # Use more thorough analysis
            }
        }
        
        self.strategy_updates.append(adjustment)
        self.logger.info("Strategy adjustment implemented due to performance decline")
        
    def get_agent_state(self) -> Dict[str, Any]:
        """Get current agent state for analysis"""
        return {
            "type": self.type,
            "performance": self.performance_metrics,
            "config": self.config,
            "learning_entries": len(self.learning_data),
            "strategy_updates": len(self.strategy_updates)
        }
        
    def monitor_technology_updates(self):
        """Monitor for new trading technologies and integrations"""
        # Placeholder for technology monitoring
        # In a real implementation, this would check for:
        # - New API endpoints
        # - Updated trading algorithms
        # - New data sources
        # - Enhanced analysis tools
        
        tech_update = {
            "timestamp": datetime.now().isoformat(),
            "status": "monitoring_active",
            "last_scan": datetime.now().isoformat()
        }
        
        self.technology_monitor.update(tech_update)
        
    async def async_run(self):
        """Asynchronous run method for concurrent operations"""
        await asyncio.gather(
            self.async_market_analysis(),
            self.async_performance_monitoring(),
            self.async_technology_monitoring()
        )
        
    async def async_market_analysis(self):
        """Asynchronous market analysis"""
        # Placeholder for async market analysis
        pass
        
    async def async_performance_monitoring(self):
        """Asynchronous performance monitoring"""
        # Placeholder for async performance monitoring
        pass
        
    async def async_technology_monitoring(self):
        """Asynchronous technology monitoring"""
        # Placeholder for async technology monitoring
        pass
        
    def run(self):
        """Enhanced run method with self-improvement capabilities"""
        self.logger.info(f"Starting {self.type} agent with advanced capabilities")
        
        # Load existing metrics
        self.load_performance_metrics()
        
        # Monitor technology updates
        self.monitor_technology_updates()
        
        # Call parent run method (to be implemented by child classes)
        try:
            super().run()
        except NotImplementedError:
            self.logger.warning("Child class must implement specific run logic")