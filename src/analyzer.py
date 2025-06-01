"""
System state analysis and health monitoring for NeuroCircuit
Provides health scoring, visual indicators, and comparative analysis
"""

from typing import Dict, Any
from ..models.data_models import SystemMetrics
from ..utils.colors import Colors

class SystemStateAnalyzer:
    """Analyzes system state and provides health metrics"""
    
    @staticmethod
    def calculate_health_score(metrics: SystemMetrics) -> float:
        """Calculate overall system health score (0-100)"""
        weights = {
            'system_integrity': 0.25,
            'agent_confidence': 0.20,
            'coordination_efficiency': 0.20,
            'message_throughput': 0.15,
            'response_latency': 0.10,
            'error_rate': 0.10
        }
        
        # Normalize latency and error rate (lower is better)
        normalized_latency = max(0, 100 - (metrics.response_latency / 10))
        normalized_error_rate = max(0, 100 - (metrics.error_rate * 100))
        
        score = (
            metrics.system_integrity * weights['system_integrity'] +
            metrics.agent_confidence * weights['agent_confidence'] +
            metrics.coordination_efficiency * weights['coordination_efficiency'] +
            metrics.message_throughput * weights['message_throughput'] +
            normalized_latency * weights['response_latency'] +
            normalized_error_rate * weights['error_rate']
        )
        
        return round(score, 2)
    
    @staticmethod
    def get_health_color(score: float) -> str:
        """Get color code based on health score"""
        c = Colors
        if score >= 95:
            return c.BRIGHT_GREEN
        elif score >= 85:
            return c.GREEN
        elif score >= 70:
            return c.YELLOW
        elif score >= 50:
            return c.BRIGHT_YELLOW
        else:
            return c.BRIGHT_RED
    
    @staticmethod
    def get_health_status(score: float) -> str:
        """Get textual health status"""
        if score >= 95:
            return "Excellent"
        elif score >= 85:
            return "Good"
        elif score >= 70:
            return "Fair"
        elif score >= 50:
            return "Poor"
        else:
            return "Critical"
    
    @staticmethod
    def create_visual_bar(value: float, max_value: float = 100, width: int = 20, 
                         show_percentage: bool = True) -> str:
        """Create a visual progress bar"""
        if max_value == 0:
            percentage = 0
        else:
            percentage = min(100, (value / max_value) * 100)
        
        filled = int((percentage / 100) * width)
        empty = width - filled
        
        bar = "█" * filled + "░" * empty
        
        if show_percentage:
            return f"{bar} {percentage:.1f}%"
        else:
            return bar
    
    @staticmethod
    def compare_states(before: SystemMetrics, after: SystemMetrics) -> Dict[str, Any]:
        """Compare before and after system states"""
        before_score = SystemStateAnalyzer.calculate_health_score(before)
        after_score = SystemStateAnalyzer.calculate_health_score(after)
        
        metrics_comparison = {}
        metric_fields = ['system_integrity', 'agent_confidence', 'coordination_efficiency', 
                        'message_throughput', 'response_latency', 'error_rate']
        
        for field in metric_fields:
            before_val = getattr(before, field)
            after_val = getattr(after, field)
            change = after_val - before_val
            change_percent = (change / before_val * 100) if before_val != 0 else 0
            
            metrics_comparison[field] = {
                'before': before_val,
                'after': after_val,
                'change': round(change, 3),
                'change_percent': round(change_percent, 2)
            }
        
        # Determine most impacted and best recovery metrics
        most_impacted = max(metrics_comparison.items(), 
                           key=lambda x: abs(x[1]['change_percent']))[0]
        
        best_recovery = max(metrics_comparison.items(),
                           key=lambda x: x[1]['change'] if 'latency' not in x[0] 
                           and 'error' not in x[0] else -x[1]['change'])[0]
        
        return {
            'overall_health': {
                'before_score': before_score,
                'after_score': after_score,
                'change': round(after_score - before_score, 2),
                'recovery_success': after_score >= (before_score * 0.95)
            },
            'metrics_comparison': metrics_comparison,
            'analysis_summary': {
                'most_impacted_metric': most_impacted,
                'best_recovery_metric': best_recovery,
                'resilience_rating': SystemStateAnalyzer._get_resilience_rating(before_score, after_score)
            }
        }
    
    @staticmethod
    def _get_resilience_rating(before_score: float, after_score: float) -> str:
        """Determine resilience rating based on recovery"""
        recovery_ratio = after_score / before_score if before_score > 0 else 1
        
        if recovery_ratio >= 0.98:
            return 'Excellent'
        elif recovery_ratio >= 0.95:
            return 'Good'
        elif recovery_ratio >= 0.90:
            return 'Adequate'
        else:
            return 'Poor'
    
    @staticmethod
    def analyze_agent_coordination(agents_before, agents_after) -> Dict[str, Any]:
        """Analyze changes in agent coordination"""
        coordination_analysis = {
            'agents_improved': 0,
            'agents_degraded': 0,
            'average_confidence_change': 0,
            'coordination_changes': []
        }
        
        if len(agents_before) != len(agents_after):
            return coordination_analysis
        
        confidence_changes = []
        
        for before, after in zip(agents_before, agents_after):
            if before.agent_id == after.agent_id:
                confidence_change = after.confidence - before.confidence
                confidence_changes.append(confidence_change)
                
                coordination_analysis['coordination_changes'].append({
                    'agent_id': before.agent_id,
                    'confidence_change': round(confidence_change, 2),
                    'state_before': before.state.value,
                    'state_after': after.state.value
                })
                
                if confidence_change > 0:
                    coordination_analysis['agents_improved'] += 1
                elif confidence_change < 0:
                    coordination_analysis['agents_degraded'] += 1
        
        if confidence_changes:
            coordination_analysis['average_confidence_change'] = round(
                sum(confidence_changes) / len(confidence_changes), 2
            )
        
        return coordination_analysis
