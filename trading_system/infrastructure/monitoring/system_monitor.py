"""
🌙 Moon Dev's System Monitor
Comprehensive system monitoring with real-time metrics and alerting
"""

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    # Create mock psutil for systems without it
    class MockPsutil:
        @staticmethod
        def cpu_percent(interval=1):
            return 50.0
        @staticmethod
        def virtual_memory():
            class MockMemory:
                def __init__(self):
                    self.total = 8 * 1024 * 1024 * 1024  # 8GB
                    self.available = 4 * 1024 * 1024 * 1024  # 4GB
                    self.used = 4 * 1024 * 1024 * 1024  # 4GB
                    self.percent = 50.0
            return MockMemory()
        @staticmethod
        def swap_memory():
            class MockSwap:
                def __init__(self):
                    self.total = 2 * 1024 * 1024 * 1024  # 2GB
                    self.used = 0
                    self.percent = 0.0
            return MockSwap()
        @staticmethod
        def disk_usage(path):
            class MockDisk:
                def __init__(self):
                    self.total = 100 * 1024 * 1024 * 1024  # 100GB
                    self.used = 50 * 1024 * 1024 * 1024  # 50GB
                    self.free = 50 * 1024 * 1024 * 1024  # 50GB
                    self.percent = 50.0
            return MockDisk()
        @staticmethod
        def disk_io_counters():
            class MockDiskIO:
                def __init__(self):
                    self.read_bytes = 1000000
                    self.write_bytes = 500000
            return MockDiskIO()
        @staticmethod
        def net_io_counters():
            class MockNetIO:
                def __init__(self):
                    self.bytes_sent = 1000000
                    self.bytes_recv = 2000000
                    self.packets_sent = 1000
                    self.packets_recv = 2000
                    self.errin = 0
                    self.errout = 0
            return MockNetIO()
        @staticmethod
        def cpu_count():
            return 4
        @staticmethod
        def cpu_freq():
            class MockFreq:
                def __init__(self):
                    self.current = 2400.0
            return MockFreq()
        @staticmethod
        def pids():
            return list(range(100))  # Mock 100 processes
        @staticmethod
        def getloadavg():
            return [0.5, 0.3, 0.2]
        @staticmethod
        def process_iter(attrs=None):
            return []  # No processes for mock
    
    psutil = MockPsutil()
import time
import json
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import logging

