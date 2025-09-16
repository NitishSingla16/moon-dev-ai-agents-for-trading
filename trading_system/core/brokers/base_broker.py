"""
🌙 Moon Dev's Base Broker Interface
Abstract base class for all broker integrations
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

class BaseBroker(ABC):
    """
    Abstract base class for broker integrations
    Defines the common interface for all brokers
    """
    
    def __init__(self, broker_name: str, config: Dict[str, Any]):
        self.broker_name = broker_name
        self.config = config
        self.connected = False
        self.authenticated = False
        
        # Setup logging
        self.logger = logging.getLogger(f"{broker_name}_broker")
        
        # Trading capabilities
        self.supported_assets = []
        self.supported_order_types = []
        self.supported_timeframes = []
        
        # Account information
        self.account_info = {}
        self.positions = {}
        self.orders = {}
        
    @abstractmethod
    def connect(self) -> bool:
        """Connect to the broker"""
        pass
    
    @abstractmethod
    def authenticate(self) -> bool:
        """Authenticate with the broker"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Disconnect from the broker"""
        pass
    
    @abstractmethod
    def get_account_info(self) -> Dict[str, Any]:
        """Get account information"""
        pass
    
    @abstractmethod
    def get_balance(self) -> float:
        """Get account balance"""
        pass
    
    @abstractmethod
    def get_positions(self) -> Dict[str, Any]:
        """Get current positions"""
        pass
    
    @abstractmethod
    def get_open_orders(self) -> List[Dict[str, Any]]:
        """Get open orders"""
        pass
    
    @abstractmethod
    def place_order(self, symbol: str, order_type: str, side: str, 
                   quantity: float, price: Optional[float] = None,
                   params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Place a trading order"""
        pass
    
    @abstractmethod
    def cancel_order(self, order_id: str) -> bool:
        """Cancel an order"""
        pass
    
    @abstractmethod
    def modify_order(self, order_id: str, quantity: Optional[float] = None,
                    price: Optional[float] = None) -> Dict[str, Any]:
        """Modify an existing order"""
        pass
    
    @abstractmethod
    def get_market_data(self, symbol: str, timeframe: str, 
                       limit: int = 100) -> List[Dict[str, Any]]:
        """Get market data (OHLCV)"""
        pass
    
    @abstractmethod
    def get_ticker(self, symbol: str) -> Dict[str, Any]:
        """Get current ticker data"""
        pass
    
    @abstractmethod
    def get_orderbook(self, symbol: str, depth: int = 10) -> Dict[str, Any]:
        """Get order book data"""
        pass
    
    @abstractmethod
    def get_trade_history(self, symbol: Optional[str] = None,
                         start_time: Optional[datetime] = None,
                         end_time: Optional[datetime] = None) -> List[Dict[str, Any]]:
        """Get trade history"""
        pass
    
    def is_connected(self) -> bool:
        """Check if connected to broker"""
        return self.connected
    
    def is_authenticated(self) -> bool:
        """Check if authenticated with broker"""
        return self.authenticated
    
    def get_supported_assets(self) -> List[str]:
        """Get list of supported assets"""
        return self.supported_assets
    
    def get_supported_order_types(self) -> List[str]:
        """Get list of supported order types"""
        return self.supported_order_types
    
    def validate_order(self, symbol: str, order_type: str, side: str,
                      quantity: float, price: Optional[float] = None) -> Dict[str, Any]:
        """Validate order parameters"""
        validation_result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        # Check if symbol is supported
        if symbol not in self.supported_assets:
            validation_result["valid"] = False
            validation_result["errors"].append(f"Unsupported symbol: {symbol}")
        
        # Check order type
        if order_type not in self.supported_order_types:
            validation_result["valid"] = False
            validation_result["errors"].append(f"Unsupported order type: {order_type}")
        
        # Check quantity
        if quantity <= 0:
            validation_result["valid"] = False
            validation_result["errors"].append("Quantity must be positive")
        
        # Check price for limit orders
        if order_type in ["limit", "stop_limit"] and (price is None or price <= 0):
            validation_result["valid"] = False
            validation_result["errors"].append("Price must be specified and positive for limit orders")
        
        return validation_result
    
    def format_symbol(self, base_asset: str, quote_asset: str) -> str:
        """Format symbol according to broker convention"""
        # Default implementation - can be overridden by specific brokers
        return f"{base_asset}{quote_asset}"
    
    def log_trade(self, trade_data: Dict[str, Any]):
        """Log trade execution"""
        self.logger.info(f"Trade executed: {trade_data}")
    
    def handle_error(self, error: Exception, context: str = ""):
        """Handle broker errors"""
        error_msg = f"Broker error in {context}: {str(error)}"
        self.logger.error(error_msg)
        return {"error": error_msg, "timestamp": datetime.now().isoformat()}
    
    def get_broker_status(self) -> Dict[str, Any]:
        """Get broker connection and status information"""
        return {
            "broker_name": self.broker_name,
            "connected": self.connected,
            "authenticated": self.authenticated,
            "supported_assets_count": len(self.supported_assets),
            "supported_order_types": self.supported_order_types,
            "last_update": datetime.now().isoformat()
        }