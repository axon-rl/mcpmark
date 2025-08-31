"""MCPMark - A benchmark for Model Context Protocol (MCP) servers.

This package provides benchmarking tools for MCP servers across different services.
"""

__version__ = "0.0.1"

# Import key modules for easy access
try:
    from src import agent, evaluator, factory, services, model_config, results_reporter
    from src.logger import get_logger
    from src.errors import *
except ImportError:
    # Fallback for when src modules aren't available
    pass

# Make key functions available at top level
__all__ = [
    'agent',
    'evaluator', 
    'factory',
    'services',
    'model_config',
    'results_reporter',
    'get_logger',
    '__version__'
]