class SystemMonitor:
    """
    Comprehensive system monitoring for the trading system:
    - CPU, Memory, Disk, Network usage
    - Application performance metrics
    - Trading system health monitoring
    - Real-time alerting
    - Historical metrics storage
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        
        # Setup logging
        self.logger = logging.getLogger("system_monitor")
        
        # Monitoring parameters
        self.monitoring_interval = self.config.get("monitoring_interval", 30)  # seconds
        self.retention_days = self.config.get("retention_days", 30)
        self.alert_thresholds = self.config.get("alert_thresholds", {
            "cpu_percent": 80,
            "memory_percent": 85,
            "disk_percent": 90,
            "network_errors": 100,
            "response_time_ms": 5000
        })
        
        # Data storage
        self.data_path = Path("trading_system/data/monitoring")
        self.data_path.mkdir(parents=True, exist_ok=True)
        
        # Monitoring state
        self.is_monitoring = False
        self.monitor_thread = None
        self.metrics_history = []
        self.alerts = []
        
        # System baseline
        self.baseline_metrics = None
        self.establish_baseline()
        
    def establish_baseline(self):
        """Establish baseline system metrics"""
        try:
            self.baseline_metrics = {
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent,
                "network_io": psutil.net_io_counters(),
                "process_count": len(psutil.pids()),
                "timestamp": datetime.now().isoformat()
            }
            self.logger.info("System baseline established")
        except Exception as e:
            self.logger.error(f"Error establishing baseline: {str(e)}")
    
    def collect_system_metrics(self) -> Dict[str, Any]:
        """Collect comprehensive system metrics"""
        try:
            # CPU metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_count = psutil.cpu_count()
            cpu_freq = psutil.cpu_freq()
            
            # Memory metrics
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            # Disk metrics
            disk_usage = psutil.disk_usage('/')
            disk_io = psutil.disk_io_counters()
            
            # Network metrics
            network_io = psutil.net_io_counters()
            
            # Process metrics
            process_count = len(psutil.pids())
            
            # System load
            try:
                load_avg = psutil.getloadavg()
            except AttributeError:
                load_avg = [0, 0, 0]  # Windows doesn't have load average
            
            metrics = {
                "timestamp": datetime.now().isoformat(),
                "cpu": {
                    "percent": cpu_percent,
                    "count": cpu_count,
                    "frequency": cpu_freq.current if cpu_freq else 0
                },
                "memory": {
                    "total": memory.total,
                    "available": memory.available,
                    "used": memory.used,
                    "percent": memory.percent,
                    "swap_total": swap.total,
                    "swap_used": swap.used,
                    "swap_percent": swap.percent
                },
                "disk": {
                    "total": disk_usage.total,
                    "used": disk_usage.used,
                    "free": disk_usage.free,
                    "percent": disk_usage.percent,
                    "read_bytes": disk_io.read_bytes if disk_io else 0,
                    "write_bytes": disk_io.write_bytes if disk_io else 0
                },
                "network": {
                    "bytes_sent": network_io.bytes_sent,
                    "bytes_received": network_io.bytes_recv,
                    "packets_sent": network_io.packets_sent,
                    "packets_received": network_io.packets_recv,
                    "errors_in": network_io.errin,
                    "errors_out": network_io.errout
                },
                "system": {
                    "process_count": process_count,
                    "load_avg_1": load_avg[0],
                    "load_avg_5": load_avg[1],
                    "load_avg_15": load_avg[2]
                }
            }
            
            return metrics
            
        except Exception as e:
            self.logger.error(f"Error collecting system metrics: {str(e)}")
            return {}
    
    def collect_application_metrics(self) -> Dict[str, Any]:
        """Collect application-specific metrics"""
        try:
            # Find trading system processes
            trading_processes = []
            
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    if 'python' in proc.info['name'].lower():
                        # Check if it's part of our trading system
                        cmdline = proc.cmdline()
                        if any('trading' in arg.lower() or 'agent' in arg.lower() for arg in cmdline):
                            trading_processes.append({
                                "pid": proc.info['pid'],
                                "name": proc.info['name'],
                                "cpu_percent": proc.info['cpu_percent'],
                                "memory_percent": proc.info['memory_percent'],
                                "status": proc.status(),
                                "create_time": proc.create_time()
                            })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            app_metrics = {
                "timestamp": datetime.now().isoformat(),
                "trading_processes": trading_processes,
                "active_processes": len(trading_processes),
                "total_cpu_usage": sum(p["cpu_percent"] for p in trading_processes),
                "total_memory_usage": sum(p["memory_percent"] for p in trading_processes)
            }
            
            return app_metrics
            
        except Exception as e:
            self.logger.error(f"Error collecting application metrics: {str(e)}")
            return {}
    
    def check_alert_conditions(self, metrics: Dict[str, Any]):
        """Check if any alert conditions are met"""
        alerts_triggered = []
        
        try:
            # CPU alert
            if metrics.get("cpu", {}).get("percent", 0) > self.alert_thresholds["cpu_percent"]:
                alerts_triggered.append({
                    "type": "cpu_high",
                    "message": f"High CPU usage: {metrics['cpu']['percent']:.1f}%",
                    "severity": "warning",
                    "value": metrics['cpu']['percent'],
                    "threshold": self.alert_thresholds["cpu_percent"]
                })
            
            # Memory alert
            if metrics.get("memory", {}).get("percent", 0) > self.alert_thresholds["memory_percent"]:
                alerts_triggered.append({
                    "type": "memory_high",
                    "message": f"High memory usage: {metrics['memory']['percent']:.1f}%",
                    "severity": "warning",
                    "value": metrics['memory']['percent'],
                    "threshold": self.alert_thresholds["memory_percent"]
                })
            
            # Disk alert
            if metrics.get("disk", {}).get("percent", 0) > self.alert_thresholds["disk_percent"]:
                alerts_triggered.append({
                    "type": "disk_high",
                    "message": f"High disk usage: {metrics['disk']['percent']:.1f}%",
                    "severity": "critical",
                    "value": metrics['disk']['percent'],
                    "threshold": self.alert_thresholds["disk_percent"]
                })
            
            # Network errors alert
            network = metrics.get("network", {})
            total_errors = network.get("errors_in", 0) + network.get("errors_out", 0)
            if total_errors > self.alert_thresholds["network_errors"]:
                alerts_triggered.append({
                    "type": "network_errors",
                    "message": f"High network errors: {total_errors}",
                    "severity": "warning",
                    "value": total_errors,
                    "threshold": self.alert_thresholds["network_errors"]
                })
            
            # Add timestamp to alerts
            for alert in alerts_triggered:
                alert["timestamp"] = datetime.now().isoformat()
            
            self.alerts.extend(alerts_triggered)
            
            # Keep only recent alerts
            if len(self.alerts) > 1000:
                self.alerts = self.alerts[-1000:]
            
            # Log critical alerts
            for alert in alerts_triggered:
                if alert["severity"] == "critical":
                    self.logger.critical(alert["message"])
                elif alert["severity"] == "warning":
                    self.logger.warning(alert["message"])
                    
        except Exception as e:
            self.logger.error(f"Error checking alert conditions: {str(e)}")
    
    def save_metrics(self, metrics: Dict[str, Any]):
        """Save metrics to file"""
        try:
            # Save daily metrics file
            date_str = datetime.now().strftime("%Y%m%d")
            metrics_file = self.data_path / f"metrics_{date_str}.json"
            
            # Load existing data or create new
            if metrics_file.exists():
                with open(metrics_file, 'r') as f:
                    daily_metrics = json.load(f)
            else:
                daily_metrics = []
            
            daily_metrics.append(metrics)
            
            # Save updated data
            with open(metrics_file, 'w') as f:
                json.dump(daily_metrics, f, indent=2)
            
            # Clean up old files
            self.cleanup_old_metrics()
            
        except Exception as e:
            self.logger.error(f"Error saving metrics: {str(e)}")
    
    def cleanup_old_metrics(self):
        """Clean up metrics files older than retention period"""
        try:
            cutoff_date = datetime.now() - timedelta(days=self.retention_days)
            
            for metrics_file in self.data_path.glob("metrics_*.json"):
                try:
                    # Extract date from filename
                    date_str = metrics_file.stem.split("_")[1]
                    file_date = datetime.strptime(date_str, "%Y%m%d")
                    
                    if file_date < cutoff_date:
                        metrics_file.unlink()
                        self.logger.info(f"Deleted old metrics file: {metrics_file}")
                        
                except (ValueError, IndexError):
                    continue
                    
        except Exception as e:
            self.logger.error(f"Error cleaning up old metrics: {str(e)}")
    
    def monitoring_loop(self):
        """Main monitoring loop"""
        self.logger.info("System monitoring started")
        
        while self.is_monitoring:
            try:
                # Collect system metrics
                system_metrics = self.collect_system_metrics()
                app_metrics = self.collect_application_metrics()
                
                # Combine metrics
                combined_metrics = {
                    **system_metrics,
                    "application": app_metrics
                }
                
                # Check for alerts
                self.check_alert_conditions(system_metrics)
                
                # Save metrics
                self.save_metrics(combined_metrics)
                
                # Add to history
                self.metrics_history.append(combined_metrics)
                
                # Keep history manageable
                if len(self.metrics_history) > 1000:
                    self.metrics_history = self.metrics_history[-1000:]
                
                # Sleep until next collection
                time.sleep(self.monitoring_interval)
                
            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {str(e)}")
                time.sleep(self.monitoring_interval)
        
        self.logger.info("System monitoring stopped")
    
    def start_monitoring(self):
        """Start system monitoring in background thread"""
        if self.is_monitoring:
            self.logger.warning("Monitoring already started")
            return
        
        self.is_monitoring = True
        self.monitor_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
        self.monitor_thread.start()
        self.logger.info("System monitoring started in background")
    
    def stop_monitoring(self):
        """Stop system monitoring"""
        if not self.is_monitoring:
            self.logger.warning("Monitoring not running")
            return
        
        self.is_monitoring = False
        if self.monitor_thread and self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=10)
        
        self.logger.info("System monitoring stopped")
    
    def get_current_status(self) -> Dict[str, Any]:
        """Get current system status"""
        current_metrics = self.collect_system_metrics()
        app_metrics = self.collect_application_metrics()
        
        # Calculate changes from baseline
        changes = {}
        if self.baseline_metrics:
            changes = {
                "cpu_change": current_metrics.get("cpu", {}).get("percent", 0) - self.baseline_metrics.get("cpu_percent", 0),
                "memory_change": current_metrics.get("memory", {}).get("percent", 0) - self.baseline_metrics.get("memory_percent", 0),
                "disk_change": current_metrics.get("disk", {}).get("percent", 0) - self.baseline_metrics.get("disk_percent", 0)
            }
        
        return {
            "timestamp": datetime.now().isoformat(),
            "system_metrics": current_metrics,
            "application_metrics": app_metrics,
            "baseline_changes": changes,
            "recent_alerts": self.alerts[-10:] if self.alerts else [],
            "monitoring_active": self.is_monitoring,
            "uptime_hours": (datetime.now() - datetime.fromisoformat(self.baseline_metrics["timestamp"])).total_seconds() / 3600 if self.baseline_metrics else 0
        }
    
    def get_performance_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get performance summary for specified time period"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        # Filter recent metrics
        recent_metrics = [
            m for m in self.metrics_history 
            if datetime.fromisoformat(m["timestamp"]) > cutoff_time
        ]
        
        if not recent_metrics:
            return {"error": "No metrics available for specified period"}
        
        # Calculate averages
        avg_cpu = sum(m.get("cpu", {}).get("percent", 0) for m in recent_metrics) / len(recent_metrics)
        avg_memory = sum(m.get("memory", {}).get("percent", 0) for m in recent_metrics) / len(recent_metrics)
        avg_disk = sum(m.get("disk", {}).get("percent", 0) for m in recent_metrics) / len(recent_metrics)
        
        # Calculate peaks
        peak_cpu = max(m.get("cpu", {}).get("percent", 0) for m in recent_metrics)
        peak_memory = max(m.get("memory", {}).get("percent", 0) for m in recent_metrics)
        peak_disk = max(m.get("disk", {}).get("percent", 0) for m in recent_metrics)
        
        # Count alerts in period
        period_alerts = [
            a for a in self.alerts 
            if datetime.fromisoformat(a["timestamp"]) > cutoff_time
        ]
        
        return {
            "period_hours": hours,
            "metrics_count": len(recent_metrics),
            "averages": {
                "cpu_percent": avg_cpu,
                "memory_percent": avg_memory,
                "disk_percent": avg_disk
            },
            "peaks": {
                "cpu_percent": peak_cpu,
                "memory_percent": peak_memory,
                "disk_percent": peak_disk
            },
            "alerts": {
                "total": len(period_alerts),
                "by_type": {}
            }
        }