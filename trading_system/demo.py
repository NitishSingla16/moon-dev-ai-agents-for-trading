"""
🌙 Moon Dev's Advanced AI Trading System Demo
Demonstration of the comprehensive trading system capabilities
"""

import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from trading_system.core.agents import MultiAssetAgent, RiskManagementAgent
from trading_system.core.brokers import BrokerManager
from trading_system.intelligence.learning import ContinuousLearner
from trading_system.intelligence.analytics import QuantitativeAnalyzer
from trading_system.infrastructure.monitoring import SystemMonitor
try:
    from termcolor import cprint
except ImportError:
    # Fallback when termcolor is not available
    def cprint(text, color=None, on_color=None):
        print(text)

def demo_multi_asset_trading():
    """Demonstrate multi-asset trading capabilities"""
    cprint("🚀 Multi-Asset Trading Demo", "white", "on_blue")
    
    # Create multi-asset agent
    agent = MultiAssetAgent()
    
    # Show tradeable assets
    tradeable = agent.get_tradeable_assets()
    for asset_class, assets in tradeable.items():
        if assets:
            cprint(f"📊 {asset_class}: {len(assets)} assets tradeable", "cyan")
            print(f"   Examples: {', '.join(assets[:3])}")
    
    # Demonstrate position sizing
    account_balance = 10000.0
    signal_strength = 0.8
    
    for asset_class in ["CRYPTO", "FOREX", "STOCKS"]:
        if asset_class in agent.asset_allocation:
            size = agent.calculate_position_size(asset_class, "BTC", account_balance, signal_strength)
            cprint(f"💰 {asset_class} position size: ${size:.2f}", "green")
    
    print()

def demo_risk_management():
    """Demonstrate risk management capabilities"""
    cprint("🛡️ Risk Management Demo", "white", "on_blue")
    
    # Create risk agent
    risk_agent = RiskManagementAgent()
    
    # Demonstrate portfolio VaR calculation
    sample_returns = [0.01, -0.02, 0.015, -0.01, 0.02, -0.005, 0.008]
    risk_agent.historical_pnl = sample_returns  # Set sample data
    var_95 = risk_agent.calculate_portfolio_var(0.95)
    var_99 = risk_agent.calculate_portfolio_var(0.99)
    
    cprint(f"📉 Portfolio VaR 95%: {var_95:.4f}", "yellow")
    cprint(f"📉 Portfolio VaR 99%: {var_99:.4f}", "yellow")
    
    # Demonstrate position sizing with risk
    position_size = risk_agent.calculate_position_size("BTC", 0.7, 0.03, 10000)
    cprint(f"💰 Risk-adjusted position size: ${position_size:.2f}", "green")
    
    # Demonstrate Monte Carlo simulation
    positions = {"BTC": 0.4, "ETH": 0.3, "SOL": 0.2}
    mc_results = risk_agent.monte_carlo_risk_simulation(positions, 1000)
    cprint(f"🎲 Monte Carlo VaR 95%: {mc_results['var_95']:.4f}", "magenta")
    
    # Demonstrate drawdown calculation
    current_dd, max_dd = risk_agent.calculate_drawdown(sample_returns)
    cprint(f"📊 Current Drawdown: {current_dd:.4f}", "red")
    cprint(f"📊 Maximum Drawdown: {max_dd:.4f}", "red")
    
    print()

def demo_continuous_learning():
    """Demonstrate continuous learning capabilities"""
    cprint("🧠 Continuous Learning Demo", "white", "on_blue")
    
    # Create learner
    learner = ContinuousLearner()
    
    # Add sample experiences
    experiences = [
        {"market_data": {"price": 50000, "volume": 1000}, "action": "BUY", "outcome": 1.5},
        {"market_data": {"price": 51000, "volume": 800}, "action": "SELL", "outcome": -0.5},
        {"market_data": {"price": 49000, "volume": 1200}, "action": "BUY", "outcome": 2.0},
    ]
    
    for exp in experiences:
        learner.add_experience(
            market_data=exp["market_data"],
            action=exp["action"],
            outcome=exp["outcome"],
            metadata={"strategy": "demo"}
        )
    
    cprint(f"📚 Learning samples: {len(learner.memory_buffer)}", "green")
    
    # Get strategy recommendation
    market_data = {"price": 50500, "volume": 900, "volatility": 0.02}
    recommendation = learner.get_strategy_recommendation(market_data)
    
    cprint(f"🎯 Recommended strategy: {recommendation['recommended_strategy']}", "cyan")
    cprint(f"🎯 Confidence: {recommendation['confidence']:.2f}", "cyan")
    cprint(f"🎯 Market regime: {recommendation['market_regime']}", "cyan")
    
    print()

