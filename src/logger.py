"""
Comprehensive logging system for NeuroCircuit
Provides both JSON files and JSONL streaming for all events
"""

import json
import os
import uuid
import datetime
from typing import Dict, List, Any
from ..models.data_models import SystemMetrics, AgentStatus, FaultEvent, RecoveryStep
from ..core.analyzer import SystemStateAnalyzer

class JSONLogger:
    """Comprehensive logging system with both JSON files and JSONL streaming"""
    
    def __init__(self, log_dir: str = "neurocircuit_logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.session_id = str(uuid.uuid4())[:8]
        self.session_start = datetime.datetime.now().isoformat()
        
        # Initialize JSONL stream file
        self.jsonl_file = self._create_session_file("events.jsonl")
        self._log_jsonl_event({
            "event_type": "session_start",
            "session_id": self.session_id,
            "timestamp": self.session_start
        })
        
    def _create_session_file(self, filename: str) -> str:
        """Create timestamped session file"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.log_dir, f"{timestamp}_{self.session_id}_{filename}")
    
    def _log_jsonl_event(self, event: Dict[str, Any]):
        """Append event to JSONL stream file"""
        with open(self.jsonl_file, 'a') as f:
            f.write(json.dumps(event) + '\n')
    
    def log_system_state(self, state_type: str, metrics: SystemMetrics, 
                        agents: List[AgentStatus], metadata: Dict[str, Any] = None) -> str:
        """Log complete system state to both JSON file and JSONL stream"""
        
        # Create JSON file
        filename = self._create_session_file(f"{state_type}_state.json")
        state_data = {
            "session_id": self.session_id,
            "state_type": state_type,
            "timestamp": datetime.datetime.now().isoformat(),
            "system_metrics": metrics.to_dict(),
            "agents": [agent.to_dict() for agent in agents],
            "metadata": metadata or {}
        }
        
        with open(filename, 'w') as f:
            json.dump(state_data, f, indent=2)
        
        # Add to JSONL stream
        self._log_jsonl_event({
            "event_type": "system_state",
            "session_id": self.session_id,
            "state_type": state_type,
            "timestamp": datetime.datetime.now().isoformat(),
            "health_score": SystemStateAnalyzer.calculate_health_score(metrics),
            "agent_count": len(agents),
            "metadata": metadata or {}
        })
        
        return filename
    
    def log_fault_event(self, fault: FaultEvent, recovery_steps: List[RecoveryStep]) -> str:
        """Log complete fault injection event to both JSON file and JSONL stream"""
        
        # Create JSON file
        filename = self._create_session_file("fault_event.json")
        event_data = {
            "session_id": self.session_id,
            "fault_event": fault.to_dict(),
            "recovery_process": [step.to_dict() for step in recovery_steps],
            "total_recovery_time": sum(step.duration_ms for step in recovery_steps),
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(event_data, f, indent=2)
        
        # Add to JSONL stream
        self._log_jsonl_event({
            "event_type": "fault_injection",
            "session_id": self.session_id,
            "fault_type": fault.fault_type.value,
            "target_agent": fault.target_agent,
            "severity": fault.severity,
            "recovery_steps": len(recovery_steps),
            "total_recovery_time_ms": sum(step.duration_ms for step in recovery_steps),
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return filename
    
    def log_kotler_demo(self, user_name: str, flow_data: Dict[str, Any]) -> str:
        """Log Kotler demo session"""
        filename = self._create_session_file("kotler_demo.json")
        demo_data = {
            "session_id": self.session_id,
            "user_name": user_name,
            "flow_data": flow_data,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(demo_data, f, indent=2)
        
        self._log_jsonl_event({
            "event_type": "kotler_demo_complete",
            "session_id": self.session_id,
            "user_name": user_name,
            "final_flow": flow_data.get('target_flow', 0),
            "effectiveness": flow_data.get('effectiveness', 0),
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return filename
    
    def log_coordination_sequence(self, sequence_type: str, steps: List[Dict[str, Any]], 
                                 user_context: Dict[str, Any] = None) -> str:
        """Log agent coordination sequence"""
        filename = self._create_session_file(f"{sequence_type}_coordination.json")
        sequence_data = {
            "session_id": self.session_id,
            "sequence_type": sequence_type,
            "steps": steps,
            "user_context": user_context or {},
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(sequence_data, f, indent=2)
        
        self._log_jsonl_event({
            "event_type": "coordination_sequence",
            "session_id": self.session_id,
            "sequence_type": sequence_type,
            "step_count": len(steps),
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return filename
    
    def finalize_session(self):
        """Close session with final JSONL event"""
        self._log_jsonl_event({
            "event_type": "session_end",
            "session_id": self.session_id,
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    def get_session_info(self) -> Dict[str, str]:
        """Get current session information"""
        return {
            "session_id": self.session_id,
            "session_start": self.session_start,
            "log_dir": self.log_dir,
            "jsonl_file": self.jsonl_file
        }
