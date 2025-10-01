# 🌙 Moon Dev's AI Agents for Trading - Complete Repository Structure

**Generated:** 2025-01-27  
**Purpose:** Comprehensive documentation of all files and folders in the repository

---

## 📂 Repository Overview

This repository contains Moon Dev's AI Agents for Trading - an experimental project exploring AI-powered trading systems using various agents for different trading tasks.

### Quick Stats
- **Total Python Files:** ~50+ files
- **Total Agents:** 17 specialized agents
- **Total Directories:** ~20+ (including subdirectories)
- **Lines of Code:** Estimated 15,000+ lines
- **Data Files:** 40+ (CSV, TXT, JSON formats)

---

## 🗂️ Root Level Structure

### Root Files

| File | Size | Description |
|------|------|-------------|
| `README.md` | 11,391 bytes | Main project documentation with overview, setup instructions, and roadmap |
| `requirements.txt` | 333 bytes | Python package dependencies (FastAPI, Anthropic, OpenAI, pandas, etc.) |
| `moondev.png` | 342,439 bytes | Project logo/branding image |
| `.env example` | 1,147 bytes | Template for environment variables (API keys) |
| `.gitignore` | 1,736 bytes | Git ignore rules for secrets, data, temp files |

### Root Directories

```
moon-dev-ai-agents-for-trading/
├── src/           # Main source code directory
├── data/          # Project-level data files
├── docs/          # Documentation
├── .git/          # Git repository data
```

---

## 📁 src/ - Source Code Directory

The main application code organized into modules.

### src/ Core Files

| File | Size | Description |
|------|------|-------------|
| `__init__.py` | 39 bytes | Package initialization |
| `config.py` | 4,439 bytes | Global configuration settings (API keys, trading parameters) |
| `main.py` | 3,992 bytes | Main application entry point |
| `ezbot.py` | 9,130 bytes | Easy bot interface for quick trading operations |
| `nice_funcs.py` | 43,810 bytes | Large utility library with trading functions (Birdeye API, data processing) |
| `nice_funcs_hl.py` | 14,253 bytes | HyperLiquid-specific utility functions |

---

## 🤖 src/agents/ - AI Agent Implementations

Contains all specialized AI trading agents. Each agent handles a specific trading task or analysis.

### Agent Files Overview

| Agent File | Size | Purpose |
|------------|------|---------|
| `__init__.py` | 0 bytes | Package initialization |
| `README.md` | 2,138 bytes | Agents documentation |
| `base_agent.py` | 523 bytes | Base class for all agents with common functionality |
| `api.py` | 10,117 bytes | Moon Dev API handler for market data access |
| `trading_agent.py` | 19,298 bytes | Basic LLM-based trading decisions |
| `strategy_agent.py` | 11,422 bytes | Manages and executes trading strategies |
| `risk_agent.py` | 26,755 bytes | Portfolio risk management and PnL monitoring |
| `copybot_agent.py` | 13,216 bytes | Copy trading monitoring and analysis |
| `whale_agent.py` | 23,294 bytes | Whale activity tracking and alerts |
| `sentiment_agent.py` | 21,755 bytes | Twitter sentiment analysis with voice alerts |
| `listingarb_agent.py` | 28,640 bytes | Pre-exchange token identification on CoinGecko |
| `focus_agent.py` | 14,551 bytes | Productivity monitoring with audio sampling |
| `funding_agent.py` | 21,742 bytes | Funding rate monitoring across exchanges |
| `liquidation_agent.py` | 27,794 bytes | Liquidation event tracking and analysis |
| `chartanalysis_agent.py` | 17,477 bytes | Chart pattern analysis with AI |
| `fundingarb_agent.py` | 14,026 bytes | Cross-exchange funding arbitrage opportunities |
| `rbi_agent.py` | 23,890 bytes | Research-Backtest-Implement automation with DeepSeek |
| `coingecko_agent.py` | 25,940 bytes | CoinGecko data integration and analysis |

### Agent Descriptions

#### Core Trading Agents
1. **Trading Agent** (`trading_agent.py`)
   - Basic LLM-powered trading decisions
   - Token data analysis
   - Entry/exit signal generation

2. **Strategy Agent** (`strategy_agent.py`)
   - Executes custom trading strategies
   - Validates strategy signals with AI
   - Manages strategy lifecycle

