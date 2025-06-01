"""
Terminal color utilities for NeuroCircuit
Provides consistent color schemes across the system
"""

class Colors:
    """Terminal color codes for consistent styling"""
    
    # Reset
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Standard colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    @classmethod
    def colorize(cls, text: str, color: str) -> str:
        """Apply color to text with automatic reset"""
        return f"{color}{text}{cls.RESET}"
    
    @classmethod
    def bold(cls, text: str) -> str:
        """Make text bold"""
        return f"{cls.BOLD}{text}{cls.RESET}"
    
    @classmethod
    def success(cls, text: str) -> str:
        """Green success text"""
        return cls.colorize(text, cls.BRIGHT_GREEN)
    
    @classmethod
    def error(cls, text: str) -> str:
        """Red error text"""
        return cls.colorize(text, cls.BRIGHT_RED)
    
    @classmethod
    def warning(cls, text: str) -> str:
        """Yellow warning text"""
        return cls.colorize(text, cls.BRIGHT_YELLOW)
    
    @classmethod
    def info(cls, text: str) -> str:
        """Cyan info text"""
        return cls.colorize(text, cls.BRIGHT_CYAN)
