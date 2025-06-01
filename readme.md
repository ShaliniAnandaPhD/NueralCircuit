# NeuroCircuit: Complete Neural Coordination System


### Core Neural Coordination Components

```
🧠 CognitiveDetector    → Flow analysis & pattern recognition
                          • Challenge-skill ratio analysis
                          • Flow coefficient calculation
                          • Attention focus measurement
                          • Error handling: Input validation, fallback strategies

🚀 NeuralBus           → Message routing & load balancing  
                          • Priority-based message routing
                          • Dynamic load balancing
                          • Fault-tolerant communication
                          • Error handling: Message retry, circuit breaking

💾 MemoryController    → Multi-layer memory management
                          • Flow strategy pattern storage
                          • User context persistence
                          • Memory consolidation
                          • Error handling: Corruption detection, backup retrieval

⚡ DecisionEngine      → Flow optimization & strategy planning
                          • Challenge-skill rebalancing
                          • Intervention strategy selection
                          • Confidence estimation
                          • Error handling: Validation chains, fallback decisions

🔄 AdaptationController → Dynamic parameter adaptation
                          • Real-time parameter tuning
                          • Learning rate adjustment
                          • Feedback loop optimization
                          • Error handling: Parameter bounds, stability checks

🎯 CoordinationHub     → Cross-module orchestration
                          • System-wide coordination
                          • Conflict resolution
                          • Performance validation
                          • Error handling: Consensus protocols, recovery coordination
```

## 🚀 Quick Start with Error Handling

### Installation and Setup

```bash
# Clone the repository
git clone <repository-url>
cd neurocircuit

# Verify Python version (3.8+ required)
python --version

# Run setup to create directory structure
python setup.py

# Test installation
python main.py architecture
```

### Basic Usage with Error Recovery

```bash
# Display architecture (includes error handling examples)
python main.py architecture

# Run Kotler demo with comprehensive error checking
python main.py kotler-live-demo

# Test fault injection with recovery validation
python main.py fault-injection

# Monitor system health with real-time analysis
python main.py health-dashboard

# Test all agents systematically with error reporting
python main.py test-all-agents
```

## 📋 Comprehensive Command Reference

| Command | Purpose | Error Handling Features |
|---------|---------|------------------------|
| `architecture` | System design display | Input validation, graceful fallbacks |
| `kotler-live-demo` | Interactive flow optimization | User input validation, session recovery |
| `fault-injection` | Resilience testing | Target validation, recovery verification |
| `health-dashboard` | Real-time monitoring | Metric validation, display error recovery |
| `test-all-agents` | Systematic validation | Progress tracking, partial failure handling |

## 🔬 Advanced Log Analysis System

### Comprehensive Validation and Analysis

```bash
# Analyze specific session with detailed error checking
python test_logs.py <session_id> --detailed

# List all sessions with health status
python test_logs.py --list-sessions

# Validate file integrity with quality scoring
python test_logs.py <session_id> --validate-only

# Export analysis with error reporting
python test_logs.py <session_id> --output analysis.json

# Batch analysis with quality thresholds
python test_logs.py <session_id> --quality-threshold 80.0
```

### Log Analysis Features

- **📊 Quality Scoring**: 100-point system with error/warning deductions
- **🔍 Structure Validation**: JSON syntax, field completeness, type checking
- **📈 Health Progression**: Trend analysis with recovery detection
- **🤝 Coordination Analysis**: Agent interaction patterns and effectiveness
- **⏰ Timeline Reconstruction**: Chronological event sequencing with gap detection
- **🎯 Performance Benchmarks**: Comparison against established thresholds

## 📁 Detailed Project Structure

```
neurocircuit/
├── main.py                           # Entry point with comprehensive error handling
├── test_logs.py                      # Advanced log analysis with validation
├── setup.py                          # Environment setup with dependency checking
├── README.md                         # This comprehensive documentation
├── src/
│   ├── __init__.py                   # Package initialization with version info
│   ├── core/
│   │   ├── __init__.py              # Core module exports
│   │   ├── system.py                # Main system class with fault tolerance
│   │   ├── logger.py                # Dual JSON/JSONL logging with error recovery
│   │   └── analyzer.py              # Health analysis with validation
│   ├── models/
│   │   ├── __init__.py              # Model exports with type validation
│   │   └── data_models.py           # All data structures with validation
│   ├── display/
│   │   ├── __init__.py              # Display module exports
│   │   ├── architecture.py          # System architecture display
│   │   ├── coordination_display.py  # Side-by-side coordination with alignment
│   │   └── health_dashboard.py      # Health visualization with error handling
│   ├── demos/
│   │   ├── __init__.py              # Demo module exports
│   │   ├── kotler_demo.py           # Flow demonstration with user validation
│   │   ├── fault_injection.py       # Fault testing with recovery validation
│   │   ├── health_dashboard.py      # Health monitoring demo
│   │   └── comprehensive_test.py    # All-agent testing with progress tracking
│   └── utils/
│       ├── __init__.py              # Utility exports
│       └── colors.py                # Terminal colors with compatibility checking
└── neurocircuit_logs/               # Generated logs with validation
    ├── events.jsonl                 # Real-time event stream
    ├── kotler_demo.json            # Demo session data
    ├── fault_event.json            # Fault injection records
    └── *_state.json                # System state snapshots
```

## 🔧 Comprehensive Error Handling Guide

### Common Issues and Solutions

