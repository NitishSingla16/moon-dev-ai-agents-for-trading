"""
🌙 Moon Dev's Quantitative Analyzer
Advanced quantitative analysis with NumPy/SciPy integration
"""

try:
    import numpy as np
    from scipy import stats, optimize, signal
    from scipy.stats import norm, t, chi2
    SCIPY_AVAILABLE = True
except ImportError:
    # Fallback for systems without scipy/pandas
    SCIPY_AVAILABLE = False
    import math
    
    class np:
        @staticmethod
        def array(data):
            return data
        @staticmethod
        def mean(data):
            return sum(data) / len(data) if data else 0
        @staticmethod
        def std(data, ddof=0):
            if not data:
                return 0
            mean_val = sum(data) / len(data)
            variance = sum((x - mean_val) ** 2 for x in data) / (len(data) - ddof if ddof else len(data))
            return math.sqrt(variance)
        @staticmethod
        def diff(data):
            return [data[i] - data[i-1] for i in range(1, len(data))]
        @staticmethod
        def where(condition, true_val, false_val):
            return [true_val if c else false_val for c in condition]
        @staticmethod
        def sum(data):
            return sum(data)
        @staticmethod
        def sqrt(val):
            return math.sqrt(val)
        @staticmethod
        def maximum(data):
            return max(data) if data else 0
        @staticmethod
        def minimum(data):
            return min(data) if data else 0
        @staticmethod
        def percentile(data, q):
            if not data:
                return 0
            sorted_data = sorted(data)
            k = (len(sorted_data) - 1) * q / 100
            f = math.floor(k)
            c = math.ceil(k)
            if f == c:
                return sorted_data[int(k)]
            return sorted_data[int(f)] * (c - k) + sorted_data[int(c)] * (k - f)
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import logging