3. **Risk Agent** (`risk_agent.py`)
   - Real-time risk monitoring
   - PnL limit enforcement
   - Position size management
   - AI-powered risk assessment
   - Daily balance logging

#### Market Intelligence Agents
4. **CopyBot Agent** (`copybot_agent.py`)
   - Monitors copy trading activity
   - Portfolio position analysis
   - Trade opportunity identification

5. **Whale Agent** (`whale_agent.py`)
   - Large holder activity tracking
   - Whale wallet monitoring
   - Alert system for significant moves

6. **Sentiment Agent** (`sentiment_agent.py`)
   - Twitter sentiment analysis
   - Real-time sentiment tracking
   - Voice announcements for shifts
   - Historical sentiment data

7. **Listing Arbitrage Agent** (`listingarb_agent.py`)
   - Identifies pre-listing opportunities
   - CoinGecko token screening
   - Parallel AI analysis (technical + fundamental)
   - Market cap and volume filtering

#### Market Data Agents
8. **Funding Agent** (`funding_agent.py`)
   - Multi-exchange funding rate monitoring
   - Extreme funding alerts
   - AI-powered opportunity analysis
   - Voice announcements

9. **Liquidation Agent** (`liquidation_agent.py`)
   - Tracks liquidation events
   - Configurable time windows (15min/1hr/4hr)
   - Liquidation spike detection
   - AI analysis and alerts

10. **Chart Analysis Agent** (`chartanalysis_agent.py`)
    - Visual chart pattern recognition
    - AI-powered technical analysis
    - Buy/Sell/Nothing recommendations

11. **Funding Arbitrage Agent** (`fundingarb_agent.py`)
    - Cross-platform arbitrage detection
    - HyperLiquid vs Solana comparison
    - Real-time opportunity alerts

#### Specialized Agents
12. **RBI Agent** (`rbi_agent.py`)
    - Research phase: Strategy analysis from videos/PDFs
    - Backtest phase: Automated backtest code generation
    - Implement phase: Strategy debugging and finalization
    - Uses DeepSeek for research and code generation

13. **CoinGecko Agent** (`coingecko_agent.py`)
    - Comprehensive CoinGecko data access
    - Multi-agent conversation system
    - Token discovery and analysis

14. **Focus Agent** (`focus_agent.py`)
    - Productivity monitoring
    - Audio sampling during work
    - Focus score tracking
    - Voice alerts for low focus

15. **API Handler** (`api.py`)
    - Moon Dev API integration
    - Historical data access
    - Liquidation data endpoints
    - Funding rate data
    - Open interest tracking
    - CopyBot data access

16. **Base Agent** (`base_agent.py`)
    - Common functionality for all agents
    - Shared utilities and methods
    - Agent interface definition

---

## 📊 src/data/ - Data Storage

Application data including CSV files, historical data, and agent outputs.

### Data Files

| File | Size | Description |
|------|------|-------------|
| `__init__.py` | 0 bytes | Package initialization |
| `ohlcv_collector.py` | 2,359 bytes | OHLCV data collection script |
| `agent_discussed_tokens.csv` | 859 bytes | Tokens analyzed by agents |
| `ai_analysis_buys.csv` | 11,847 bytes | AI buy recommendations log |
| `current_allocation.csv` | 255 bytes | Current portfolio positions |
| `funding_history.csv` | 356 bytes | Historical funding rate data |
| `funding_history_backup.csv` | 336 bytes | Backup funding data |
| `liquidation_history.csv` | 2,364 bytes | Liquidation event history |
| `oi_history.csv` | 5,523 bytes | Open interest historical data |
| `portfolio_balance.csv` | 336 bytes | Portfolio balance over time |
| `sentiment_history.csv` | 134 bytes | Historical sentiment scores |

### Data Subdirectories

#### src/data/charts/
- Empty directory for storing generated chart visualizations
- Used by agents to save HTML chart outputs

#### src/data/rbi/ - RBI Agent Working Directory

Complete workspace for the Research-Backtest-Implement agent.

| Item | Type | Description |
|------|------|-------------|
| `BTC-USD-15m.csv` | File (2.3 MB) | Bitcoin 15-minute OHLCV data for backtesting |
| `ideas.txt` | File (262 bytes) | Trading ideas input (YouTube URLs, PDFs, text) |
| `backtests/` | Directory | Initial backtest code outputs |
| `backtests_package/` | Directory | Package-verified backtest code |
| `backtests_final/` | Directory | Final debugged backtest code |
| `research/` | Directory | Strategy research outputs (30+ files) |
| `run_0125_1142/` | Directory | Historical run data |

