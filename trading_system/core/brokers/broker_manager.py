"""
🌙 Moon Dev's Broker Manager
Manages multiple broker connections and routes orders to appropriate brokers
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
from .base_broker import BaseBroker
from .binance_broker import BinanceBroker
from .oanda_broker import OandaBroker
from .alpaca_broker import AlpacaBroker
from .interactive_brokers import InteractiveBrokersBroker

class BrokerManager:
    """
    Manages multiple broker connections and provides unified interface
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.brokers: Dict[str, BaseBroker] = {}
        self.asset_broker_mapping: Dict[str, str] = {}
        
        # Setup logging
        self.logger = logging.getLogger("broker_manager")
        
        # Initialize brokers based on configuration
        self.initialize_brokers()
        
        # Setup asset routing
        self.setup_asset_routing()
        
    def initialize_brokers(self):
        """Initialize all configured brokers"""
        broker_configs = self.config.get("brokers", {})
        
        for broker_name, broker_config in broker_configs.items():
            if not broker_config.get("enabled", False):
                continue
                
            try:
                broker = self.create_broker(broker_name, broker_config)
                if broker:
                    self.brokers[broker_name] = broker
                    self.logger.info(f"Initialized {broker_name} broker")
            except Exception as e:
                self.logger.error(f"Failed to initialize {broker_name} broker: {str(e)}")
    
    def create_broker(self, broker_name: str, config: Dict[str, Any]) -> Optional[BaseBroker]:
        """Create broker instance based on name"""
        broker_classes = {
            "binance": BinanceBroker,
            "oanda": OandaBroker,
            "alpaca": AlpacaBroker,
            "interactive_brokers": InteractiveBrokersBroker
        }
        
        broker_class = broker_classes.get(broker_name.lower())
        if not broker_class:
            self.logger.error(f"Unknown broker: {broker_name}")
            return None
            
        return broker_class(config)
    
    def setup_asset_routing(self):
        """Setup routing of assets to appropriate brokers"""
        # Default asset routing
        asset_routing = {
            # Crypto assets -> Binance
            "BTC": "binance", "ETH": "binance", "SOL": "binance", "ADA": "binance",
            "DOT": "binance", "LINK": "binance", "UNI": "binance", "AAVE": "binance",
            
            # Forex pairs -> OANDA
            "EUR_USD": "oanda", "GBP_USD": "oanda", "USD_JPY": "oanda", "USD_CHF": "oanda",
            "AUD_USD": "oanda", "USD_CAD": "oanda", "NZD_USD": "oanda", "GBP_JPY": "oanda",
            
            # US Stocks -> Alpaca
            "AAPL": "alpaca", "GOOGL": "alpaca", "MSFT": "alpaca", "TSLA": "alpaca",
            "AMZN": "alpaca", "META": "alpaca", "NVDA": "alpaca", "NFLX": "alpaca",
            
            # Options/Futures -> Interactive Brokers
            "ES": "interactive_brokers", "NQ": "interactive_brokers", "YM": "interactive_brokers",
            "RTY": "interactive_brokers", "CL": "interactive_brokers", "GC": "interactive_brokers"
        }
        
        # Override with configuration if provided
        configured_routing = self.config.get("asset_routing", {})
        asset_routing.update(configured_routing)
        
        self.asset_broker_mapping = asset_routing
    
    def connect_all_brokers(self) -> Dict[str, bool]:
        """Connect to all configured brokers"""
        connection_results = {}
        
        for broker_name, broker in self.brokers.items():
            try:
                success = broker.connect()
                if success:
                    success = broker.authenticate()
                connection_results[broker_name] = success
                
                if success:
                    self.logger.info(f"Successfully connected to {broker_name}")
                else:
                    self.logger.error(f"Failed to connect to {broker_name}")
                    
            except Exception as e:
                self.logger.error(f"Error connecting to {broker_name}: {str(e)}")
                connection_results[broker_name] = False
        
        return connection_results
    
    def disconnect_all_brokers(self):
        """Disconnect from all brokers"""
        for broker_name, broker in self.brokers.items():
            try:
                broker.disconnect()
                self.logger.info(f"Disconnected from {broker_name}")
            except Exception as e:
                self.logger.error(f"Error disconnecting from {broker_name}: {str(e)}")
    
    def get_broker_for_asset(self, symbol: str) -> Optional[BaseBroker]:
        """Get the appropriate broker for a given asset"""
        broker_name = self.asset_broker_mapping.get(symbol)
        
        if not broker_name:
            # Try to infer broker based on symbol format
            broker_name = self.infer_broker_from_symbol(symbol)
        
        if broker_name and broker_name in self.brokers:
            broker = self.brokers[broker_name]
            if broker.is_connected() and broker.is_authenticated():
                return broker
        
        return None
    
    def infer_broker_from_symbol(self, symbol: str) -> Optional[str]:
        """Infer appropriate broker based on symbol format"""
        symbol_upper = symbol.upper()
        
        # Crypto patterns
        if any(crypto in symbol_upper for crypto in ["BTC", "ETH", "SOL", "ADA", "DOT"]):
            return "binance"
        
        # Forex patterns
        if "_" in symbol and len(symbol.split("_")) == 2:
            parts = symbol.split("_")
            if all(len(part) == 3 for part in parts):
                return "oanda"
        
        # Stock patterns (3-5 letter symbols)
        if symbol.isalpha() and 2 <= len(symbol) <= 5:
            return "alpaca"
        
        # Futures patterns
        if symbol_upper in ["ES", "NQ", "YM", "RTY", "CL", "GC", "SI", "ZN"]:
            return "interactive_brokers"
        
        return None
    
    def place_order(self, symbol: str, order_type: str, side: str,
                   quantity: float, price: Optional[float] = None,
                   params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Place order through appropriate broker"""
        broker = self.get_broker_for_asset(symbol)
        
        if not broker:
            return {
                "error": f"No suitable broker found for asset: {symbol}",
                "timestamp": datetime.now().isoformat()
            }
        
        try:
            result = broker.place_order(symbol, order_type, side, quantity, price, params)
            result["broker"] = broker.broker_name
            return result
        except Exception as e:
            return broker.handle_error(e, "place_order")
    
    def cancel_order(self, order_id: str, symbol: str) -> Dict[str, Any]:
        """Cancel order through appropriate broker"""
        broker = self.get_broker_for_asset(symbol)
        
        if not broker:
            return {
                "error": f"No suitable broker found for asset: {symbol}",
                "timestamp": datetime.now().isoformat()
            }
        
        try:
            success = broker.cancel_order(order_id)
            return {
                "success": success,
                "broker": broker.broker_name,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return broker.handle_error(e, "cancel_order")
    
    def get_consolidated_positions(self) -> Dict[str, Any]:
        """Get positions from all brokers"""
        consolidated_positions = {}
        
        for broker_name, broker in self.brokers.items():
            if not broker.is_connected():
                continue
                
            try:
                positions = broker.get_positions()
                consolidated_positions[broker_name] = positions
            except Exception as e:
                self.logger.error(f"Error getting positions from {broker_name}: {str(e)}")
                consolidated_positions[broker_name] = {"error": str(e)}
        
        return consolidated_positions
    
    def get_consolidated_balance(self) -> Dict[str, float]:
        """Get balance from all brokers"""
        consolidated_balance = {}
        total_balance = 0.0
        
        for broker_name, broker in self.brokers.items():
            if not broker.is_connected():
                continue
                
            try:
                balance = broker.get_balance()
                consolidated_balance[broker_name] = balance
                total_balance += balance
            except Exception as e:
                self.logger.error(f"Error getting balance from {broker_name}: {str(e)}")
                consolidated_balance[broker_name] = 0.0
        
        consolidated_balance["total"] = total_balance
        return consolidated_balance
    
    def get_market_data(self, symbol: str, timeframe: str, limit: int = 100) -> Dict[str, Any]:
        """Get market data through appropriate broker"""
        broker = self.get_broker_for_asset(symbol)
        
        if not broker:
            return {
                "error": f"No suitable broker found for asset: {symbol}",
                "timestamp": datetime.now().isoformat()
            }
        
        try:
            data = broker.get_market_data(symbol, timeframe, limit)
            return {
                "symbol": symbol,
                "timeframe": timeframe,
                "data": data,
                "broker": broker.broker_name,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return broker.handle_error(e, "get_market_data")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get status of all brokers"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "total_brokers": len(self.brokers),
            "connected_brokers": 0,
            "brokers": {}
        }
        
        for broker_name, broker in self.brokers.items():
            broker_status = broker.get_broker_status()
            status["brokers"][broker_name] = broker_status
            
            if broker_status["connected"] and broker_status["authenticated"]:
                status["connected_brokers"] += 1
        
        return status
    
    def health_check(self) -> Dict[str, Any]:
        """Perform health check on all brokers"""
        health_status = {
            "timestamp": datetime.now().isoformat(),
            "overall_health": "healthy",
            "brokers": {}
        }
        
        unhealthy_count = 0
        
        for broker_name, broker in self.brokers.items():
            try:
                # Simple health check - try to get account info
                account_info = broker.get_account_info()
                health_status["brokers"][broker_name] = {
                    "status": "healthy",
                    "connected": broker.is_connected(),
                    "authenticated": broker.is_authenticated()
                }
            except Exception as e:
                health_status["brokers"][broker_name] = {
                    "status": "unhealthy",
                    "error": str(e),
                    "connected": False,
                    "authenticated": False
                }
                unhealthy_count += 1
        
        if unhealthy_count > 0:
            if unhealthy_count == len(self.brokers):
                health_status["overall_health"] = "critical"
            else:
                health_status["overall_health"] = "degraded"
        
        return health_status