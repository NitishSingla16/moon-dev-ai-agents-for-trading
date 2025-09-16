# 🌙 Moon Dev's Advanced AI Trading System

A comprehensive self-improving AI trading system with multi-asset support, advanced risk management, and continuous learning capabilities.

## 🚀 Features

### Core Trading Features
- **Multi-Asset Support**: Trade Forex, Crypto, Stocks, Options, and Futures
- **Advanced AI Agents**: Technical analysis, fundamental analysis, sentiment analysis, risk management
- **Multi-Broker Integration**: Binance, OANDA, Alpaca, Interactive Brokers
- **Sophisticated Risk Management**: Dynamic position sizing, correlation analysis, drawdown protection
- **Extensible Strategy Framework**: Pluggable trading strategies with performance tracking

### Self-Improvement Capabilities
- **Continuous Learning**: System learns from market data and trading performance
- **Auto-Updates**: Automatically updates strategies and parameters based on performance
- **Technology Monitoring**: Scans for new trading technologies and integrations
- **Performance Analytics**: Advanced metrics and self-optimization

### Advanced Analytics
- **Scientific Calculations**: NumPy/SciPy integration for advanced mathematics (optional)
- **Quantitative Analysis**: Statistical models, Monte Carlo simulations
- **Risk Metrics**: VaR, CVaR, Sharpe ratio, Sortino ratio, maximum drawdown
- **Mathematical Modeling**: Black-Scholes, Greeks calculations, portfolio optimization

### Infrastructure
- **Real-time Monitoring**: Comprehensive system health and performance monitoring
- **Scalable Architecture**: Modular microservices design
- **Security**: Encrypted credentials and secure API handling
- **Production Ready**: Comprehensive error handling, logging, and alerting

## 📁 Project Structure

```
trading_system/
├── core/
│   ├── agents/           # AI trading agents
│   │   ├── multi_asset_agent.py
│   │   ├── risk_management_agent.py
│   │   ├── technical_analysis_agent.py
│   │   └── advanced_base_agent.py
│   ├── brokers/         # Broker integrations
│   │   ├── broker_manager.py
│   │   ├── binance_broker.py
│   │   ├── oanda_broker.py
│   │   ├── alpaca_broker.py
│   │   └── interactive_brokers.py
│   ├── strategies/      # Trading strategies
│   └── risk/            # Risk management
├── intelligence/
│   ├── learning/        # Self-improvement algorithms
│   │   ├── continuous_learner.py
│   │   ├── strategy_optimizer.py
│   │   └── performance_analyzer.py
│   ├── analytics/       # Quantitative analysis
│   │   ├── quantitative_analyzer.py
│   │   ├── monte_carlo_simulator.py
│   │   └── mathematical_models.py
│   └── data_sources/    # Data source integrations
├── infrastructure/
│   ├── monitoring/      # System monitoring
│   │   ├── system_monitor.py
│   │   ├── performance_tracker.py
│   │   └── alert_manager.py
│   ├── deployment/      # Deployment configs
│   └── security/        # Security utilities
└── tests/              # Test suites
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NitishSingla16/moon-dev-ai-agents-for-trading.git
   cd moon-dev-ai-agents-for-trading
   ```

2. **Install dependencies** (optional for advanced features):
   ```bash
   pip install numpy scipy pandas psutil
   ```
   
   Note: The system works without these dependencies using built-in fallbacks.

3. **Set up environment variables**:
   ```bash
   cp '.env example' .env
   # Edit .env with your API keys
   ```

## 🚀 Quick Start

### Running Tests
```bash
python trading_system/test_system.py
```

### Running Demo
```bash
python trading_system/demo.py
```

### Running the Full System
```bash
python trading_system/main.py
```

## 🎯 Usage Examples

### Multi-Asset Trading
```python
from trading_system.core.agents import MultiAssetAgent

# Create multi-asset agent
agent = MultiAssetAgent()

# Get tradeable assets across all supported exchanges
tradeable = agent.get_tradeable_assets()
print(f"Total tradeable assets: {sum(len(assets) for assets in tradeable.values())}")

# Execute trading strategy
agent.execute_multi_asset_strategy()
```

### Risk Management
```python
from trading_system.core.agents import RiskManagementAgent

# Create risk management agent
risk_agent = RiskManagementAgent()

# Calculate position size with risk management
position_size = risk_agent.calculate_position_size(
    asset="BTC", 
    signal_strength=0.8, 
    volatility=0.03, 
    account_balance=10000
)

# Run Monte Carlo risk simulation
positions = {"BTC": 0.4, "ETH": 0.3, "SOL": 0.2}
risk_metrics = risk_agent.monte_carlo_risk_simulation(positions)
print(f"Portfolio VaR 95%: {risk_metrics['var_95']:.4f}")
```

