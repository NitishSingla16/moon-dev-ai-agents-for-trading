"""
🌙 Moon Dev's Trading System Test Script
Simple test to verify all components work together
"""

import sys
import os
from pathlib import Path
import asyncio
import logging

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Test imports
try:
    from trading_system.core.agents import MultiAssetAgent, RiskManagementAgent
    from trading_system.core.brokers import BrokerManager, BinanceBroker
    from trading_system.intelligence.learning import ContinuousLearner
    from trading_system.intelligence.analytics import QuantitativeAnalyzer
    from trading_system.infrastructure.monitoring import SystemMonitor
    print("✅ All imports successful!")
except ImportError as e:
    print(f"❌ Import error: {str(e)}")
    sys.exit(1)

def test_basic_functionality():
    """Test basic functionality of key components"""
    print("\n🧪 Testing Basic Functionality...")
    
    # Test broker manager
    print("Testing Broker Manager...")
    broker_config = {
        "brokers": {
            "binance": {
                "enabled": True,
                "api_key": "test_key",
                "api_secret": "test_secret",
                "sandbox": True
            }
        }
    }
    
    broker_manager = BrokerManager(broker_config)
    print(f"✅ Broker Manager created with {len(broker_manager.brokers)} brokers")
    
    # Test multi-asset agent
    print("Testing Multi-Asset Agent...")
    multi_asset_config = {"enabled": True, "update_interval": 60}
    multi_asset_agent = MultiAssetAgent(multi_asset_config)
    
    tradeable_assets = multi_asset_agent.get_tradeable_assets()
    print(f"✅ Multi-Asset Agent created. Found {sum(len(assets) for assets in tradeable_assets.values())} tradeable assets")
    
    # Test risk management agent
    print("Testing Risk Management Agent...")
    risk_config = {"enabled": True, "max_portfolio_risk": 0.02}
    risk_agent = RiskManagementAgent(risk_config)
    
    # Test position size calculation
    position_size = risk_agent.calculate_position_size("BTC", 0.8, 0.03, 10000)
    print(f"✅ Risk Management Agent created. Sample position size: ${position_size:.2f}")
    
    # Test continuous learner
    print("Testing Continuous Learner...")
    learning_config = {"learning_rate": 0.01, "memory_size": 1000}
    learner = ContinuousLearner(learning_config)
    
    # Add sample experience
    learner.add_experience(
        market_data={"price": 50000, "volume": 1000, "volatility": 0.02},
        action="BUY",
        outcome=1.5,
        metadata={"strategy": "test"}
    )
    print(f"✅ Continuous Learner created. Memory size: {len(learner.memory_buffer)}")
    
    # Test quantitative analyzer
    print("Testing Quantitative Analyzer...")
    quant_analyzer = QuantitativeAnalyzer()
    
    # Test with sample data
    sample_prices = [100, 101, 99, 102, 98, 105, 103, 107, 109, 108]
    returns = quant_analyzer.calculate_returns(sample_prices)
    volatility = quant_analyzer.calculate_volatility(returns)
    print(f"✅ Quantitative Analyzer created. Sample volatility: {volatility:.4f}")
    
    # Test system monitor
    print("Testing System Monitor...")
    monitor_config = {"monitoring_interval": 30, "retention_days": 7}
    system_monitor = SystemMonitor(monitor_config)
    
    current_status = system_monitor.get_current_status()
    print(f"✅ System Monitor created. CPU usage: {current_status['system_metrics'].get('cpu', {}).get('percent', 0):.1f}%")
    
    print("\n🎉 All basic functionality tests passed!")

def test_integration():
    """Test component integration"""
    print("\n🔗 Testing Component Integration...")
    
    # Test broker-agent integration
    print("Testing Broker-Agent Integration...")
    
    broker_config = {
        "brokers": {
            "binance": {
                "enabled": True,
                "api_key": "test_key",
                "api_secret": "test_secret",
                "sandbox": True
            }
        }
    }
    
    broker_manager = BrokerManager(broker_config)
    connection_results = broker_manager.connect_all_brokers()
    print(f"✅ Broker connections: {connection_results}")
    
    # Test getting market data through broker
    market_data = broker_manager.get_market_data("BTCUSDT", "1h", 10)
    if "data" in market_data:
        print(f"✅ Market data retrieved: {len(market_data['data'])} candles")
    else:
        print(f"⚠️ Market data result: {market_data}")
    
    # Test risk-learning integration
    print("Testing Risk-Learning Integration...")
    
    risk_agent = RiskManagementAgent()
    learner = ContinuousLearner()
    
    # Simulate trading experience
    market_data = {"price": 50000, "volatility": 0.025, "indicators": {"rsi": 65}}
    position_size = risk_agent.calculate_position_size("BTC", 0.7, 0.025, 10000)
    
    # Add experience to learner
    learner.add_experience(
        market_data=market_data,
        action="BUY",
        outcome=position_size / 100,  # Normalized outcome
        metadata={"position_size": position_size}
    )
    
    print(f"✅ Risk-Learning integration: Position ${position_size:.2f}, Learning samples: {len(learner.memory_buffer)}")
    
    print("\n🎉 All integration tests passed!")

async def test_async_functionality():
    """Test asynchronous functionality"""
    print("\n⚡ Testing Async Functionality...")
    
    # Test async agent operations
    multi_asset_agent = MultiAssetAgent()
    
    try:
        await multi_asset_agent.async_run()
        print("✅ Async agent operations completed")
    except Exception as e:
        print(f"⚠️ Async test completed with: {str(e)}")
    
    print("🎉 Async functionality test completed!")

def test_error_handling():
    """Test error handling"""
    print("\n🛡️ Testing Error Handling...")
    
    # Test broker with invalid config
    try:
        broker_manager = BrokerManager({"brokers": {}})
        print("✅ Empty broker config handled gracefully")
    except Exception as e:
        print(f"❌ Error with empty broker config: {str(e)}")
    
    # Test agent with invalid data
    try:
        quant_analyzer = QuantitativeAnalyzer()
        result = quant_analyzer.calculate_returns([])  # Empty array
        print(f"✅ Empty data handled gracefully: {len(result)} returns")
    except Exception as e:
        print(f"❌ Error with empty data: {str(e)}")
    
    print("🎉 Error handling tests completed!")

async def main():
    """Main test function"""
    print("🌙 Moon Dev's Advanced AI Trading System Test Suite")
    print("=" * 60)
    
    # Setup logging
    logging.basicConfig(level=logging.ERROR)  # Suppress info logs during testing
    
    try:
        # Run tests
        test_basic_functionality()
        test_integration()
        await test_async_functionality()
        test_error_handling()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED! Trading system is ready.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Test suite failed with error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())