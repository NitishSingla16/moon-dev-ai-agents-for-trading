"""
🌙 Moon Dev's Simple Quantitative Analyzer
Basic quantitative analysis without external dependencies
"""

import math
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import logging

class QuantitativeAnalyzer:
    """
    Simple quantitative analysis toolkit with basic Python only
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.logger = logging.getLogger("quantitative_analyzer")
        
        # Analysis parameters
        self.confidence_levels = [0.90, 0.95, 0.99]
        self.window_sizes = {
            "short": 20,
            "medium": 60,
            "long": 252
        }
        
        # Cache for computationally expensive operations
        self.cache = {}
    
    def calculate_returns(self, prices: List[float], method: str = "simple") -> List[float]:
        """Calculate returns from price series"""
        if len(prices) < 2:
            return []
        
        if method == "simple":
            returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
        elif method == "log":
            returns = [math.log(prices[i] / prices[i-1]) for i in range(1, len(prices))]
        else:
            raise ValueError("Method must be 'simple' or 'log'")
        
        return returns
    
    def calculate_volatility(self, returns: List[float], method: str = "standard", 
                           window: Optional[int] = None, annualize: bool = True) -> float:
        """Calculate volatility using various methods"""
        if len(returns) == 0:
            return 0.0
        
        if method == "standard":
            vol = self._std(returns)
        elif method == "ewma":
            # Exponentially Weighted Moving Average
            alpha = 0.94  # RiskMetrics parameter
            vol = self._ewma_volatility(returns, alpha)
        else:
            vol = self._std(returns)
        
        if annualize:
            vol *= math.sqrt(252)  # Assume 252 trading days
        
        return vol
    
    def _mean(self, data: List[float]) -> float:
        """Calculate mean"""
        return sum(data) / len(data) if data else 0.0
    
    def _std(self, data: List[float]) -> float:
        """Calculate standard deviation"""
        if not data:
            return 0.0
        
        mean_val = self._mean(data)
        variance = sum((x - mean_val) ** 2 for x in data) / (len(data) - 1)
        return math.sqrt(variance)
    
    def _ewma_volatility(self, returns: List[float], alpha: float) -> float:
        """Calculate EWMA volatility"""
        if not returns:
            return 0.0
        
        variance = returns[0] ** 2
        for ret in returns[1:]:
            variance = alpha * variance + (1 - alpha) * ret ** 2
        
        return math.sqrt(variance)
    
    def calculate_var(self, returns: List[float], confidence_level: float = 0.95, 
                     method: str = "historical") -> float:
        """Calculate Value at Risk"""
        if len(returns) == 0:
            return 0.0
        
        alpha = 1 - confidence_level
        
        if method == "historical":
            sorted_returns = sorted(returns)
            index = int(alpha * len(sorted_returns))
            var = -sorted_returns[index] if index < len(sorted_returns) else 0
        elif method == "parametric":
            mu = self._mean(returns)
            sigma = self._std(returns)
            # Approximate normal distribution critical value
            z_alpha = self._norm_ppf(alpha)
            var = -(mu + sigma * z_alpha)
        else:
            # Default to historical
            sorted_returns = sorted(returns)
            index = int(alpha * len(sorted_returns))
            var = -sorted_returns[index] if index < len(sorted_returns) else 0
        
        return var
    
    def _norm_ppf(self, p: float) -> float:
        """Approximate normal distribution percent point function"""
        # Simplified approximation for normal distribution
        if p <= 0.01:
            return -2.33
        elif p <= 0.05:
            return -1.645
        elif p <= 0.1:
            return -1.28
        elif p >= 0.99:
            return 2.33
        elif p >= 0.95:
            return 1.645
        elif p >= 0.9:
            return 1.28
        else:
            return 0.0  # Approximate for middle values
    
    def calculate_cvar(self, returns: List[float], confidence_level: float = 0.95) -> float:
        """Calculate Conditional Value at Risk (Expected Shortfall)"""
        if len(returns) == 0:
            return 0.0
        
        var = self.calculate_var(returns, confidence_level, method="historical")
        tail_returns = [r for r in returns if r <= -var]
        
        if tail_returns:
            cvar = -self._mean(tail_returns)
        else:
            cvar = var
        
        return cvar
    
    def calculate_sharpe_ratio(self, returns: List[float], risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio"""
        if len(returns) == 0:
            return 0.0
            
        excess_returns = [r - risk_free_rate / 252 for r in returns]  # Daily risk-free rate
        mean_excess = self._mean(excess_returns)
        std_excess = self._std(excess_returns)
        
        if std_excess == 0:
            return 0.0
        
        return mean_excess / std_excess * math.sqrt(252)
    
    def calculate_maximum_drawdown(self, returns: List[float]) -> Dict[str, float]:
        """Calculate maximum drawdown and related metrics"""
        if len(returns) == 0:
            return {"max_drawdown": 0.0, "duration": 0, "recovery_time": 0}
        
        # Calculate cumulative returns
        cumulative = [sum(returns[:i+1]) for i in range(len(returns))]
        
        # Calculate running maximum
        running_max = []
        current_max = cumulative[0]
        for val in cumulative:
            current_max = max(current_max, val)
            running_max.append(current_max)
        
        # Calculate drawdown series
        drawdown = [cumulative[i] - running_max[i] for i in range(len(cumulative))]
        
        max_drawdown = min(drawdown) if drawdown else 0.0
        max_dd_idx = drawdown.index(max_drawdown) if max_drawdown in drawdown else 0
        
        # Find duration (simplified)
        duration = 0
        for i in range(max_dd_idx):
            if running_max[i] == running_max[max_dd_idx]:
                duration = max_dd_idx - i
                break
        
        return {
            "max_drawdown": abs(max_drawdown),
            "duration": duration,
            "recovery_time": 0,  # Simplified
            "calmar_ratio": self._mean(returns) * 252 / abs(max_drawdown) if max_drawdown != 0 else 0
        }
    
    def generate_analytics_report(self, data: Dict[str, List[float]]) -> Dict[str, Any]:
        """Generate comprehensive analytics report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "assets_analyzed": len(data),
            "summary_statistics": {},
            "risk_metrics": {}
        }
        
        # Calculate statistics for each asset
        for asset, prices in data.items():
            if len(prices) < 2:
                continue
                
            returns = self.calculate_returns(prices)
            
            report["summary_statistics"][asset] = {
                "total_return": (prices[-1] / prices[0] - 1) * 100 if prices[0] != 0 else 0,
                "annualized_return": self._mean(returns) * 252 * 100,
                "volatility": self.calculate_volatility(returns) * 100,
                "sharpe_ratio": self.calculate_sharpe_ratio(returns),
                "max_drawdown": self.calculate_maximum_drawdown(returns)
            }
            
            report["risk_metrics"][asset] = {
                "var_95": self.calculate_var(returns, 0.95) * 100,
                "var_99": self.calculate_var(returns, 0.99) * 100,
                "cvar_95": self.calculate_cvar(returns, 0.95) * 100
            }
        
        return report