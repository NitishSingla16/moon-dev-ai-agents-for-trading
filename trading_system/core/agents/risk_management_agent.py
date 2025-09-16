"""
🌙 Moon Dev's Advanced Risk Management Agent
Sophisticated risk management with dynamic position sizing, correlation analysis, and drawdown protection
"""

import math
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import json
import math
from .advanced_base_agent import AdvancedBaseAgent

class RiskManagementAgent(AdvancedBaseAgent):
    """
    Advanced risk management agent with:
    - Dynamic position sizing based on volatility
    - Correlation analysis for portfolio optimization
    - Drawdown protection with multiple levels
    - Real-time risk monitoring and alerts
    - Monte Carlo simulations for risk assessment
    - VaR (Value at Risk) calculations
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("risk_management", config)
        
        # Risk parameters
        self.risk_params = {
            "max_portfolio_risk": 0.02,      # 2% max portfolio risk per day
            "max_position_risk": 0.005,      # 0.5% max risk per position
            "max_correlation": 0.7,          # Max correlation between positions
            "max_drawdown": 0.15,            # 15% max drawdown before protection
            "var_confidence": 0.95,          # VaR confidence level
            "volatility_lookback": 20,       # Days for volatility calculation
            "correlation_lookback": 60       # Days for correlation calculation
        }
        
        # Risk monitoring
        self.portfolio_metrics = {
            "total_exposure": 0.0,
            "net_exposure": 0.0,
            "gross_exposure": 0.0,
            "current_drawdown": 0.0,
            "portfolio_var": 0.0,
            "portfolio_volatility": 0.0,
            "sharpe_ratio": 0.0,
            "beta": 1.0
        }
        
        # Position tracking
        self.positions = {}
        self.historical_pnl = []
        self.correlation_matrix = {}
        
        # Risk alerts
        self.risk_alerts = []
        self.alert_thresholds = {
            "high_correlation": 0.8,
            "high_volatility": 0.03,
            "large_position": 0.01,
            "drawdown_warning": 0.10,
            "drawdown_critical": 0.15
        }
        
    def calculate_position_size(self, asset: str, signal_strength: float, 
                              volatility: float, account_balance: float) -> float:
        """
        Calculate optimal position size using Kelly Criterion and volatility adjustment
        """
        # Kelly Criterion: f = (bp - q) / b
        # Where: b = odds, p = probability of win, q = probability of loss
        
        # Estimate probability based on signal strength and historical performance
        win_probability = min(0.4 + (signal_strength * 0.3), 0.8)  # Cap at 80%
        loss_probability = 1 - win_probability
        
        # Estimate odds based on typical risk/reward ratio
        risk_reward_ratio = 2.0  # Target 2:1 reward:risk
        
        # Kelly fraction
        kelly_fraction = (win_probability * risk_reward_ratio - loss_probability) / risk_reward_ratio
        kelly_fraction = max(0, min(kelly_fraction, 0.25))  # Cap at 25%
        
        # Volatility adjustment
        vol_adjustment = min(1.0, self.risk_params["max_position_risk"] / volatility)
        
        # Base position size
        base_size = account_balance * kelly_fraction * vol_adjustment
        
        # Apply maximum position risk limit
        max_size = account_balance * self.risk_params["max_position_risk"]
        
        return min(base_size, max_size)
    
    def calculate_portfolio_var(self, confidence_level: float = 0.95) -> float:
        """Calculate Portfolio Value at Risk using historical simulation"""
        if len(self.historical_pnl) < 30:
            return 0.0
        
        # Sort historical PnL in ascending order
        sorted_pnl = sorted(self.historical_pnl[-252:])  # Last 252 trading days
        
        # Calculate VaR at specified confidence level
        var_index = int((1 - confidence_level) * len(sorted_pnl))
        portfolio_var = abs(sorted_pnl[var_index]) if var_index < len(sorted_pnl) else 0.0
        
        return portfolio_var
    
    def calculate_correlation_matrix(self, assets: List[str], 
                                   price_data: Dict[str, List[float]]) -> Dict[str, Dict[str, float]]:
        """Calculate correlation matrix for portfolio assets"""
        correlation_matrix = {}
        
        for asset1 in assets:
            correlation_matrix[asset1] = {}
            for asset2 in assets:
                if asset1 == asset2:
                    correlation_matrix[asset1][asset2] = 1.0
                elif asset1 in price_data and asset2 in price_data:
                    # Calculate correlation coefficient
                    corr = np.corrcoef(price_data[asset1], price_data[asset2])[0, 1]
                    correlation_matrix[asset1][asset2] = corr if not np.isnan(corr) else 0.0
                else:
                    correlation_matrix[asset1][asset2] = 0.0
        
        return correlation_matrix
    
    def check_correlation_risk(self, new_asset: str, existing_positions: Dict[str, float]) -> bool:
        """Check if adding new position would create excessive correlation risk"""
        if not existing_positions or new_asset not in self.correlation_matrix:
            return True  # Allow if no existing positions or no correlation data
        
        for existing_asset in existing_positions.keys():
            if existing_asset in self.correlation_matrix.get(new_asset, {}):
                correlation = abs(self.correlation_matrix[new_asset][existing_asset])
                if correlation > self.risk_params["max_correlation"]:
                    self.add_risk_alert(
                        f"High correlation risk: {new_asset} vs {existing_asset} "
                        f"(correlation: {correlation:.2f})"
                    )
                    return False
        
        return True
    
    def calculate_portfolio_volatility(self, positions: Dict[str, float], 
                                     volatilities: Dict[str, float]) -> float:
        """Calculate portfolio volatility considering correlations"""
        if not positions or not volatilities:
            return 0.0
        
        assets = list(positions.keys())
        weights = [positions[asset] for asset in assets]
        vols = [volatilities.get(asset, 0.0) for asset in assets]
        
        # Simplified portfolio volatility calculation
        weighted_vol_squared = sum((weights[i] * vols[i])**2 for i in range(len(assets)))
        
        # Add correlation effects (simplified)
        correlation_effect = 0.0
        for i in range(len(assets)):
            for j in range(i+1, len(assets)):
                corr = self.correlation_matrix.get(assets[i], {}).get(assets[j], 0.0)
                correlation_effect += 2 * weights[i] * weights[j] * vols[i] * vols[j] * corr
        
        portfolio_variance = weighted_vol_squared + correlation_effect
        return math.sqrt(max(0, portfolio_variance))
    
    def monte_carlo_risk_simulation(self, positions: Dict[str, float], 
                                   num_simulations: int = 1000) -> Dict[str, float]:
        """Run Monte Carlo simulation for portfolio risk assessment"""
        if not positions:
            return {"var_95": 0.0, "var_99": 0.0, "expected_return": 0.0, "volatility": 0.0}
        
        # Simplified Monte Carlo simulation
        import random
        
        simulated_portfolio_returns = []
        
        for _ in range(num_simulations):
            portfolio_return = 0.0
            
            for asset, weight in positions.items():
                # Generate random return based on historical volatility
                volatility = 0.02  # Placeholder 2% daily volatility
                random_return = random.gauss(0, volatility)
                portfolio_return += weight * random_return
            
            simulated_portfolio_returns.append(portfolio_return)
        
        # Calculate risk metrics
        sorted_returns = sorted(simulated_portfolio_returns)
        
        return {
            "var_95": abs(sorted_returns[int(0.05 * num_simulations)]),
            "var_99": abs(sorted_returns[int(0.01 * num_simulations)]),
            "expected_return": sum(simulated_portfolio_returns) / len(simulated_portfolio_returns),
            "volatility": math.sqrt(sum((r - sum(simulated_portfolio_returns) / len(simulated_portfolio_returns))**2 
                                       for r in simulated_portfolio_returns) / len(simulated_portfolio_returns))
        }
    
    def calculate_drawdown(self, pnl_series: List[float]) -> Tuple[float, float]:
        """Calculate current and maximum drawdown"""
        if not pnl_series:
            return 0.0, 0.0
        
        # Calculate cumulative returns
        cumulative = []
        running_sum = 0
        for pnl in pnl_series:
            running_sum += pnl
            cumulative.append(running_sum)
        
        # Calculate running maximum
        running_max = []
        current_max = cumulative[0] if cumulative else 0
        for val in cumulative:
            current_max = max(current_max, val)
            running_max.append(current_max)
        
        # Calculate drawdown series
        drawdown = [cumulative[i] - running_max[i] for i in range(len(cumulative))]
        
        current_drawdown = drawdown[-1] if drawdown else 0.0
        max_drawdown = min(drawdown) if drawdown else 0.0
        
        return abs(current_drawdown), abs(max_drawdown)
    
    def check_drawdown_protection(self) -> Dict[str, Any]:
        """Check drawdown levels and return protection actions"""
        current_dd, max_dd = self.calculate_drawdown(self.historical_pnl)
        
        protection_actions = {
            "reduce_exposure": False,
            "halt_trading": False,
            "close_positions": False,
            "current_drawdown": current_dd,
            "max_drawdown": max_dd
        }
        
        if current_dd > self.alert_thresholds["drawdown_warning"]:
            self.add_risk_alert(f"Drawdown warning: {current_dd:.1%}")
            protection_actions["reduce_exposure"] = True
        
        if current_dd > self.alert_thresholds["drawdown_critical"]:
            self.add_risk_alert(f"Critical drawdown: {current_dd:.1%}")
            protection_actions["halt_trading"] = True
        
        if current_dd > self.risk_params["max_drawdown"]:
            self.add_risk_alert(f"Maximum drawdown exceeded: {current_dd:.1%}")
            protection_actions["close_positions"] = True
        
        return protection_actions
    
    def add_risk_alert(self, message: str, severity: str = "WARNING"):
        """Add risk alert to monitoring system"""
        alert = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "severity": severity
        }
        
        self.risk_alerts.append(alert)
        self.logger.warning(f"RISK ALERT [{severity}]: {message}")
        
        # Keep only recent alerts
        if len(self.risk_alerts) > 100:
            self.risk_alerts = self.risk_alerts[-100:]
    
    def update_portfolio_metrics(self, positions: Dict[str, float], 
                               pnl: float, market_data: Dict[str, Any]):
        """Update portfolio risk metrics"""
        # Update PnL history
        self.historical_pnl.append(pnl)
        if len(self.historical_pnl) > 1000:  # Keep last 1000 data points
            self.historical_pnl = self.historical_pnl[-1000:]
        
        # Calculate metrics
        self.portfolio_metrics.update({
            "total_exposure": sum(abs(pos) for pos in positions.values()),
            "net_exposure": sum(positions.values()),
            "gross_exposure": sum(abs(pos) for pos in positions.values()),
            "portfolio_var": self.calculate_portfolio_var(),
            "current_drawdown": self.calculate_drawdown(self.historical_pnl)[0]
        })
        
        # Check risk thresholds
        self.check_risk_thresholds()
    
    def check_risk_thresholds(self):
        """Check all risk thresholds and generate alerts"""
        metrics = self.portfolio_metrics
        
        if metrics["total_exposure"] > 1.0:  # 100% exposure
            self.add_risk_alert(f"High portfolio exposure: {metrics['total_exposure']:.1%}")
        
        if metrics["portfolio_var"] > self.risk_params["max_portfolio_risk"]:
            self.add_risk_alert(f"Portfolio VaR exceeds limit: {metrics['portfolio_var']:.1%}")
        
        if metrics["current_drawdown"] > self.alert_thresholds["drawdown_warning"]:
            self.add_risk_alert(f"Drawdown alert: {metrics['current_drawdown']:.1%}")
    
    def get_risk_report(self) -> Dict[str, Any]:
        """Generate comprehensive risk report"""
        return {
            "timestamp": datetime.now().isoformat(),
            "portfolio_metrics": self.portfolio_metrics,
            "risk_parameters": self.risk_params,
            "recent_alerts": self.risk_alerts[-10:],  # Last 10 alerts
            "drawdown_protection": self.check_drawdown_protection(),
            "monte_carlo_simulation": self.monte_carlo_risk_simulation(self.positions)
        }
    
    def run(self):
        """Main risk management monitoring loop"""
        self.logger.info("Starting Advanced Risk Management Agent")
        
        try:
            while True:
                # Update risk metrics
                # (In real implementation, would get actual positions and PnL)
                sample_positions = {"BTC": 0.3, "ETH": 0.2, "SOL": 0.1}
                sample_pnl = 0.0  # Placeholder
                sample_market_data = {}
                
                self.update_portfolio_metrics(sample_positions, sample_pnl, sample_market_data)
                
                # Generate risk report
                risk_report = self.get_risk_report()
                
                # Save risk report
                self.save_risk_report(risk_report)
                
                # Learn from risk data
                self.learn_from_market_data({
                    "risk_metrics": self.portfolio_metrics,
                    "alerts": len(self.risk_alerts),
                    "positions": len(self.positions)
                })
                
                # Sleep before next check
                import time
                time.sleep(30)  # Check every 30 seconds
                
        except KeyboardInterrupt:
            self.logger.info("Risk Management Agent stopped by user")
        except Exception as e:
            self.logger.error(f"Error in Risk Management Agent: {str(e)}")
            raise
    
    def save_risk_report(self, report: Dict[str, Any]):
        """Save risk report to file"""
        report_file = self.data_path / f"risk_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)