"""
NeuroCircuit: Main Entry Point
Complete Neural Coordination System with Agent-Based Architecture
"""

import sys
from src.core.system import NeuroCircuitSystem
from src.display.architecture import display_architecture
from src.demos.kotler_demo import run_kotler_demo
from src.demos.fault_injection import run_fault_injection
from src.demos.health_dashboard import run_health_dashboard
from src.demos.comprehensive_test import test_all_agents
from src.utils.colors import Colors

def main():
    """Main entry point"""
    c = Colors
    
    if len(sys.argv) < 2:
        print(f"{c.BOLD}{c.BRIGHT_CYAN}NeuroCircuit: Complete Neural Coordination System
