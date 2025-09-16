"""
🌙 Moon Dev's Continuous Learning System
System that continuously learns from market data and trading performance
"""

import math
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import logging

class ContinuousLearner:
    """
    Continuous learning system that:
    - Learns from market patterns and trading outcomes
    - Adapts strategies based on performance
    - Updates model parameters automatically
    - Identifies new market regimes
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        
        # Setup logging
        self.logger = logging.getLogger("continuous_learner")
        
        # Learning parameters
        self.learning_rate = self.config.get("learning_rate", 0.01)
        self.memory_size = self.config.get("memory_size", 10000)
        self.batch_size = self.config.get("batch_size", 100)
        self.update_frequency = self.config.get("update_frequency", 100)
        
        # Data storage
        self.data_path = Path("trading_system/data/learning")
        self.data_path.mkdir(parents=True, exist_ok=True)
        
        # Learning memory
        self.memory_buffer = []
        self.performance_history = []
        self.market_patterns = {}
        self.strategy_weights = {}
        
        # Model state
        self.model_version = 1
        self.last_update = None
        self.learning_metrics = {
            "total_samples": 0,
            "learning_cycles": 0,
            "accuracy": 0.0,
            "improvement_rate": 0.0
        }
        
        # Market regime detection
        self.market_regimes = {
            "trending": {"up": 0.0, "down": 0.0},
            "ranging": 0.0,
            "volatile": 0.0,
            "current_regime": "unknown"
        }
        
        # Load existing model if available
        self.load_model_state()
    
    def add_experience(self, market_data: Dict[str, Any], action: str, 
                      outcome: float, metadata: Dict[str, Any] = None):
        """Add new trading experience to learning memory"""
        experience = {
            "timestamp": datetime.now().isoformat(),
            "market_data": market_data,
            "action": action,
            "outcome": outcome,
            "metadata": metadata or {},
            "features": self.extract_features(market_data)
        }
        
        self.memory_buffer.append(experience)
        
        # Maintain memory size limit
        if len(self.memory_buffer) > self.memory_size:
            self.memory_buffer = self.memory_buffer[-self.memory_size:]
        
        self.learning_metrics["total_samples"] += 1
        
        # Trigger learning if enough new samples
        if len(self.memory_buffer) % self.update_frequency == 0:
            self.learn_from_experiences()
    
    def extract_features(self, market_data: Dict[str, Any]) -> List[float]:
        """Extract numerical features from market data"""
        features = []
        
        # Price-based features
        if "price" in market_data:
            features.append(market_data["price"])
        
        # Volume features
        if "volume" in market_data:
            features.append(market_data["volume"])
        
        # Technical indicators
        if "indicators" in market_data:
            indicators = market_data["indicators"]
            features.extend([
                indicators.get("rsi", 50),
                indicators.get("macd", 0),
                indicators.get("bollinger_position", 0.5),
                indicators.get("volume_sma_ratio", 1.0)
            ])
        
        # Market sentiment
        if "sentiment" in market_data:
            features.append(market_data["sentiment"])
        
        # Volatility measures
        if "volatility" in market_data:
            features.append(market_data["volatility"])
        
        # Ensure consistent feature size
        while len(features) < 10:  # Pad to standard size
            features.append(0.0)
        
        return features[:10]  # Limit to standard size
    
    def learn_from_experiences(self):
        """Learn from recent trading experiences"""
        if len(self.memory_buffer) < self.batch_size:
            return
        
        self.logger.info(f"Starting learning cycle with {len(self.memory_buffer)} experiences")
        
        # Sample experiences for learning
        sample_size = min(self.batch_size, len(self.memory_buffer))
        recent_experiences = self.memory_buffer[-sample_size:]
        
        # Extract patterns
        patterns = self.identify_patterns(recent_experiences)
        self.update_market_patterns(patterns)
        
        # Update strategy weights based on performance
        self.update_strategy_weights(recent_experiences)
        
        # Detect market regime changes
        self.detect_market_regime(recent_experiences)
        
        # Update model parameters
        self.update_model_parameters(recent_experiences)
        
        # Save learning progress
        self.learning_metrics["learning_cycles"] += 1
        self.learning_metrics["accuracy"] = self.calculate_prediction_accuracy()
        
        self.last_update = datetime.now()
        self.save_model_state()
        
        self.logger.info(f"Learning cycle completed. Accuracy: {self.learning_metrics['accuracy']:.3f}")
    
    def identify_patterns(self, experiences: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Identify recurring patterns in market data and outcomes"""
        patterns = {
            "successful_conditions": [],
            "failure_conditions": [],
            "market_correlations": {}
        }
        
        # Analyze successful trades
        successful_trades = [exp for exp in experiences if exp["outcome"] > 0]
        failed_trades = [exp for exp in experiences if exp["outcome"] <= 0]
        
        if successful_trades:
            # Find common features in successful trades
            success_features = [exp["features"] for exp in successful_trades]
            if success_features and success_features[0]:
                success_mean = [sum(feature[i] for feature in success_features) / len(success_features) 
                              for i in range(len(success_features[0]))]
                patterns["successful_conditions"] = success_mean
        
        if failed_trades:
            # Find common features in failed trades
            failure_features = [exp["features"] for exp in failed_trades]
            if failure_features and failure_features[0]:
                failure_mean = [sum(feature[i] for feature in failure_features) / len(failure_features) 
                              for i in range(len(failure_features[0]))]
                patterns["failure_conditions"] = failure_mean
        
        return patterns
    
    def update_market_patterns(self, new_patterns: Dict[str, Any]):
        """Update stored market patterns with new findings"""
        timestamp = datetime.now().isoformat()
        
        if "market_patterns" not in self.market_patterns:
            self.market_patterns["market_patterns"] = []
        
        pattern_entry = {
            "timestamp": timestamp,
            "patterns": new_patterns,
            "confidence": self.calculate_pattern_confidence(new_patterns)
        }
        
        self.market_patterns["market_patterns"].append(pattern_entry)
        
        # Keep only recent patterns
        if len(self.market_patterns["market_patterns"]) > 100:
            self.market_patterns["market_patterns"] = self.market_patterns["market_patterns"][-100:]
    
    def calculate_pattern_confidence(self, patterns: Dict[str, Any]) -> float:
        """Calculate confidence score for identified patterns"""
        # Simple confidence based on data availability
        confidence = 0.5
        
        if patterns.get("successful_conditions"):
            confidence += 0.2
        
        if patterns.get("failure_conditions"):
            confidence += 0.2
        
        if patterns.get("market_correlations"):
            confidence += 0.1
        
        return min(confidence, 1.0)
    
    def update_strategy_weights(self, experiences: List[Dict[str, Any]]):
        """Update strategy weights based on recent performance"""
        strategy_performance = {}
        
        for exp in experiences:
            strategy = exp.get("metadata", {}).get("strategy", "default")
            if strategy not in strategy_performance:
                strategy_performance[strategy] = {"outcomes": [], "count": 0}
            
            strategy_performance[strategy]["outcomes"].append(exp["outcome"])
            strategy_performance[strategy]["count"] += 1
        
        # Update weights based on performance
        for strategy, perf in strategy_performance.items():
            if perf["count"] > 0:
                avg_outcome = sum(perf["outcomes"]) / len(perf["outcomes"])
                success_rate = len([x for x in perf["outcomes"] if x > 0]) / perf["count"]
                
                # Calculate new weight (higher for better performing strategies)
                new_weight = (success_rate * 0.7) + (max(0, avg_outcome) * 0.3)
                self.strategy_weights[strategy] = new_weight
        
        # Normalize weights
        if self.strategy_weights:
            total_weight = sum(self.strategy_weights.values())
            if total_weight > 0:
                for strategy in self.strategy_weights:
                    self.strategy_weights[strategy] /= total_weight
    
    def detect_market_regime(self, experiences: List[Dict[str, Any]]):
        """Detect current market regime based on recent data"""
        if not experiences:
            return
        
        # Analyze price movements
        price_changes = []
        volatilities = []
        
        for exp in experiences:
            market_data = exp["market_data"]
            if "price_change" in market_data:
                price_changes.append(market_data["price_change"])
            if "volatility" in market_data:
                volatilities.append(market_data["volatility"])
        
        if price_changes:
            # Trend detection
            avg_change = sum(price_changes) / len(price_changes)
            trend_strength = abs(avg_change)
            
            if trend_strength > 0.01:  # Strong trend
                if avg_change > 0:
                    self.market_regimes["trending"]["up"] += 0.1
                    self.market_regimes["trending"]["down"] *= 0.9
                    self.market_regimes["current_regime"] = "trending_up"
                else:
                    self.market_regimes["trending"]["down"] += 0.1
                    self.market_regimes["trending"]["up"] *= 0.9
                    self.market_regimes["current_regime"] = "trending_down"
            else:  # Ranging market
                self.market_regimes["ranging"] += 0.1
                self.market_regimes["current_regime"] = "ranging"
        
        if volatilities and sum(volatilities) / len(volatilities) > 0.03:  # High volatility
            self.market_regimes["volatile"] += 0.1
            self.market_regimes["current_regime"] = "volatile"
        
        # Decay old regime weights
        for regime in self.market_regimes:
            if isinstance(self.market_regimes[regime], (int, float)):
                self.market_regimes[regime] *= 0.95
    
    def update_model_parameters(self, experiences: List[Dict[str, Any]]):
        """Update internal model parameters based on learning"""
        if not experiences:
            return
        
        # Simple parameter updates based on recent performance
        recent_outcomes = [exp["outcome"] for exp in experiences[-50:]]  # Last 50 outcomes
        
        if recent_outcomes:
            avg_outcome = sum(recent_outcomes) / len(recent_outcomes)
            
            # Adjust learning rate based on performance
            if avg_outcome > 0:
                self.learning_rate = min(self.learning_rate * 1.05, 0.1)  # Increase if doing well
            else:
                self.learning_rate = max(self.learning_rate * 0.95, 0.001)  # Decrease if doing poorly
            
            # Update improvement rate
            if len(self.performance_history) > 0:
                prev_avg = sum(self.performance_history[-50:]) / len(self.performance_history[-50:]) if len(self.performance_history) >= 50 else 0
                self.learning_metrics["improvement_rate"] = avg_outcome - prev_avg
        
        self.performance_history.extend(recent_outcomes)
        
        # Keep performance history manageable
        if len(self.performance_history) > 1000:
            self.performance_history = self.performance_history[-1000:]
    
    def calculate_prediction_accuracy(self) -> float:
        """Calculate prediction accuracy based on recent performance"""
        if len(self.performance_history) < 10:
            return 0.5  # Default accuracy
        
        recent_performance = self.performance_history[-100:]
        positive_outcomes = len([x for x in recent_performance if x > 0])
        
        return positive_outcomes / len(recent_performance)
    
    def get_strategy_recommendation(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Get strategy recommendation based on learned patterns"""
        features = self.extract_features(market_data)
        
        # Find best matching pattern
        best_strategy = "default"
        confidence = 0.5
        
        if self.strategy_weights:
            # Use weighted strategy selection
            best_strategy = max(self.strategy_weights, key=self.strategy_weights.get)
            confidence = self.strategy_weights[best_strategy]
        
        return {
            "recommended_strategy": best_strategy,
            "confidence": confidence,
            "market_regime": self.market_regimes["current_regime"],
            "learning_accuracy": self.learning_metrics["accuracy"]
        }
    
    def save_model_state(self):
        """Save current model state to disk"""
        model_state = {
            "model_version": self.model_version,
            "last_update": self.last_update.isoformat() if self.last_update else None,
            "learning_metrics": self.learning_metrics,
            "strategy_weights": self.strategy_weights,
            "market_regimes": self.market_regimes,
            "learning_rate": self.learning_rate,
            "config": self.config
        }
        
        state_file = self.data_path / "model_state.json"
        with open(state_file, 'w') as f:
            json.dump(model_state, f, indent=2)
    
    def load_model_state(self):
        """Load model state from disk"""
        state_file = self.data_path / "model_state.json"
        
        if state_file.exists():
            try:
                with open(state_file, 'r') as f:
                    model_state = json.load(f)
                
                self.model_version = model_state.get("model_version", 1)
                self.learning_metrics = model_state.get("learning_metrics", self.learning_metrics)
                self.strategy_weights = model_state.get("strategy_weights", {})
                self.market_regimes = model_state.get("market_regimes", self.market_regimes)
                self.learning_rate = model_state.get("learning_rate", self.learning_rate)
                
                if model_state.get("last_update"):
                    self.last_update = datetime.fromisoformat(model_state["last_update"])
                
                self.logger.info(f"Loaded model state version {self.model_version}")
                
            except Exception as e:
                self.logger.error(f"Error loading model state: {str(e)}")
    
    def get_learning_status(self) -> Dict[str, Any]:
        """Get current learning system status"""
        return {
            "model_version": self.model_version,
            "last_update": self.last_update.isoformat() if self.last_update else None,
            "learning_metrics": self.learning_metrics,
            "memory_buffer_size": len(self.memory_buffer),
            "strategy_weights": self.strategy_weights,
            "current_market_regime": self.market_regimes["current_regime"],
            "learning_rate": self.learning_rate
        }