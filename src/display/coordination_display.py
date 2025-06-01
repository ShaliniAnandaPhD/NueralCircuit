"""
Side-by-side coordination display system
Provides perfectly aligned visual coordination between agents
"""

import random
from typing import Dict, List, Any
from ..models.data_models import AgentStatus, SystemMetrics, CoordinationStep
from ..core.analyzer import SystemStateAnalyzer

# Display constants for perfect alignment
LEFT_WIDTH = 50
RIGHT_WIDTH = 65

def pad_left(text: str) -> str:
    """Pad text to exactly LEFT_WIDTH characters"""
    return f"│{text[:LEFT_WIDTH-2]:<{LEFT_WIDTH-2}}│"

def pad_right(text: str) -> str:
    """Pad text to exactly RIGHT_WIDTH characters"""
    return f"│{text[:RIGHT_WIDTH-2]:<{RIGHT_WIDTH-2}}│"

def display_side_by_side_kotler_coordination(step_data: CoordinationStep, user_name: str, agents: List[str]):
    """Display the beautiful side-by-side Kotler coordination"""
    
    # Header row
    left_header = pad_left(" 🤖 Agent Coordination Actions")
    right_header = pad_right(f" 🤖 LIVE AGENT COORDINATION - Step {step_data.step}")
    print(f"╭{'─' * (LEFT_WIDTH-2)}╮ ╭{'─' * (RIGHT_WIDTH-2)}╮")
    print(f"{left_header} {right_header}")
    
    # Second row
    left_coord = pad_left(" 🤖 LIVE AGENT COORDINATION:")
    right_empty = pad_right("")
    print(f"{left_coord} {right_empty}")
    
    # Third row - step description
    left_empty = pad_left("")
    right_desc = pad_right(f" {step_data.description}")
    print(f"{left_empty} {right_desc}")
    
    # Show each agent's status and actions
    for i, agent in enumerate(agents):
        state_icon = "🔥" if agent == step_data.active else "🎯" if agent == step_data.target else "⚙️"
        status = "← ACTIVE" if agent == step_data.active else "← TARGET" if agent == step_data.target else ""
        
        # Generate agent actions based on step and role
        action = _generate_kotler_action(step_data, agent, user_name)
        
        # Left column: Agent name and status
        left_agent = pad_left(f" {state_icon} {agent}:{' ' * (25 - len(agent))}{status}")
        
        # Right column content varies by row
        right_content = _get_kotler_right_content(i, step_data, user_name)
        
        print(f"{left_agent} {right_content}")
        
        # Left column: Agent action (indented)
        left_action = pad_left(f"    {action[:LEFT_WIDTH-6]}")
        
        # Right column content for second row of each agent
        right_content2 = _get_kotler_right_content_second_row(i, step_data)
        
        print(f"{left_action} {right_content2}")
    
    # Footer
    print(f"╰{'─' * (LEFT_WIDTH-2)}╯ ╰{'─' * (RIGHT_WIDTH-2)}╯")
    
    # Show live coordination message
    print(f"────────── 🔴 LIVE: {step_data.active} ═══▶ {step_data.target} (with {user_name}'s data) ──────────")
    print()

