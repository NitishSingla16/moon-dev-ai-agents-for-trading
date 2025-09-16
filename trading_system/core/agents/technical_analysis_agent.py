"""
🌙 Moon Dev's Technical Analysis Agent
Advanced technical analysis with multiple indicators and pattern recognition
"""

import math
from typing import Dict, List, Any, Optional
from datetime import datetime
from .advanced_base_agent import AdvancedBaseAgent

class TechnicalAnalysisAgent(AdvancedBaseAgent):
    """
    Technical Analysis Agent that provides:
    - Multiple technical indicators (RSI, MACD, Bollinger Bands, etc.)
    - Chart pattern recognition
    - Support/resistance levels
    - Trend analysis
    - Signal generation and confirmation
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("technical_analysis", config)
        
        # Technical analysis parameters
        self.indicators = {
            "rsi_period": 14,
            "macd_fast": 12,
            "macd_slow": 26,
            "macd_signal": 9,
            "bb_period": 20,
            "bb_std": 2,
            "ema_short": 10,
            "ema_long": 30
        }
        
    def calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """Calculate Relative Strength Index"""
        if len(prices) < period + 1:
            return 50.0
        
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        
        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period
        
        if avg_loss == 0:
            return 100.0
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def calculate_macd(self, prices: List[float]) -> Dict[str, float]:
        """Calculate MACD indicator"""
        if len(prices) < max(self.indicators["macd_slow"], self.indicators["macd_signal"]):
            return {"macd": 0.0, "signal": 0.0, "histogram": 0.0}
        
        # Simple moving averages (in practice would use EMA)
        fast_period = self.indicators["macd_fast"]
        slow_period = self.indicators["macd_slow"]
        
        fast_ma = sum(prices[-fast_period:]) / fast_period
        slow_ma = sum(prices[-slow_period:]) / slow_period
        
        macd_line = fast_ma - slow_ma
        signal_line = macd_line * 0.9  # Simplified signal line
        histogram = macd_line - signal_line
        
        return {
            "macd": macd_line,
            "signal": signal_line,
            "histogram": histogram
        }
    
    def calculate_bollinger_bands(self, prices: List[float]) -> Dict[str, float]:
        """Calculate Bollinger Bands"""
        period = self.indicators["bb_period"]
        std_mult = self.indicators["bb_std"]
        
        if len(prices) < period:
            current_price = prices[-1] if len(prices) > 0 else 100.0
            return {
                "upper": current_price * 1.02,
                "middle": current_price,
                "lower": current_price * 0.98,
                "position": 0.5
            }
        
        recent_prices = prices[-period:]
        sma = sum(recent_prices) / len(recent_prices)
        
        # Calculate standard deviation
        variance = sum((price - sma) ** 2 for price in recent_prices) / len(recent_prices)
        std = math.sqrt(variance)
        
        upper = sma + (std * std_mult)
        lower = sma - (std * std_mult)
        
        current_price = prices[-1]
        position = (current_price - lower) / (upper - lower) if upper != lower else 0.5
        
        return {
            "upper": upper,
            "middle": sma,
            "lower": lower,
            "position": position
        }
    
    def generate_technical_signals(self, prices: List[float], volumes: List[float] = None) -> Dict[str, Any]:
        """Generate comprehensive technical analysis signals"""
        if len(prices) < 20:
            return {"signal": "HOLD", "strength": 0.5, "confidence": 0.3, "indicators": {}}
        
        # Calculate indicators
        rsi = self.calculate_rsi(prices)
        macd = self.calculate_macd(prices)
        bb = self.calculate_bollinger_bands(prices)
        
        # Price analysis
        current_price = prices[-1]
        price_change = (current_price - prices[-2]) / prices[-2] * 100 if len(prices) > 1 else 0
        
        # Trend analysis
        short_period = self.indicators["ema_short"]
        long_period = self.indicators["ema_long"]
        
        short_ma = sum(prices[-short_period:]) / short_period if len(prices) >= short_period else current_price
        long_ma = sum(prices[-long_period:]) / long_period if len(prices) >= long_period else current_price
        
        trend = "UPTREND" if short_ma > long_ma else "DOWNTREND" if short_ma < long_ma else "SIDEWAYS"
        
        # Signal generation
        signals = []
        
        # RSI signals
        if rsi < 30:
            signals.append(("BUY", 0.7, "RSI oversold"))
        elif rsi > 70:
            signals.append(("SELL", 0.7, "RSI overbought"))
        
        # MACD signals
        if macd["histogram"] > 0 and macd["macd"] > macd["signal"]:
            signals.append(("BUY", 0.6, "MACD bullish"))
        elif macd["histogram"] < 0 and macd["macd"] < macd["signal"]:
            signals.append(("SELL", 0.6, "MACD bearish"))
        
        # Bollinger Bands signals
        if bb["position"] < 0.1:
            signals.append(("BUY", 0.5, "BB lower band bounce"))
        elif bb["position"] > 0.9:
            signals.append(("SELL", 0.5, "BB upper band rejection"))
        
        # Trend signals
        if trend == "UPTREND" and current_price > short_ma:
            signals.append(("BUY", 0.4, "Trend following"))
        elif trend == "DOWNTREND" and current_price < short_ma:
            signals.append(("SELL", 0.4, "Trend following"))
        
        # Aggregate signals
        buy_strength = sum(strength for signal, strength, reason in signals if signal == "BUY")
        sell_strength = sum(strength for signal, strength, reason in signals if signal == "SELL")
        
        if buy_strength > sell_strength + 0.3:
            final_signal = "BUY"
            signal_strength = min(buy_strength / 2, 1.0)
        elif sell_strength > buy_strength + 0.3:
            final_signal = "SELL"
            signal_strength = min(sell_strength / 2, 1.0)
        else:
            final_signal = "HOLD"
            signal_strength = 0.5
        
        confidence = min(len(signals) / 5, 1.0) * 0.8 + 0.2  # Base confidence of 20%
        
        return {
            "signal": final_signal,
            "strength": signal_strength,
            "confidence": confidence,
            "indicators": {
                "rsi": rsi,
                "macd": macd,
                "bollinger_bands": bb,
                "trend": trend,
                "price_change": price_change
            },
            "supporting_signals": [f"{signal} ({strength:.2f}): {reason}" for signal, strength, reason in signals],
            "timestamp": datetime.now().isoformat()
        }
    
    def run(self):
        """Run technical analysis"""
        # Placeholder for actual implementation
        self.logger.info("Technical Analysis Agent running...")
        
        # In real implementation, would:
        # 1. Get market data from broker
        # 2. Calculate technical indicators
        # 3. Generate signals
        # 4. Update performance metrics
        pass