##### RBI Backtests Structure

**backtests/** - Initial Phase
- `VengeanceTrender_BT.py` - Initial backtest
- `VengeanceTrend_BT.py` - Initial backtest
- `EMAVolumeSync_BT.py` - Initial backtest
- `MomentumRejection_BT.py` - Initial backtest

**backtests_package/** - Package Check Phase
- `MomentumRejection_PKG.py` - Package-verified code
- `EMAVolumeSync_PKG.py` - Package-verified code
- `VengeanceTrend_PKG.py` - Package-verified code

**backtests_final/** - Final Phase
- `VengeanceTrend_BTFinal.py` - Production-ready backtest
- `MomentumRejection_BTFinal.py` - Production-ready backtest
- `EMAVolumeSync_BTFinal.py` - Production-ready backtest

**research/** - Strategy Research (30+ files)
Sample strategies researched:
- `DualEMAMomentum1141_strategy_0125_1141.txt`
- `TrendFollower_strategy_0125_1109.txt`
- `AdaptiveTrendline1124_strategy_0125_1124.txt`
- `VengeanceTrend_strategy_0125_1130.txt`
- `EMAVolumeSync_strategy.txt`
- `AdaptiveTrendline_strategy_0125_1116.txt`
- `TrendPulse_strategy_0125_1039.txt`
- `EMAWaveRider_strategy.txt`
- `DynamicTrendSync_strategy_0125_1126.txt`
- And 20+ more strategy research files

---

## 🌐 src/frontend/ - Web Interface

FastAPI-based web application for the RBI Agent.

### Frontend Structure

```
src/frontend/
├── main.py              # FastAPI application (7,019 bytes)
├── static/              # Static assets
│   ├── css/
│   │   └── styles.css   # Application styling
│   ├── js/
│   │   └── main.js      # Frontend JavaScript
│   └── images/
│       └── moondev.png  # Logo
└── templates/
    └── index.html       # Main UI template (7,402 bytes)
```

### Frontend Features
- Strategy analysis interface
- Real-time processing status
- File download functionality
- Research and backtest result display
- Background task processing

---

## 🔧 src/scripts/ - Utility Scripts

Standalone utility scripts for specific tasks.

| Script | Size | Purpose |
|--------|------|---------|
| `coingecko_exchangeless_tokens.py` | 10,047 bytes | Find tokens not on major exchanges |
| `deepseek_backtest.py` | 2,771 bytes | DeepSeek-powered backtesting |
| `fundingarb_calc.py` | 6,603 bytes | Funding arbitrage calculations |
| `openlinks_intabs.py` | 3,699 bytes | Browser automation for opening links |
| `token_list_tool.py` | 3,230 bytes | Token list management utilities |
| `twitter_login.py` | 3,820 bytes | Twitter authentication helper |

---

## 📈 src/strategies/ - Trading Strategies

Strategy implementation framework with base classes and examples.

### Strategy Files

```
src/strategies/
├── __init__.py              # Package init (197 bytes)
├── README.md                # Strategy documentation (1,656 bytes)
├── base_strategy.py         # Base strategy class (661 bytes)
├── example_strategy.py      # Example implementation (2,796 bytes)
└── custom/                  # User custom strategies
    ├── __init__.py          # Package init (239 bytes)
    ├── README.md            # Custom strategy docs (2,375 bytes)
    └── example_strategy.py  # Custom example (638 bytes)
```

### Strategy System Features
- Base class for consistent interface
- Custom strategy support
- Example implementations
- Integration with Strategy Agent
- Position sizing and risk management
- Signal generation framework

### Private Strategies (Ignored)
The following patterns are excluded via `.gitignore`:
- `private_*.py` - Private strategies
- `secret_*.py` - Secret strategies
- `dev_*.py` - Development strategies

---

## 📚 docs/ - Documentation

Project documentation and examples.

### Documentation Files

```
docs/
├── README.md                 # Documentation index (722 bytes)
├── api.md                    # API documentation (3,683 bytes)
├── REPOSITORY_STRUCTURE.md   # This file
└── examples/
    └── examplespan.md        # Example documentation (367 bytes)
```

### Documentation Coverage
- API endpoint reference
- Setup and configuration guides
- Example usage patterns
- Agent descriptions
- Environment variable reference

---

## 📦 data/ - Root Data Directory

Project-level data files (separate from src/data/).

| File | Size | Description |
|------|------|-------------|
| `all_titles.txt` | 2,362 bytes | Collection of titles |
| `notion_roadmap.html` | 55,231 bytes | Exported Notion roadmap |
| `section_titles.txt` | 489 bytes | Section title collection |
| `urls.txt` | 478 bytes | URL collection |
| `youtube_urls.txt` | 32 bytes | YouTube video URLs |

---

## 🔐 Configuration & Environment

### Environment Variables Required

From `.env example`:
```bash
# Core API Keys
ANTHROPIC_KEY=your_key_here
DEEPSEEK_KEY=your_key_here
BIRDEYE_API_KEY=your_key_here

# Optional
MOONDEV_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Trading Configuration
WALLET_ADDRESS=your_wallet
PRIVATE_KEY=your_key
```

### Configuration Files
- `.env` - Environment variables (not tracked)
- `config.py` - Python configuration
- `.gitignore` - Git exclusion rules
- `requirements.txt` - Python dependencies

---

## 📊 File Statistics

### By File Type

| Type | Count | Total Size |
|------|-------|------------|
| Python (`.py`) | 50+ | ~400 KB |
| Markdown (`.md`) | 8 | ~25 KB |
| CSV (`.csv`) | 10+ | ~23 KB + 2.3 MB BTC data |
| Text (`.txt`) | 35+ | ~50 KB |
| HTML | 3 | ~68 KB |
| JavaScript | 1 | ~5 KB |
| CSS | 1 | ~8 KB |
| Images | 2 | ~350 KB |

### Largest Files
1. `BTC-USD-15m.csv` - 2,285,825 bytes (2.3 MB)
2. `moondev.png` - 342,439 bytes (334 KB)
3. `data/notion_roadmap.html` - 55,231 bytes (54 KB)
4. `src/nice_funcs.py` - 43,810 bytes (43 KB)
5. `src/agents/listingarb_agent.py` - 28,640 bytes (28 KB)

### Code Complexity
- Most complex agents: Risk Agent, Liquidation Agent, Listing Arb Agent
- Largest utility library: `nice_funcs.py` (43 KB)
- Total estimated lines of Python code: 15,000+
- Number of AI prompts: 50+ across all agents

---

## 🔄 Git Ignore Rules

### Ignored Patterns

**Secrets & Credentials:**
- `.env`
- `**/dontshare.py`
- `secrets.json`
- `config.private.py`
- `cookies.json`

**Python Artifacts:**
- `__pycache__/`
- `*.pyc`, `*.pyo`
- `*.egg-info/`
- Virtual environments

**Data & Temporary:**
- `temp_data/`
- `ohlcv_data/`
- `trading_history/`
- `src/agents/api_data`
- `src/data/agent_memory`
- `src/data/private_data`
- `src/data/sentiment`
- `src/audio`

**Private Strategies:**
- `src/strategies/custom/private_*.py`
- `src/strategies/custom/secret_*.py`
- `src/strategies/custom/dev_*.py`

**Frontend:**
- `src/frontend/` (currently excluded)

**Development:**
- `.idea/`, `.vscode/`
- `*.log`
- `.DS_Store`

---

## 🚀 Entry Points & Usage

### Main Applications

1. **Main Trading Application**
   ```bash
   python src/main.py
   ```
   Runs the main trading system with all enabled agents

2. **Web Interface**
   ```bash
   python -m uvicorn src.frontend.main:app --reload
   ```
   Starts the FastAPI web interface

3. **Easy Bot**
   ```bash
   python src/ezbot.py
   ```
   Quick trading interface

4. **Individual Agents**
   ```bash
   python src/agents/risk_agent.py
   python src/agents/rbi_agent.py
   # etc.
   ```
   Run specific agents standalone

### Utility Scripts
```bash
python src/scripts/deepseek_backtest.py
python src/scripts/coingecko_exchangeless_tokens.py
# etc.
```

---

## 🏗️ Architecture Overview

### System Design

```
┌─────────────────────────────────────────────┐
│           Main Application (main.py)         │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │        Strategy Agent                │  │
│  │  - Validates strategy signals        │  │
│  │  - Executes approved trades          │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │         Risk Agent                   │  │
│  │  - Monitors PnL limits              │  │
│  │  - Enforces position sizes          │  │
│  │  - Tracks daily balance             │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │    Market Intelligence Agents        │  │
│  │  - Whale Agent                       │  │
│  │  - Sentiment Agent                   │  │
│  │  - Funding Agent                     │  │
│  │  - Liquidation Agent                 │  │
│  │  - Chart Analysis Agent              │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │      Specialized Agents              │  │
│  │  - RBI Agent                         │  │
│  │  - Listing Arb Agent                 │  │
│  │  - Funding Arb Agent                 │  │
│  │  - CopyBot Agent                     │  │
│  │  - Focus Agent                       │  │
│  └──────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
    ┌────▼────┐            ┌────▼────┐
    │  Data   │            │   API   │
    │ Storage │            │ Clients │
    └─────────┘            └─────────┘
