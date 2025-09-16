"""
🌙 Moon Dev's Advanced AI Trading System
A comprehensive self-improving AI trading system with multi-asset support
"""

__version__ = "1.0.0"
__author__ = "Moon Dev"

# Import core modules
from .core import *
from .intelligence import *
from .infrastructure import *

# Trading system configuration
SUPPORTED_ASSETS = ["FOREX", "CRYPTO", "STOCKS", "OPTIONS", "FUTURES"]
SUPPORTED_BROKERS = ["BINANCE", "OANDA", "ALPACA", "INTERACTIVE_BROKERS"]

# System status
SYSTEM_STATUS = {
    "initialized": False,
    "agents_active": 0,
    "strategies_loaded": 0,
    "brokers_connected": 0,
    "last_update": None
}