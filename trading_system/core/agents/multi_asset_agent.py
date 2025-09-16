"""
🌙 Moon Dev's Multi-Asset Trading Agent
Handles trading across multiple asset classes: Forex, Crypto, Stocks, Options, Futures
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import json
from .advanced_base_agent import AdvancedBaseAgent

class MultiAssetAgent(AdvancedBaseAgent):
    """
    Multi-asset trading agent that can handle:
    - Forex pairs (EUR/USD, GBP/USD, etc.)
    - Cryptocurrencies (BTC, ETH, SOL, etc.)
    - Stocks (AAPL, GOOGL, TSLA, etc.)
    - Options contracts
    - Futures contracts
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("multi_asset", config)
        
        # Asset-specific configurations
        self.asset_configs = {
            "FOREX": {
                "session_hours": {"start": 22, "end": 22},  # 24/7 but best hours
                "major_pairs": ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF"],
                "min_pip_movement": 0.0001,
                "default_lot_size": 0.1
            },
            "CRYPTO": {
                "session_hours": {"start": 0, "end": 24},  # 24/7
                "major_tokens": ["BTC", "ETH", "SOL", "ADA", "DOT"],
                "min_price_movement": 0.01,
                "default_size_usd": 100
            },
            "STOCKS": {
                "session_hours": {"start": 9, "end": 16},  # 9:30 AM - 4:00 PM EST
                "major_stocks": ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"],
                "min_price_movement": 0.01,
                "default_shares": 10
            },
            "OPTIONS": {
                "session_hours": {"start": 9, "end": 16},
                "strategies": ["covered_call", "protective_put", "iron_condor"],
                "min_days_to_expiry": 30,
                "max_days_to_expiry": 90
            },
            "FUTURES": {
                "session_hours": {"start": 18, "end": 17},  # Nearly 24/7
                "major_contracts": ["ES", "NQ", "YM", "RTY", "CL", "GC"],
                "margin_requirements": {"ES": 500, "NQ": 800, "CL": 3000},
                "tick_sizes": {"ES": 0.25, "NQ": 0.25, "CL": 0.01}
            }
        }
        
        # Asset allocation and limits
        self.asset_allocation = {
            "FOREX": 0.3,
            "CRYPTO": 0.4,
            "STOCKS": 0.2,
            "OPTIONS": 0.05,
            "FUTURES": 0.05
        }
        
        # Risk parameters per asset class
        self.risk_parameters = {
            "FOREX": {"max_position_size": 0.02, "stop_loss": 0.01, "take_profit": 0.02},
            "CRYPTO": {"max_position_size": 0.05, "stop_loss": 0.05, "take_profit": 0.10},
            "STOCKS": {"max_position_size": 0.03, "stop_loss": 0.03, "take_profit": 0.06},
            "OPTIONS": {"max_position_size": 0.01, "stop_loss": 0.50, "take_profit": 1.00},
            "FUTURES": {"max_position_size": 0.02, "stop_loss": 0.02, "take_profit": 0.04}
        }
        
        # Performance tracking per asset
        self.asset_performance = {asset: {"trades": 0, "pnl": 0.0, "win_rate": 0.0} 
                                 for asset in self.supported_assets}
        
    def is_market_open(self, asset_class: str) -> bool:
        """Check if market is open for specific asset class"""
        if asset_class not in self.asset_configs:
            return False
            
        current_hour = datetime.now().hour
        session = self.asset_configs[asset_class]["session_hours"]
        
        # Handle 24/7 markets
        if session["start"] == 0 and session["end"] == 24:
            return True
        
        # Handle markets that cross midnight
        if session["start"] > session["end"]:
            return current_hour >= session["start"] or current_hour <= session["end"]
        
        # Normal market hours
        return session["start"] <= current_hour <= session["end"]
    
    def get_tradeable_assets(self) -> Dict[str, List[str]]:
        """Get list of tradeable assets by class"""
        tradeable = {}
        
        for asset_class in self.supported_assets:
            if self.is_market_open(asset_class):
                if asset_class == "FOREX":
                    tradeable[asset_class] = self.asset_configs[asset_class]["major_pairs"]
                elif asset_class == "CRYPTO":
                    tradeable[asset_class] = self.asset_configs[asset_class]["major_tokens"]
                elif asset_class == "STOCKS":
                    tradeable[asset_class] = self.asset_configs[asset_class]["major_stocks"]
                elif asset_class == "OPTIONS":
                    tradeable[asset_class] = self.get_active_options()
                elif asset_class == "FUTURES":
                    tradeable[asset_class] = self.asset_configs[asset_class]["major_contracts"]
                    
        return tradeable
    
    def get_active_options(self) -> List[str]:
        """Get active options contracts within expiry range"""
        # Placeholder - in real implementation would query options chain
        return ["AAPL_240315_C_150", "TSLA_240315_P_200", "SPY_240315_C_400"]
    
    def calculate_position_size(self, asset_class: str, asset: str, 
                              account_balance: float, signal_strength: float) -> float:
        """Calculate appropriate position size for asset"""
        if asset_class not in self.risk_parameters:
            return 0.0
            
        # Base allocation
        base_allocation = account_balance * self.asset_allocation[asset_class]
        
        # Risk-adjusted size
        max_position = self.risk_parameters[asset_class]["max_position_size"]
        position_size = base_allocation * max_position * signal_strength
        
        return min(position_size, base_allocation * 0.1)  # Cap at 10% of allocation
    
    def analyze_multi_asset_correlations(self) -> Dict[str, float]:
        """Analyze correlations between different asset classes"""
        # Placeholder for correlation analysis
        # In real implementation would calculate actual correlations
        correlations = {
            "FOREX_CRYPTO": 0.15,
            "CRYPTO_STOCKS": 0.35,
            "STOCKS_OPTIONS": 0.85,
            "FUTURES_FOREX": 0.25,
            "OPTIONS_FUTURES": 0.20
        }
        
        return correlations
    
    def optimize_asset_allocation(self):
        """Optimize asset allocation based on performance and correlations"""
        correlations = self.analyze_multi_asset_correlations()
        
        # Simple rebalancing based on performance
        for asset_class in self.supported_assets:
            performance = self.asset_performance[asset_class]
            
            # Increase allocation for well-performing assets
            if performance["win_rate"] > 0.6 and performance["pnl"] > 0:
                self.asset_allocation[asset_class] *= 1.1
            # Decrease allocation for poor-performing assets
            elif performance["win_rate"] < 0.4 or performance["pnl"] < 0:
                self.asset_allocation[asset_class] *= 0.9
        
        # Normalize allocations to sum to 1.0
        total = sum(self.asset_allocation.values())
        if total > 0:
            for asset_class in self.asset_allocation:
                self.asset_allocation[asset_class] /= total
                
        self.logger.info(f"Asset allocation optimized: {self.asset_allocation}")
    
    def get_asset_signals(self, asset_class: str, asset: str) -> Dict[str, Any]:
        """Get trading signals for specific asset"""
        # Placeholder for asset-specific signal generation
        # In real implementation would use technical/fundamental analysis
        
        signal = {
            "asset_class": asset_class,
            "asset": asset,
            "signal": "HOLD",  # BUY, SELL, HOLD
            "strength": 0.5,   # 0.0 to 1.0
            "confidence": 0.6, # 0.0 to 1.0
            "timestamp": datetime.now().isoformat(),
            "analysis": {
                "technical": "Neutral trend with support at key level",
                "fundamental": "Mixed indicators",
                "sentiment": "Slightly bullish"
            }
        }
        
        return signal
    
    def execute_multi_asset_strategy(self):
        """Execute trading strategy across multiple asset classes"""
        tradeable_assets = self.get_tradeable_assets()
        account_balance = 10000  # Placeholder - get from broker
        
        for asset_class, assets in tradeable_assets.items():
            if not assets:
                continue
                
            self.logger.info(f"Analyzing {asset_class} markets: {len(assets)} assets")
            
            for asset in assets:
                signal = self.get_asset_signals(asset_class, asset)
                
                if signal["signal"] in ["BUY", "SELL"] and signal["confidence"] > 0.7:
                    position_size = self.calculate_position_size(
                        asset_class, asset, account_balance, signal["strength"]
                    )
                    
                    if position_size > 0:
                        self.execute_trade(asset_class, asset, signal, position_size)
    
    def execute_trade(self, asset_class: str, asset: str, signal: Dict[str, Any], size: float):
        """Execute trade for specific asset"""
        trade = {
            "timestamp": datetime.now().isoformat(),
            "asset_class": asset_class,
            "asset": asset,
            "signal": signal["signal"],
            "size": size,
            "confidence": signal["confidence"],
            "executed": False  # Placeholder - would be True after actual execution
        }
        
        # Log the trade
        self.logger.info(f"Trade signal: {signal['signal']} {asset} ({asset_class}) "
                        f"Size: {size:.2f} Confidence: {signal['confidence']:.2f}")
        
        # Update performance tracking (placeholder)
        self.asset_performance[asset_class]["trades"] += 1
        
        # In real implementation, would execute through appropriate broker
        # self.brokers[asset_class].execute_trade(trade)
    
    def run(self):
        """Main execution loop for multi-asset trading"""
        self.logger.info("Starting Multi-Asset Trading Agent")
        
        try:
            while True:
                # Optimize asset allocation periodically
                if datetime.now().minute % 30 == 0:  # Every 30 minutes
                    self.optimize_asset_allocation()
                
                # Execute multi-asset strategy
                self.execute_multi_asset_strategy()
                
                # Learn from market data
                market_data = {
                    "tradeable_assets": self.get_tradeable_assets(),
                    "correlations": self.analyze_multi_asset_correlations(),
                    "allocations": self.asset_allocation,
                    "performance": self.asset_performance
                }
                self.learn_from_market_data(market_data)
                
                # Update performance metrics
                self.update_performance_metrics({
                    "success": True,
                    "pnl": 0.0,  # Placeholder
                    "timestamp": datetime.now().isoformat()
                })
                
                # Sleep before next iteration
                import time
                time.sleep(60)  # Run every minute
                
        except KeyboardInterrupt:
            self.logger.info("Multi-Asset Trading Agent stopped by user")
        except Exception as e:
            self.logger.error(f"Error in Multi-Asset Trading Agent: {str(e)}")
            raise