#### 1. Import Errors
```
❌ ModuleNotFoundError: No module named 'src'

🔍 CAUSE: Running from wrong directory or missing __init__.py files
✅ SOLUTION: 
   - Ensure you're in the project root directory
   - Run: python setup.py to create missing files
   - Check: ls -la src/ for __init__.py files
```

#### 2. Permission Errors
```
❌ PermissionError: Cannot write to neurocircuit_logs/

🔍 CAUSE: Insufficient write permissions for log directory
✅ SOLUTION:
   - Check permissions: ls -ld neurocircuit_logs/
   - Fix permissions: chmod 755 neurocircuit_logs/
   - Or run with sudo (not recommended for production)
```

#### 3. JSON Validation Errors
```
❌ JSON decode error: Expecting ',' delimiter

🔍 CAUSE: Corrupted or incomplete JSON files
✅ SOLUTION:
   - Run: python test_logs.py --validate-only
   - Check disk space: df -h
   - Examine file: tail -n 20 problematic_file.json
```

#### 4. Display Alignment Issues
```
❌ Terminal display appears misaligned

🔍 CAUSE: Terminal width < 120 characters or font issues
✅ SOLUTION:
   - Resize terminal: echo $COLUMNS (should be ≥120)
   - Use monospace font: DejaVu Sans Mono, Consolas, etc.
   - Check locale: echo $LANG (should support UTF-8)
```

#### 5. Health Calculation Errors
```
❌ ValueError: Weights must sum to approximately 1.0

🔍 CAUSE: Invalid custom weights for health calculation
✅ SOLUTION:
   - Check weight values sum to 1.0
   - Use default weights: SystemStateAnalyzer.DEFAULT_HEALTH_WEIGHTS
   - Validate inputs: all(0 <= w <= 1 for w in weights.values())
```

### Debug Mode

Enable detailed error tracebacks:
```bash
export NEUROCIRCUIT_DEBUG=1
python main.py kotler-live-demo
```

## 🎯 Extensive Code Documentation

Every file includes:

### Function-Level Documentation
```python
def generate_baseline_metrics(self, variation_factor: float = 0.1,
                             target_health: Optional[float] = None) -> SystemMetrics:
    """
    Generate realistic baseline system metrics with controlled variation.
    
    This method creates realistic system metrics that can be used as baselines
    for testing, demonstrations, and analysis. The metrics are generated to
    represent a healthy, well-functioning system with natural variation.
    
    Args:
        variation_factor (float): Amount of random variation (0.0-1.0)
                                0.0 = no variation, 1.0 = maximum variation
        target_health (float, optional): Target health score (0-100)
                                       If specified, metrics are adjusted to achieve this score
    
    Returns:
        SystemMetrics: Realistic baseline system metrics
        
    Raises:
        ValueError: If variation_factor is outside valid range
        
    Example:
        >>> system = NeuroCircuitSystem()
        >>> metrics = system.generate_baseline_metrics(variation_factor=0.2, target_health=85.0)
        >>> print(f"Generated health: {analyzer.calculate_health_score(metrics):.1f}")
    """
```

### Error Handling Patterns
```python
try:
    # Main operation
    result = perform_complex_operation()
except SpecificException as e:
    # Handle specific error with context
    logger.error(f"Operation failed: {e}")
    # Provide fallback or recovery
    result = fallback_operation()
except Exception as e:
    # Handle unexpected errors
    logger.error(f"Unexpected error: {e}")
    if debug_mode:
        traceback.print_exc()
    raise SystemError(f"Critical failure in operation: {e}") from e
```

### Input Validation Examples
```python
# ===== INPUT VALIDATION =====
if not isinstance(metrics, SystemMetrics):
    raise ValueError("metrics must be a SystemMetrics instance")

if not 0.0 <= variation_factor <= 1.0:
    raise ValueError("variation_factor must be between 0.0 and 1.0")

# Sanitize string inputs
agent_id = validate_agent_id(agent_name)  # Raises ValueError if invalid
```

## 📊 Quality Assurance Features

### Automated Validation
- **JSON Structure Validation**: Syntax checking with detailed error reporting
- **Content Type Detection**: Automatic identification of log file types
- **Field Completeness**: Required field checking with warnings for missing optional fields
- **Value Range Validation**: Metric bounds checking with threshold alerts
- **Cross-File Consistency**: Session-wide validation with correlation analysis

### Quality Scoring System
```
Quality Score Calculation:
Base Score: 100 points
Deductions:
- Critical Errors: -20 points each
- Warnings: -5 points each
- Missing Required Fields: -15 points each
- Invalid Ranges: -10 points each
- Inconsistencies: -5 points each

Rating Scale:
90-100: Excellent
75-89:  Good  
60-74:  Fair
40-59:  Poor
0-39:   Critical
```

## 🧪 Testing and Validation

### Comprehensive Test Suite
```bash
# Test all agents with detailed reporting
python main.py test-all-agents

# Validate all log files
python test_logs.py --validate-only

# Performance stress testing
python -c "
from src.demos.comprehensive_test import run_performance_stress_test
run_performance_stress_test(iterations=10)
"

# Memory usage validation
python -c "
import psutil, os
print(f'Memory usage: {psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024:.1f} MB')
"
```

### Error Recovery Testing
```bash
# Test fault injection recovery
python main.py fault-injection

# Test with corrupted inputs
echo '{"invalid": json}' > test_invalid.json
python test_logs.py --validate-only

# Test permission handling
chmod 000 neu