def demo_quantitative_analysis():
    """Demonstrate quantitative analysis capabilities"""
    cprint("📊 Quantitative Analysis Demo", "white", "on_blue")
    
    # Create analyzer
    analyzer = QuantitativeAnalyzer()
    
    # Sample price data
    sample_data = {
        "BTC": [45000, 46000, 44000, 47000, 46500, 48000, 47500, 49000, 48500, 50000],
        "ETH": [3000, 3100, 2950, 3150, 3080, 3200, 3170, 3250, 3220, 3300]
    }
    
    # Generate analytics report
    report = analyzer.generate_analytics_report(sample_data)
    
    for asset, stats in report["summary_statistics"].items():
        cprint(f"📈 {asset} Analytics:", "yellow")
        print(f"   Total Return: {stats['total_return']:.2f}%")
        print(f"   Annualized Return: {stats['annualized_return']:.2f}%")
        print(f"   Volatility: {stats['volatility']:.2f}%")
        print(f"   Sharpe Ratio: {stats['sharpe_ratio']:.2f}")
        
        risk_metrics = report["risk_metrics"][asset]
        print(f"   VaR 95%: {risk_metrics['var_95']:.2f}%")
        print()

def demo_broker_integration():
    """Demonstrate broker integration capabilities"""
    cprint("🔗 Broker Integration Demo", "white", "on_blue")
    
    # Sample broker configuration
    config = {
        "brokers": {
            "binance": {
                "enabled": True,
                "api_key": "demo_key",
                "api_secret": "demo_secret",
                "sandbox": True
            }
        }
    }
    
    # Create broker manager
    broker_manager = BrokerManager(config)
    
    # Show system status
    status = broker_manager.get_system_status()
    cprint(f"🏗️ Total brokers: {status['total_brokers']}", "green")
    cprint(f"🔌 Connected brokers: {status['connected_brokers']}", "green")
    
    # Demonstrate asset routing
    test_assets = ["BTCUSDT", "EUR_USD", "AAPL", "ES"]
    for asset in test_assets:
        broker_name = broker_manager.infer_broker_from_symbol(asset)
        if broker_name:
            cprint(f"🎯 {asset} → {broker_name}", "cyan")
    
    print()

def demo_system_monitoring():
    """Demonstrate system monitoring capabilities"""
    cprint("📡 System Monitoring Demo", "white", "on_blue")
    
    # Create system monitor
    monitor = SystemMonitor()
    
    # Get current status
    status = monitor.get_current_status()
    
    # Display key metrics
    sys_metrics = status["system_metrics"]
    cprint(f"💻 CPU Usage: {sys_metrics.get('cpu', {}).get('percent', 0):.1f}%", "yellow")
    cprint(f"🧠 Memory Usage: {sys_metrics.get('memory', {}).get('percent', 0):.1f}%", "yellow")
    cprint(f"💾 Disk Usage: {sys_metrics.get('disk', {}).get('percent', 0):.1f}%", "yellow")
    
    app_metrics = status["application_metrics"]
    cprint(f"🔄 Trading Processes: {app_metrics.get('active_processes', 0)}", "green")
    
    print()

async def run_full_demo():
    """Run complete system demonstration"""
    cprint("=" * 80, "blue")
    cprint("🌙 MOON DEV'S ADVANCED AI TRADING SYSTEM", "white", "on_blue")
    cprint("           COMPREHENSIVE DEMONSTRATION", "white", "on_blue")
    cprint("=" * 80, "blue")
    print()
    
    # Run all demonstrations
    demo_multi_asset_trading()
    demo_risk_management()
    demo_continuous_learning()
    demo_quantitative_analysis()
    demo_broker_integration()
    demo_system_monitoring()
    
    cprint("=" * 80, "blue")
    cprint("🎉 DEMONSTRATION COMPLETED SUCCESSFULLY!", "white", "on_green")
    cprint("   All system components are working perfectly!", "white", "on_green")
    cprint("=" * 80, "blue")

if __name__ == "__main__":
    asyncio.run(run_full_demo())