### Continuous Learning
```python
from trading_system.intelligence.learning import ContinuousLearner

# Create learning system
learner = ContinuousLearner()

# Add trading experience
learner.add_experience(
    market_data={"price": 50000, "volume": 1000, "volatility": 0.02},
    action="BUY",
    outcome=1.5,  # Positive outcome
    metadata={"strategy": "momentum"}
)

# Get strategy recommendation
recommendation = learner.get_strategy_recommendation(market_data)
print(f"Recommended strategy: {recommendation['recommended_strategy']}")
```

### Broker Integration
```python
from trading_system.core.brokers import BrokerManager

# Configure brokers
config = {
    "brokers": {
        "binance": {
            "enabled": True,
            "api_key": "your_api_key",
            "api_secret": "your_api_secret",
            "sandbox": True
        }
    }
}

# Create broker manager
broker_manager = BrokerManager(config)

# Connect to brokers
broker_manager.connect_all_brokers()

# Place order
result = broker_manager.place_order(
    symbol="BTCUSDT",
    order_type="market",
    side="buy",
    quantity=0.001
)
```

### System Monitoring
```python
from trading_system.infrastructure.monitoring import SystemMonitor

# Create system monitor
monitor = SystemMonitor()

# Start monitoring
monitor.start_monitoring()

# Get system status
status = monitor.get_current_status()
print(f"CPU Usage: {status['system_metrics']['cpu']['percent']:.1f}%")
print(f"Memory Usage: {status['system_metrics']['memory']['percent']:.1f}%")
```

## 🔧 Configuration

The system uses a comprehensive configuration system. Key configuration areas:

### Broker Configuration
```python
broker_config = {
    "brokers": {
        "binance": {
            "enabled": True,
            "api_key": "your_key",
            "api_secret": "your_secret",
            "sandbox": True
        },
        "oanda": {
            "enabled": False,
            "api_key": "your_key",
            "account_id": "your_account",
            "environment": "practice"
        }
    }
}
```

### Risk Management Configuration
```python
risk_config = {
    "max_portfolio_risk": 0.02,      # 2% max portfolio risk
    "max_position_risk": 0.005,      # 0.5% max risk per position
    "max_correlation": 0.7,          # Max correlation between positions
    "max_drawdown": 0.15,            # 15% max drawdown
    "var_confidence": 0.95           # VaR confidence level
}
```

### Learning Configuration
```python
learning_config = {
    "learning_rate": 0.01,
    "memory_size": 10000,
    "batch_size": 100,
    "update_frequency": 100
}
```

## 🧪 Testing

The system includes comprehensive testing:

```bash
# Run all tests
python trading_system/test_system.py

# Run specific test categories
python -c "
from trading_system.test_system import *
test_basic_functionality()
test_integration()
test_error_handling()
"
```

## 📊 Monitoring and Alerts

The system provides comprehensive monitoring:

- **System Health**: CPU, memory, disk usage
- **Trading Performance**: Win rate, PnL, Sharpe ratio
- **Risk Metrics**: VaR, drawdown, correlation
- **Alert System**: Real-time notifications for critical events

## 🔒 Security

- **API Key Encryption**: Secure storage of broker credentials
- **Environment Variables**: Sensitive data stored in environment
- **Input Validation**: Comprehensive validation of all inputs
- **Error Handling**: Graceful handling of all error conditions

## 🚨 Important Disclaimers

**⚠️ This is experimental trading software. Use at your own risk.**

- No guarantees of profitability
- Trading involves substantial risk of loss
- Past performance does not indicate future results
- Always test thoroughly before live trading
- Never risk more than you can afford to lose

## 🤝 Contributing

This system builds upon Moon Dev's existing infrastructure. Contributions should:

1. Maintain compatibility with existing systems
2. Follow the established coding patterns
3. Include comprehensive tests
4. Provide proper documentation

## 📄 License

This project follows Moon Dev's licensing terms. See the main repository for details.

## 🔗 Links

- **Moon Dev**: [moondev.com](https://moondev.com)
- **Algo Trading Education**: [algotradecamp.com](https://algotradecamp.com)
- **YouTube Updates**: [Trading System Playlist](https://www.youtube.com/playlist?list=PLXrNVMjRZUJg4M4uz52iGd1LhXXGVbIFz)

---

**Built with ❤️ by Moon Dev - Pioneering the future of AI-powered trading**