```

### Data Flow

1. **Market Data Collection**
   - Birdeye API (token data)
   - Moon Dev API (liquidations, funding, OI)
   - CoinGecko API (token listings)
   - Twitter API (sentiment)

2. **Agent Processing**
   - Each agent analyzes specific data
   - Agents use LLMs (Claude, DeepSeek) for decisions
   - Results stored in CSV files

3. **Strategy Execution**
   - Strategy Agent validates signals
   - Risk Agent checks limits
   - Trades executed via trading functions

4. **Monitoring & Logging**
   - Real-time data updates
   - Historical data tracking
   - Voice announcements for alerts

---

## 📈 Dependencies

From `requirements.txt` (key packages):
- `fastapi` - Web framework
- `anthropic` - Claude API
- `openai` - OpenAI/DeepSeek API
- `pandas` - Data manipulation
- `requests` - HTTP client
- `termcolor` - Terminal colors
- `python-dotenv` - Environment variables
- Additional trading and utility libraries

---

## 🎯 Key Features

### Agent Capabilities
- ✅ Real-time market monitoring
- ✅ AI-powered decision making
- ✅ Risk management and PnL tracking
- ✅ Sentiment analysis with voice alerts
- ✅ Automated strategy research and backtesting
- ✅ Cross-exchange arbitrage detection
- ✅ Whale and liquidation tracking
- ✅ Portfolio optimization

### Data Management
- ✅ Historical data collection
- ✅ CSV-based storage
- ✅ Chart generation
- ✅ Real-time updates
- ✅ Data backup systems

### Development Features
- ✅ Modular architecture
- ✅ Base classes for extension
- ✅ Custom strategy support
- ✅ Environment-based configuration
- ✅ Comprehensive logging

---

## 🔮 Future Development Areas

Based on README roadmap:
- [ ] Portfolio optimization
- [ ] Advanced risk management
- [ ] Machine learning integration
- [ ] Backtesting framework improvements
- [ ] Performance analytics dashboard
- [ ] Additional agent types
- [ ] Enhanced web interface

---

## ⚠️ Important Notes

### Security
- **Never commit** `.env` files
- **Keep private** strategy implementations
- **Protect** API keys and wallet credentials
- **Exclude** sensitive data from version control

### Testing
- This is an **experimental** project
- **No guarantees** of profitability
- **Test thoroughly** before live trading
- **Start small** with real money
- **Monitor closely** all agent actions

### Disclaimers
- Not financial advice
- Substantial risk of loss
- Educational purposes only
- No profit guarantees
- DYOR (Do Your Own Research)

---

## 📞 Support & Community

- **Discord:** [moondev.com](http://moondev.com)
- **YouTube Updates:** [Playlist](https://www.youtube.com/playlist?list=PLXrNVMjRZUJg4M4uz52iGd1LhXXGVbIFz)
- **Education:** [algotradecamp.com](https://algotradecamp.com)
- **Business:** moon@algotradecamp.com

---

## 📝 Maintenance Notes

### Regular Tasks
- Update CSV data files
- Monitor agent performance
- Review and update strategies
- Check API rate limits
- Backup important data

### Version Control
- Commit frequently
- Use descriptive messages
- Branch for new features
- Tag releases
- Document changes

---

**Last Updated:** 2025-01-27  
**Maintained by:** Moon Dev 🌙  
**Version:** 1.0

*Built with love for the trading community. Always remember: Trading involves substantial risk. Never invest more than you can afford to lose.*
