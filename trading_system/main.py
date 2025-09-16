"""
🌙 Moon Dev's Advanced AI Trading System
Main orchestrator for the comprehensive self-improving AI trading system
"""

import asyncio
import sys
import os
from datetime import datetime
from typing import Dict, List, Any
import logging
from pathlib import Path
import signal

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import existing Moon Dev infrastructure
from src.config import *
from termcolor import cprint

# Import new trading system components
from trading_system.core.agents import (
    MultiAssetAgent, 
    RiskManagementAgent,
    AdvancedBaseAgent
)
from trading_system.core.brokers import BrokerManager
from trading_system.intelligence.learning import ContinuousLearner
from trading_system.intelligence.analytics import QuantitativeAnalyzer
from trading_system.infrastructure.monitoring import SystemMonitor

class AdvancedTradingSystem:
    """
    Advanced AI Trading System Orchestrator
    
    Coordinates all components:
    - Multi-asset trading agents
    - Risk management
    - Broker integrations
    - Self-improvement learning
    - Advanced analytics
    - System monitoring
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or self.load_default_config()
        
        # Setup comprehensive logging
        self.setup_logging()
        self.logger = logging.getLogger("trading_system")
        
        # System components
        self.broker_manager = None
        self.multi_asset_agent = None
        self.risk_agent = None
        self.continuous_learner = None
        self.quantitative_analyzer = None
        self.system_monitor = None
        
        # System state
        self.is_running = False
        self.start_time = None
        self.shutdown_requested = False
        
        # Performance tracking
        self.system_metrics = {
            "agents_active": 0,
            "brokers_connected": 0,
            "trades_executed": 0,
            "learning_cycles": 0,
            "uptime_hours": 0
        }
        
        # Initialize components
        self.initialize_components()
        
        # Setup signal handlers for graceful shutdown
        self.setup_signal_handlers()
    
    def load_default_config(self) -> Dict[str, Any]:
        """Load default system configuration"""
        return {
            "system": {
                "name": "Moon Dev Advanced AI Trading System",
                "version": "1.0.0",
                "environment": "development",
                "max_concurrent_agents": 10,
                "health_check_interval": 60,
                "auto_restart": True
            },
            "brokers": {
                "binance": {
                    "enabled": True,
                    "api_key": os.getenv("BINANCE_API_KEY", ""),
                    "api_secret": os.getenv("BINANCE_API_SECRET", ""),
                    "sandbox": True
                },
                "oanda": {
                    "enabled": False,
                    "api_key": os.getenv("OANDA_API_KEY", ""),
                    "account_id": os.getenv("OANDA_ACCOUNT_ID", ""),
                    "environment": "practice"
                },
                "alpaca": {
                    "enabled": False,
                    "api_key": os.getenv("ALPACA_API_KEY", ""),
                    "api_secret": os.getenv("ALPACA_API_SECRET", ""),
                    "paper": True
                },
                "interactive_brokers": {
                    "enabled": False,
                    "host": "127.0.0.1",
                    "port": 7497,
                    "client_id": 1
                }
            },
            "agents": {
                "multi_asset": {
                    "enabled": True,
                    "update_interval": 60,
                    "max_positions": 10
                },
                "risk_management": {
                    "enabled": True,
                    "check_interval": 30,
                    "max_portfolio_risk": 0.02,
                    "max_drawdown": 0.15
                }
            },
            "learning": {
                "enabled": True,
                "learning_rate": 0.01,
                "memory_size": 10000,
                "update_frequency": 100
            },
            "monitoring": {
                "enabled": True,
                "interval": 30,
                "retention_days": 30,
                "alert_thresholds": {
                    "cpu_percent": 80,
                    "memory_percent": 85,
                    "disk_percent": 90
                }
            }
        }
    
    def setup_logging(self):
        """Setup comprehensive logging system"""
        # Create logs directory
        logs_path = Path("logs")
        logs_path.mkdir(exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/trading_system.log'),
                logging.StreamHandler()
            ]
        )
        
        # Set specific log levels
        logging.getLogger('trading_system').setLevel(logging.INFO)
        logging.getLogger('system_monitor').setLevel(logging.INFO)
        logging.getLogger('broker_manager').setLevel(logging.INFO)
    
    def initialize_components(self):
        """Initialize all system components"""
        try:
            cprint("🚀 Initializing Advanced AI Trading System Components...", "cyan")
            
            # Initialize system monitoring first
            if self.config["monitoring"]["enabled"]:
                self.system_monitor = SystemMonitor(self.config["monitoring"])
                cprint("✅ System Monitor initialized", "green")
            
            # Initialize broker manager
            self.broker_manager = BrokerManager(self.config)
            cprint("✅ Broker Manager initialized", "green")
            
            # Initialize continuous learner
            if self.config["learning"]["enabled"]:
                self.continuous_learner = ContinuousLearner(self.config["learning"])
                cprint("✅ Continuous Learner initialized", "green")
            
            # Initialize quantitative analyzer
            self.quantitative_analyzer = QuantitativeAnalyzer()
            cprint("✅ Quantitative Analyzer initialized", "green")
            
            # Initialize trading agents
            if self.config["agents"]["multi_asset"]["enabled"]:
                self.multi_asset_agent = MultiAssetAgent(self.config["agents"]["multi_asset"])
                cprint("✅ Multi-Asset Agent initialized", "green")
            
            if self.config["agents"]["risk_management"]["enabled"]:
                self.risk_agent = RiskManagementAgent(self.config["agents"]["risk_management"])
                cprint("✅ Risk Management Agent initialized", "green")
            
            cprint("🎉 All components initialized successfully!", "green", "on_blue")
            
        except Exception as e:
            cprint(f"❌ Error initializing components: {str(e)}", "red")
            raise
    
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            cprint(f"\n🛑 Received signal {signum}, initiating graceful shutdown...", "yellow")
            self.shutdown_requested = True
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    async def start_system(self):
        """Start the trading system"""
        if self.is_running:
            self.logger.warning("System already running")
            return
        
        try:
            cprint("🌙 Starting Moon Dev Advanced AI Trading System...", "white", "on_blue")
            
            self.start_time = datetime.now()
            self.is_running = True
            
            # Start system monitoring
            if self.system_monitor:
                self.system_monitor.start_monitoring()
                cprint("📊 System monitoring started", "cyan")
            
            # Connect to brokers
            connection_results = self.broker_manager.connect_all_brokers()
            connected_brokers = sum(1 for success in connection_results.values() if success)
            self.system_metrics["brokers_connected"] = connected_brokers
            
            cprint(f"🔗 Connected to {connected_brokers}/{len(connection_results)} brokers", "cyan")
            
            # Start main trading loop
            await self.main_trading_loop()
            
        except Exception as e:
            cprint(f"❌ Error starting system: {str(e)}", "red")
            self.logger.error(f"System startup error: {str(e)}")
            raise
    
    async def main_trading_loop(self):
        """Main trading system loop"""
        cprint("🔄 Starting main trading loop...", "cyan")
        
        cycle_count = 0
        
        while self.is_running and not self.shutdown_requested:
            try:
                cycle_start = datetime.now()
                cycle_count += 1
                
                # Health check
                if cycle_count % 10 == 0:  # Every 10 cycles
                    await self.perform_health_check()
                
                # Risk management check
                if self.risk_agent:
                    risk_status = await self.run_risk_management()
                    if not risk_status.get("continue_trading", True):
                        cprint("⚠️ Risk management halted trading", "yellow")
                        await asyncio.sleep(60)  # Wait before next check
                        continue
                
                # Multi-asset trading
                if self.multi_asset_agent:
                    await self.run_multi_asset_trading()
                
                # Learning and adaptation
                if self.continuous_learner and cycle_count % 5 == 0:  # Every 5 cycles
                    await self.run_learning_cycle()
                
                # Update system metrics
                self.update_system_metrics()
                
                # Log cycle completion
                cycle_duration = (datetime.now() - cycle_start).total_seconds()
                self.logger.info(f"Trading cycle {cycle_count} completed in {cycle_duration:.2f}s")
                
                # Sleep until next cycle
                await asyncio.sleep(30)  # 30 second cycles
                
            except Exception as e:
                self.logger.error(f"Error in trading loop cycle {cycle_count}: {str(e)}")
                cprint(f"❌ Error in cycle {cycle_count}: {str(e)}", "red")
                await asyncio.sleep(60)  # Longer wait on error
        
        cprint("🛑 Main trading loop stopped", "yellow")
    
    async def run_risk_management(self) -> Dict[str, Any]:
        """Run risk management checks"""
        try:
            # Get current positions from broker manager
            positions = self.broker_manager.get_consolidated_positions()
            balance = self.broker_manager.get_consolidated_balance()
            
            # Update risk agent with current data
            sample_pnl = 0.0  # Would calculate from actual positions
            market_data = {"positions": positions, "balance": balance}
            
            self.risk_agent.update_portfolio_metrics(
                positions.get("binance", {}), 
                sample_pnl, 
                market_data
            )
            
            # Check drawdown protection
            protection_status = self.risk_agent.check_drawdown_protection()
            
            return {
                "continue_trading": not protection_status.get("halt_trading", False),
                "reduce_exposure": protection_status.get("reduce_exposure", False),
                "protection_status": protection_status
            }
            
        except Exception as e:
            self.logger.error(f"Error in risk management: {str(e)}")
            return {"continue_trading": True, "error": str(e)}
    
    async def run_multi_asset_trading(self):
        """Run multi-asset trading logic"""
        try:
            # Execute multi-asset strategy
            self.multi_asset_agent.execute_multi_asset_strategy()
            
            # Update metrics
            self.system_metrics["agents_active"] = 1
            
        except Exception as e:
            self.logger.error(f"Error in multi-asset trading: {str(e)}")
    
    async def run_learning_cycle(self):
        """Run continuous learning cycle"""
        try:
            # Collect market data for learning
            market_data = {
                "timestamp": datetime.now().isoformat(),
                "brokers_status": self.broker_manager.get_system_status(),
                "performance": self.system_metrics
            }
            
            # Add experience to learner
            self.continuous_learner.add_experience(
                market_data=market_data,
                action="system_cycle",
                outcome=1.0,  # Placeholder - would use actual performance
                metadata={"cycle_type": "automated"}
            )
            
            # Update learning metrics
            self.system_metrics["learning_cycles"] = self.continuous_learner.learning_metrics["learning_cycles"]
            
        except Exception as e:
            self.logger.error(f"Error in learning cycle: {str(e)}")
    
    async def perform_health_check(self):
        """Perform comprehensive system health check"""
        try:
            health_status = {
                "timestamp": datetime.now().isoformat(),
                "system_status": "healthy",
                "components": {}
            }
            
            # Check broker health
            broker_health = self.broker_manager.health_check()
            health_status["components"]["brokers"] = broker_health
            
            # Check system monitor health
            if self.system_monitor:
                monitor_status = self.system_monitor.get_current_status()
                health_status["components"]["system_monitor"] = monitor_status
            
            # Check agents health
            agents_health = {
                "multi_asset": self.multi_asset_agent is not None,
                "risk_management": self.risk_agent is not None,
                "continuous_learner": self.continuous_learner is not None
            }
            health_status["components"]["agents"] = agents_health
            
            # Determine overall health
            if broker_health["overall_health"] != "healthy":
                health_status["system_status"] = "degraded"
            
            self.logger.info(f"Health check completed: {health_status['system_status']}")
            
        except Exception as e:
            self.logger.error(f"Error in health check: {str(e)}")
    
    def update_system_metrics(self):
        """Update system performance metrics"""
        if self.start_time:
            uptime = (datetime.now() - self.start_time).total_seconds() / 3600
            self.system_metrics["uptime_hours"] = uptime
    
    async def shutdown_system(self):
        """Gracefully shutdown the trading system"""
        cprint("🛑 Shutting down Advanced AI Trading System...", "yellow")
        
        try:
            self.is_running = False
            
            # Stop system monitoring
            if self.system_monitor:
                self.system_monitor.stop_monitoring()
                cprint("📊 System monitoring stopped", "yellow")
            
            # Disconnect from brokers
            self.broker_manager.disconnect_all_brokers()
            cprint("🔌 Disconnected from all brokers", "yellow")
            
            # Save learning state
            if self.continuous_learner:
                self.continuous_learner.save_model_state()
                cprint("🧠 Learning state saved", "yellow")
            
            # Final metrics report
            total_uptime = self.system_metrics["uptime_hours"]
            cprint(f"📈 System ran for {total_uptime:.2f} hours", "cyan")
            cprint(f"📊 {self.system_metrics['learning_cycles']} learning cycles completed", "cyan")
            
            cprint("✅ System shutdown completed gracefully", "green")
            
        except Exception as e:
            cprint(f"❌ Error during shutdown: {str(e)}", "red")
            self.logger.error(f"Shutdown error: {str(e)}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            "timestamp": datetime.now().isoformat(),
            "system_info": {
                "name": self.config["system"]["name"],
                "version": self.config["system"]["version"],
                "environment": self.config["system"]["environment"],
                "is_running": self.is_running,
                "start_time": self.start_time.isoformat() if self.start_time else None
            },
            "metrics": self.system_metrics,
            "components": {
                "broker_manager": self.broker_manager is not None,
                "multi_asset_agent": self.multi_asset_agent is not None,
                "risk_agent": self.risk_agent is not None,
                "continuous_learner": self.continuous_learner is not None,
                "quantitative_analyzer": self.quantitative_analyzer is not None,
                "system_monitor": self.system_monitor is not None
            }
        }

async def main():
    """Main entry point"""
    try:
        # Display startup banner
        cprint("=" * 80, "blue")
        cprint("🌙 MOON DEV'S ADVANCED AI TRADING SYSTEM", "white", "on_blue")
        cprint("    Self-Improving Multi-Asset Trading Platform", "white", "on_blue")
        cprint("=" * 80, "blue")
        print()
        
        # Initialize and start system
        trading_system = AdvancedTradingSystem()
        
        try:
            await trading_system.start_system()
        except KeyboardInterrupt:
            cprint("\n🛑 Shutdown requested by user", "yellow")
        finally:
            await trading_system.shutdown_system()
    
    except Exception as e:
        cprint(f"❌ Fatal error: {str(e)}", "red")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())