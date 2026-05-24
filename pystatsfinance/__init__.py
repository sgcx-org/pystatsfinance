"""
PyStatsFinance: Financial and quantitative statistical computing.

Part of the PyStatistics open-core ecosystem (alongside ``pystatistics`` and
``pystatsbio``). Provides finance-specific methods built on the general
statistical layer.

Usage:
    from pystatsfinance import performance
    sharpe = performance.sharpe_ratio(returns)
"""

__version__ = "0.1.0"
__author__ = "Hai-Shuo"
__email__ = "contact@sgcx.org"

from pystatsfinance import performance

__all__ = [
    "__version__",
    "performance",
]
