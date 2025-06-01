"""
NeuroCircuitSystem: Main system class that coordinates all components
Manages agents, logging, and system-wide operations
"""

import random
import datetime
from typing import List, Optional, Dict, Any
from ..models.data_models import SystemMetrics, AgentStatus, AgentState
from ..core.logger import JSONLogger
from ..core.analyzer import SystemStateAnalyzer

class NeuroCircuitSystem:
    """Main system class for NeuroCircuit coordination"""
    
    def __init__(self, log_dir: str = "neurocircuit_logs"):
        """Initialize the NeuroCircuit system"""
        self.agents = [
            "CognitiveDetector",
            "NeuralBus", 
            "MemoryController",
            "DecisionEngine",
            "AdaptationController",
            "CoordinationHub"
        ]
        self.last_demo_data = None
        self.logger = JSONLogger(log_dir)
        self.analyzer = SystemStateAnalyzer()
    
    def get_agent_info(self) -> Dict[str, Dict[str, Any]]:
        """Get detailed information about all agents"""
        return {
            "CognitiveDetector": {
                "icon": "🧠", 
                "role": "Flow Analysis & Pattern Recognition",
                "primary_function": "Analyzes user flow states and cognitive patterns",
                "key_capabilities": [
                    "Challenge-skill ratio analysis",
                    "Flow coefficient calculation", 
                    "Attention focus measurement",
                    "Stress level detection",
                    "Intrinsic motivation assessment"
                ],
                "coordination_role": "Circuit input node - initiates all flow analysis"
            },
            "NeuralBus": {
                "icon": "🚀", 
                "role": "Message Routing & Load Balancing",
                "primary_function": "Routes messages between agents with fault tolerance",
                "key_capabilities": [
                    "Priority-based message routing",
                    "Load balancing across agents",
                    "Fault-tolerant communication",
                    "Context preservation",
                    "Emergency bypass routing"
                ],
                "coordination_role": "Circuit router - manages all inter-agent communication"
            },
            "MemoryController": {
                "icon": "💾", 
                "role": "Multi-Layer Memory Management",
                "primary_function": "Manages episodic, semantic, and working memory",
                "key_capabilities": [
                    "Flow strategy pattern storage",
                    "User context persistence",
                    "Memory consolidation",
                    "Retrieval optimization",
                    "Memory decay management"
                ],
                "coordination_role": "Circuit memory bank - stores and retrieves all system knowledge"
            },
            "DecisionEngine": {
                "icon": "⚡", 
                "role": "Flow Optimization & Strategy Planning",
                "primary_function": "Makes decisions for optimal flow state achievement",
                "key_capabilities": [
                    "Challenge-skill rebalancing",
                    "Intervention strategy selection",
                    "Confidence estimation",
                    "Risk assessment",
                    "Optimization plan generation"
                ],
                "coordination_role": "Circuit processor - executes all optimization decisions"
            },
            "AdaptationController": {
                "icon": "🔄", 
                "role": "Dynamic Parameter Adaptation",
                "primary_function": "Adapts system parameters based on real-time feedback",
                "key_capabilities": [
                    "Real-time parameter tuning",
                    "Learning rate adjustment",
                    "Feedback loop optimization",
                    "Personalization engine",
                    "Progressive adaptation"
                ],
                "coordination_role": "Circuit adapter - dynamically adjusts all system responses"
            },
            "CoordinationHub": {
                "icon": "🎯", 
                "role": "Cross-Module Orchestration",
                "primary_function": "Orchestrates overall system coordination and validation",
                "key_capabilities": [
                    "System-wide coordination",
                    "Conflict resolution",
                    "Performance validation",
                    "Recovery orchestration",
                    "Success confirmation"
                ],
                "coordination_role": "Circuit controller - manages entire system orchestration"
            }
        }
    
    def generate_baseline_metrics(self) -> SystemMetrics:
        """Generate realistic baseline system metrics"""
        return SystemMetrics(
            system_integrity=random.uniform(97.0, 99.5),
            agent_confidence=random.uniform(85.0, 95.0),
            message_throughput=random.uniform(45.0, 55.0),
            response_latency=random.uniform(100, 300),
            error_rate=random.uniform(0.001, 0.01),
            coordination_efficiency=random.uniform(88.0, 96.0),
            timestamp=datetime.datetime.now().isoformat()
        )
    
    def generate_agent_statuses(self, fault_target: Optional[str] = None, 
                               recovery_phase: int = 0) -> List[AgentStatus]:
        """Generate agent statuses based on system state"""
        statuses = []
        
        for agent in self.agents:
            # Determine agent state based on fault and recovery phase
            if fault_target == agent and recovery_phase <= 2:
                state = AgentState.CRITICAL if recovery_phase == 1 else AgentState.EMERGENCY
                confidence = random.uniform(20.0, 40.0)
                error_count = random.randint(5, 15)
                coordination_score = random.uniform(30.0, 50.0)
            elif fault_target and recovery_phase in [1, 2]:
                state = AgentState.WARNING if recovery_phase == 1 else AgentState.EMERGENCY
                confidence = random.uniform(70.0, 85.0)
                error_count = random.randint(1, 3)
                coordination_score = random.uniform(75.0, 90.0)
            elif recovery_phase == 3:
                state = AgentState.RECOVERY
                confidence = random.uniform(80.0, 95.0)
                error_count = random.randint(0, 2)
                coordination_score = random.uniform(85.0, 95.0)
            else:
                state = AgentState.NORMAL if recovery_phase != 4 else AgentState.VALIDATED
                confidence = random.uniform(85.0, 98.0)
                error_count = random.randint(0, 1)
                coordination_score = random.uniform(90.0, 98.0)
            
            statuses.append(AgentStatus(
                agent_id=agent,
                state=state,
                confidence=confidence,
                active_tasks=[f"task_{i}" for i in range(random.randint(2, 6))],
                last_response_time=random.uniform(50, 200),
                error_count=error_count,
                coordination_score=coordination_score,
                timestamp=datetime.datetime.now().isoformat()
            ))
        