class QuantitativeAnalyzer:
    """
    Advanced quantitative analysis toolkit featuring:
    - Statistical analysis and hypothesis testing
    - Time series analysis and forecasting
    - Risk metrics calculation (VaR, CVaR, etc.)
    - Portfolio optimization
    - Signal processing and filtering
    - Regime detection and structural breaks
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
        
    def calculate_returns(self, prices, method: str = "simple"):
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
            vol = np.std(returns, ddof=1)
        elif method == "ewma":
            # Exponentially Weighted Moving Average
            alpha = 0.94  # RiskMetrics parameter
            weights = np.array([(1-alpha) * alpha**i for i in range(len(returns))])
            weights = weights[::-1] / weights.sum()
            vol = np.sqrt(np.sum(weights * returns**2))
        elif method == "garch":
            # Simplified GARCH(1,1) estimation
            vol = self._estimate_garch_volatility(returns)
        else:
            raise ValueError("Method must be 'standard', 'ewma', or 'garch'")
        
        if annualize:
            vol *= np.sqrt(252)  # Assume 252 trading days
        
        return vol
    
    def _estimate_garch_volatility(self, returns: np.ndarray) -> float:
        """Estimate GARCH(1,1) volatility"""
        # Simplified GARCH estimation - in practice would use maximum likelihood
        alpha = 0.1  # ARCH parameter
        beta = 0.85  # GARCH parameter
        omega = np.var(returns) * (1 - alpha - beta)
        
        variance = np.var(returns)
        for ret in returns:
            variance = omega + alpha * ret**2 + beta * variance
        
        return np.sqrt(variance)
    
    def calculate_var(self, returns: List[float], confidence_level: float = 0.95, 
                     method: str = "historical") -> float:
        """Calculate Value at Risk"""
        if len(returns) == 0:
            return 0.0
        
        alpha = 1 - confidence_level
        
        if method == "historical":
            var = -np.percentile(returns, alpha * 100)
        elif method == "parametric":
            mu = np.mean(returns)
            sigma = np.std(returns, ddof=1)
            var = -(mu + sigma * norm.ppf(alpha))
        elif method == "cornish_fisher":
            # Cornish-Fisher expansion for non-normal returns
            mu = np.mean(returns)
            sigma = np.std(returns, ddof=1)
            skew = stats.skew(returns)
            kurt = stats.kurtosis(returns, fisher=True)
            
            z_alpha = norm.ppf(alpha)
            cf_adjustment = (z_alpha**2 - 1) * skew / 6 + (z_alpha**3 - 3*z_alpha) * kurt / 24
            var = -(mu + sigma * (z_alpha + cf_adjustment))
        else:
            raise ValueError("Method must be 'historical', 'parametric', or 'cornish_fisher'")
        
        return var
    
    def calculate_cvar(self, returns: List[float], confidence_level: float = 0.95) -> float:
        """Calculate Conditional Value at Risk (Expected Shortfall)"""
        if len(returns) == 0:
            return 0.0
        
        var = self.calculate_var(returns, confidence_level, method="historical")
        cvar = -np.mean(returns[returns <= -var])
        
        return cvar if not np.isnan(cvar) else var
    
    def calculate_sharpe_ratio(self, returns: List[float], risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio"""
        if len(returns) == 0 or np.std(returns) == 0:
            return 0.0
        
        excess_returns = returns - risk_free_rate / 252  # Daily risk-free rate
        return np.mean(excess_returns) / np.std(excess_returns, ddof=1) * np.sqrt(252)
    
    def calculate_sortino_ratio(self, returns: List[float], target_return: float = 0.0) -> float:
        """Calculate Sortino ratio"""
        if len(returns) == 0:
            return 0.0
        
        excess_returns = returns - target_return / 252
        downside_returns = excess_returns[excess_returns < 0]
        
        if len(downside_returns) == 0:
            return float('inf') if np.mean(excess_returns) > 0 else 0.0
        
        downside_deviation = np.std(downside_returns, ddof=1)
        return np.mean(excess_returns) / downside_deviation * np.sqrt(252)
    
    def calculate_maximum_drawdown(self, returns: List[float]) -> Dict[str, float]:
        """Calculate maximum drawdown and related metrics"""
        if len(returns) == 0:
            return {"max_drawdown": 0.0, "duration": 0, "recovery_time": 0}
        
        cumulative = np.cumsum(returns)
        running_max = np.maximum.accumulate(cumulative)
        drawdown = cumulative - running_max
        
        max_drawdown = np.min(drawdown)
        max_dd_idx = np.argmin(drawdown)
        
        # Find drawdown duration
        peak_idx = np.argmax(running_max[:max_dd_idx+1])
        duration = max_dd_idx - peak_idx
        
        # Find recovery time
        recovery_time = 0
        if max_dd_idx < len(cumulative) - 1:
            recovery_level = running_max[max_dd_idx]
            recovery_indices = np.where(cumulative[max_dd_idx:] >= recovery_level)[0]
            if len(recovery_indices) > 0:
                recovery_time = recovery_indices[0]
        
        return {
            "max_drawdown": abs(max_drawdown),
            "duration": duration,
            "recovery_time": recovery_time,
            "calmar_ratio": np.mean(returns) * 252 / abs(max_drawdown) if max_drawdown != 0 else 0
        }
    
    def detect_outliers(self, data: List[float], method: str = "iqr", 
                       threshold: float = 1.5) -> Dict[str, Any]:
        """Detect outliers in data"""
        if len(data) == 0:
            return {"outliers": [], "indices": [], "method": method}
        
        if method == "iqr":
            q1, q3 = np.percentile(data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr
            outlier_mask = (data < lower_bound) | (data > upper_bound)
        
        elif method == "zscore":
            z_scores = np.abs(stats.zscore(data))
            outlier_mask = z_scores > threshold
        
        elif method == "modified_zscore":
            median = np.median(data)
            mad = np.median(np.abs(data - median))
            modified_z_scores = 0.6745 * (data - median) / mad
            outlier_mask = np.abs(modified_z_scores) > threshold
        
        else:
            raise ValueError("Method must be 'iqr', 'zscore', or 'modified_zscore'")
        
        outliers = data[outlier_mask]
        indices = np.where(outlier_mask)[0]
        
        return {
            "outliers": outliers.tolist(),
            "indices": indices.tolist(),
            "method": method,
            "count": len(outliers)
        }
    
    def perform_stationarity_test(self, data: np.ndarray) -> Dict[str, Any]:
        """Perform Augmented Dickey-Fuller test for stationarity"""
        try:
            from statsmodels.tsa.stattools import adfuller
            
            result = adfuller(data)
            
            return {
                "adf_statistic": result[0],
                "p_value": result[1],
                "critical_values": result[4],
                "is_stationary": result[1] < 0.05,
                "confidence_level": "95%"
            }
        except ImportError:
            # Fallback to simplified test
            # Check if mean and variance are stable over time
            mid_point = len(data) // 2
            first_half = data[:mid_point]
            second_half = data[mid_point:]
            
            mean_test = stats.ttest_ind(first_half, second_half)
            var_test = stats.levene(first_half, second_half)
            
            return {
                "mean_stable": mean_test.pvalue > 0.05,
                "variance_stable": var_test.pvalue > 0.05,
                "is_stationary": mean_test.pvalue > 0.05 and var_test.pvalue > 0.05,
                "method": "simplified"
            }
    
    def calculate_correlation_matrix(self, data: Dict[str, np.ndarray]) -> Dict[str, Any]:
        """Calculate correlation matrix with significance tests"""
        assets = list(data.keys())
        n_assets = len(assets)
        
        if n_assets < 2:
            return {"correlation_matrix": {}, "p_values": {}, "significant_correlations": []}
        
        correlation_matrix = {}
        p_values = {}
        significant_correlations = []
        
        for i, asset1 in enumerate(assets):
            correlation_matrix[asset1] = {}
            p_values[asset1] = {}
            
            for j, asset2 in enumerate(assets):
                if asset1 == asset2:
                    correlation_matrix[asset1][asset2] = 1.0
                    p_values[asset1][asset2] = 0.0
                else:
                    # Calculate correlation and p-value
                    corr, p_val = stats.pearsonr(data[asset1], data[asset2])
                    correlation_matrix[asset1][asset2] = corr
                    p_values[asset1][asset2] = p_val
                    
                    # Check if correlation is significant
                    if p_val < 0.05 and abs(corr) > 0.5:
                        significant_correlations.append({
                            "asset1": asset1,
                            "asset2": asset2,
                            "correlation": corr,
                            "p_value": p_val
                        })
        
        return {
            "correlation_matrix": correlation_matrix,
            "p_values": p_values,
            "significant_correlations": significant_correlations
        }
    
    def detect_regime_changes(self, data: np.ndarray, min_segment_length: int = 20) -> Dict[str, Any]:
        """Detect structural breaks/regime changes in time series"""
        if len(data) < min_segment_length * 2:
            return {"change_points": [], "regimes": [], "method": "insufficient_data"}
        
        # Use CUSUM test for change point detection
        cumsum = np.cumsum(data - np.mean(data))
        
        # Find potential change points
        change_points = []
        threshold = 3 * np.std(data) * np.sqrt(len(data))
        
        for i in range(min_segment_length, len(cumsum) - min_segment_length):
            if abs(cumsum[i]) > threshold:
                change_points.append(i)
        
        # Identify regime characteristics
        regimes = []
        start_idx = 0
        
        for cp in change_points + [len(data)]:
            if cp - start_idx >= min_segment_length:
                segment_data = data[start_idx:cp]
                regimes.append({
                    "start": start_idx,
                    "end": cp,
                    "mean": np.mean(segment_data),
                    "std": np.std(segment_data),
                    "trend": self._calculate_trend(segment_data)
                })
            start_idx = cp
        
        return {
            "change_points": change_points,
            "regimes": regimes,
            "method": "cusum",
            "threshold": threshold
        }
    
    def _calculate_trend(self, data: np.ndarray) -> float:
        """Calculate trend slope using linear regression"""
        if len(data) < 2:
            return 0.0
        
        x = np.arange(len(data))
        slope, _, _, _, _ = stats.linregress(x, data)
        return slope
    
    def optimize_portfolio(self, expected_returns: np.ndarray, 
                          covariance_matrix: np.ndarray,
                          risk_aversion: float = 1.0) -> Dict[str, Any]:
        """Optimize portfolio using Modern Portfolio Theory"""
        n_assets = len(expected_returns)
        
        if n_assets == 0:
            return {"weights": [], "expected_return": 0.0, "volatility": 0.0}
        
        # Objective function: maximize utility = return - (risk_aversion * variance) / 2
        def objective(weights):
            portfolio_return = np.sum(weights * expected_returns)
            portfolio_variance = np.dot(weights, np.dot(covariance_matrix, weights))
            return -(portfolio_return - risk_aversion * portfolio_variance / 2)
        
        # Constraints: weights sum to 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        
        # Bounds: weights between 0 and 1 (long-only portfolio)
        bounds = tuple((0, 1) for _ in range(n_assets))
        
        # Initial guess: equal weights
        initial_guess = np.ones(n_assets) / n_assets
        
        try:
            result = optimize.minimize(objective, initial_guess, method='SLSQP',
                                     bounds=bounds, constraints=constraints)
            
            if result.success:
                weights = result.x
                expected_return = np.sum(weights * expected_returns)
                volatility = np.sqrt(np.dot(weights, np.dot(covariance_matrix, weights)))
                
                return {
                    "weights": weights.tolist(),
                    "expected_return": expected_return,
                    "volatility": volatility,
                    "sharpe_ratio": expected_return / volatility if volatility > 0 else 0,
                    "optimization_success": True
                }
            else:
                return {
                    "weights": initial_guess.tolist(),
                    "expected_return": np.sum(initial_guess * expected_returns),
                    "volatility": np.sqrt(np.dot(initial_guess, np.dot(covariance_matrix, initial_guess))),
                    "optimization_success": False,
                    "error": result.message
                }
        
        except Exception as e:
            return {
                "weights": initial_guess.tolist(),
                "expected_return": np.sum(initial_guess * expected_returns),
                "volatility": np.sqrt(np.dot(initial_guess, np.dot(covariance_matrix, initial_guess))),
                "optimization_success": False,
                "error": str(e)
            }
    
    def generate_analytics_report(self, data: Dict[str, np.ndarray]) -> Dict[str, Any]:
        """Generate comprehensive analytics report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "assets_analyzed": len(data),
            "summary_statistics": {},
            "risk_metrics": {},
            "correlation_analysis": {},
            "regime_analysis": {}
        }
        
        # Calculate statistics for each asset
        for asset, prices in data.items():
            if len(prices) < 2:
                continue
                
            returns = self.calculate_returns(prices)
            
            report["summary_statistics"][asset] = {
                "total_return": (prices[-1] / prices[0] - 1) * 100,
                "annualized_return": np.mean(returns) * 252 * 100,
                "volatility": self.calculate_volatility(returns) * 100,
                "sharpe_ratio": self.calculate_sharpe_ratio(returns),
                "max_drawdown": self.calculate_maximum_drawdown(returns),
                "skewness": stats.skew(returns),
                "kurtosis": stats.kurtosis(returns, fisher=True)
            }
            
            report["risk_metrics"][asset] = {
                "var_95": self.calculate_var(returns, 0.95) * 100,
                "var_99": self.calculate_var(returns, 0.99) * 100,
                "cvar_95": self.calculate_cvar(returns, 0.95) * 100,
                "sortino_ratio": self.calculate_sortino_ratio(returns)
            }
        
        # Correlation analysis
        if len(data) > 1:
            returns_data = {asset: self.calculate_returns(prices) 
                          for asset, prices in data.items() if len(prices) > 1}
            report["correlation_analysis"] = self.calculate_correlation_matrix(returns_data)
        
        return report