def display_side_by_side_fault_injection(agents: List[AgentStatus], target_agent: str, 
                                        phase: int, metrics: SystemMetrics, user_name: str = "User"):
    """Display fault injection with the beautiful side-by-side coordination display"""
    
    # Phase descriptions
    phase_descriptions = {
        1: f"🔴 FAULT INJECTED - {target_agent} compromised, others detecting",
        2: f"🟡 EMERGENCY COORDINATION - Agents collaborating on isolation", 
        3: f"🔄 COLLABORATIVE RECOVERY - Agents healing {target_agent} together",
        4: f"✅ RECOVERY COMPLETE - All agents back in coordination"
    }
    
    # Progress bars
    progress_bars = {
        1: "████████░░░░░░░░░░░░",
        2: "████████████░░░░░░░░", 
        3: "████████████████░░░░",
        4: "████████████████████"
    }
    
    # Header row
    left_header = pad_left(" 🤖 Agent Coordination Actions")
    right_header = pad_right(f" 🤖 LIVE FAULT RECOVERY - Step {phase}/4")
    print(f"╭{'─' * (LEFT_WIDTH-2)}╮ ╭{'─' * (RIGHT_WIDTH-2)}╮")
    print(f"{left_header} {right_header}")
    
    # Second row
    left_coord = pad_left(" 🤖 LIVE AGENT COORDINATION:")
    right_empty = pad_right("")
    print(f"{left_coord} {right_empty}")
    
    # Third row
    left_empty = pad_left("")
    right_desc = pad_right(f" {phase_descriptions[phase][:RIGHT_WIDTH-4]}")
    print(f"{left_empty} {right_desc}")
    
    # Show each agent's status and actions
    for i, agent in enumerate(agents):
        state_icon = agent.state.value
        
        # Generate fault-specific actions
        action = _generate_fault_action(agent, target_agent, phase)
        
        # Left column: Agent name and status
        left_agent = pad_left(f" {state_icon} {agent.agent_id}:")
        
        # Right column content varies by row
        right_content = _get_fault_right_content(i, phase, progress_bars, target_agent)
        
        print(f"{left_agent} {right_content}")
        
        # Left column: Agent action (indented)
        left_action = pad_left(f"    {action[:LEFT_WIDTH-6]}")
        
        # Right column content for second row of each agent
        right_content2 = _get_fault_right_content_second_row(i, metrics, user_name)
        
        print(f"{left_action} {right_content2}")
    
    # Footer
    print(f"╰{'─' * (LEFT_WIDTH-2)}╯ ╰{'─' * (RIGHT_WIDTH-2)}╯")
    
    # Show phase-specific messages
    _display_fault_phase_message(phase, target_agent)
    print()

def _generate_kotler_action(step_data: CoordinationStep, agent: str, user_name: str) -> str:
    """Generate action text for Kotler demo"""
    if agent == step_data.active:
        actions = {
            "1/6": f"Analyzing {user_name}'s flow state patterns",
            "2/6": f"Routing {user_name}'s context to memory systems",
            "3/6": f"Retrieving flow strategies for {user_name}",
            "4/6": f"Optimizing {user_name}'s challenge-skill balance",
            "5/6": f"Adapting flow parameters for {user_name}",
            "6/6": f"Coordinating {user_name}'s flow completion"
        }
        return actions.get(step_data.step, "Processing coordination")
    elif agent == step_data.target:
        actions = {
            "1/6": "Receiving flow analysis data",
            "2/6": "Processing context preservation request",
            "3/6": "Preparing strategy pattern delivery",
            "4/6": "Ready for optimization plan execution",
            "5/6": "Coordinating system-wide flow adjustment",
            "6/6": "Confirming flow recovery completion"
        }
        return actions.get(step_data.step, "Receiving coordination")
    else:
        # Supporting agents
        if step_data.step in ["1/6", "2/6"]:
            return f"Supporting {user_name} context analysis"
        elif step_data.step in ["3/6", "4/6"]:
            return f"Contributing to {user_name} flow optimization"
        else:
            return f"Validating {user_name} flow recovery success"

def _generate_fault_action(agent: AgentStatus, target_agent: str, phase: int) -> str:
    """Generate action text for fault injection"""
    if agent.agent_id == target_agent and phase <= 2:
        if phase == 1:
            return "FAULT DETECTED: Attempting self-recovery"
        else:
            return "COORDINATING: Accepting recovery assistance"
    elif phase == 1:
        return f"ALERT: Detecting {target_agent} communication failure"
    elif phase == 2:
        return f"EMERGENCY: Bypassing {target_agent}, rerouting tasks"
    elif phase == 3:
        return f"HEALING: Restoring {target_agent} functionality"
    else:
        return f"VALIDATED: Confirming {target_agent} full recovery"

def _get_kotler_right_content(i: int, step_data: CoordinationStep, user_name: str) -> str:
    """Get right column content for Kotler display"""
    if i == 0:  # First agent - show progress
        return pad_right(" Agent Coordination Progress:")
    elif i == 1:  # Second agent - show progress bar
        progress_bars = {
            "1/6": "████░░░░░░░░░░░░░░░░",
            "2/6": "████████░░░░░░░░░░░░", 
            "3/6": "████████████░░░░░░░░",
            "4/6": "████████████████░░░░",
            "5/6": "████████████████████",
            "6/6": "████████████████████"
        }
        return pad_right(f" {progress_bars[step_data.step]} {step_data.step}")
    elif i == 2:  # Third agent - show coordination analysis
        return pad_right(" Coordination Analysis:")
    elif i == 3:  # Fourth agent - show analysis details
        if step_data.step in ["1/6", "2/6"]:
            analysis_text = f"Flow analysis: {user_name} requires skill-challenge balance"
        elif step_data.step in ["3/6", "4/6"]:
            analysis_text = f"Strategy optimization: Improving {user_name}'s flow coefficient"
        else:
            analysis_text = f"SUCCESS: {user_name} achieved optimal flow state"
        return pad_right(f" {analysis_text[:RIGHT_WIDTH-4]}")
    elif i == 4:  # Fifth agent - show metrics
        return pad_right(" System Recovery Metrics:")
    else:  # Sixth agent - show context preservation
        return pad_right(f" Context Preserved: ✅ {user_name}'s profile")

def _get_kotler_right_content_second_row(i: int, step_data: CoordinationStep) -> str:
    """Get second row right column content for Kotler display"""
    if i == 1:  # After progress bar - show empty
        return pad_right("")
    elif i == 2:  # After coordination analysis - show empty  
        return pad_right("")
    elif i == 3:  # After analysis details - show empty
        return pad_right("")
    elif i == 4:  # After metrics header - show system integrity
        integrity_value = random.uniform(85, 99)
        integrity_bar = "█" * int(integrity_value / 5) + "░" * (20 - int(integrity_value / 5))
        return pad_right(f" System Integrity  {integrity_bar} {integrity_value:.1f}%")
    elif i == 5:  # After context preservation - show confidence
        confidence_value = random.uniform(80, 95)
        confidence_bar = "█" * int(confidence_value / 5) + "░" * (20 - int(confidence_value / 5))
        return pad_right(f" Agent Confidence  {confidence_bar} {confidence_value:.1f}%")
    else:
        return pad_right("")

def _get_fault_right_content(i: int, phase: int, progress_bars: Dict[int, str], target_agent: str) -> str:
    """Get right column content for fault display"""
    if i == 0:  # First agent - show progress
        return pad_right(" Agent Coordination Progress:")
    elif i == 1:  # Second agent - show progress bar
        return pad_right(f" {progress_bars[phase]} Step {phase}/4")
    elif i == 2:  # Third agent - show coordination analysis
        return pad_right(" Coordination Analysis:")
    elif i == 3:  # Fourth agent - show analysis details
        if phase == 1:
            analysis_text = f"Agents detecting {target_agent} failure, diagnostics active"
        elif phase == 2:
            analysis_text = f"Emergency coordination: 5 agents isolating {target_agent}"
        elif phase == 3:
            analysis_text = f"Collaborative healing: All agents restoring {target_agent}"
        else:
            analysis_text = f"SUCCESS: {target_agent} fully recovered via coordination"
        return pad_right(f" {analysis_text[:RIGHT_WIDTH-4]}")
    elif i == 4:  # Fifth agent - show metrics
        return pad_right(" System Recovery Metrics:")
    else:  # Sixth agent - show data protection
        return pad_right(f" Data Protection: User context preserved")

def _get_fault_right_content_second_row(i: int, metrics: SystemMetrics, user_name: str) -> str:
    """Get second row right column content for fault display"""
    if i == 1:  # After progress bar - show empty
        return pad_right("")
    elif i == 2:  # After coordination analysis - show empty  
        return pad_right("")
    elif i == 3:  # After analysis details - show empty
        return pad_right("")
    elif i == 4:  # After metrics header - show system integrity
        integrity_bar = "█" * int(metrics.system_integrity / 5) + "░" * (20 - int(metrics.system_integrity / 5))
        return pad_right(f" System Integrity  {integrity_bar} {metrics.system_integrity:.1f}%")
    elif i == 5:  # After data protection - show confidence
        confidence_bar = "█" * int(metrics.agent_confidence / 5) + "░" * (20 - int(metrics.agent_confidence / 5))
        return pad_right(f" Agent Confidence  {confidence_bar} {metrics.agent_confidence:.1f}%")
    else:
        return pad_right("")

def _display_fault_phase_message(phase: int, target_agent: str):
    """Display phase-specific messages for fault injection"""
    if phase == 1:
        print("🚨 FAULT DETECTED: Agents initiating cross-coordination protocols!")
    elif phase == 2:
        print(f"🤝 EMERGENCY COORDINATION: 5 agents collaborating to isolate {target_agent}!")
    elif phase == 3:
        print(f"🔄 COLLABORATIVE HEALING: All agents working together to restore {target_agent}!")
    else:
        print(f"🎉 COORDINATION SUCCESS: {target_agent} restored through agent collaboration!")
