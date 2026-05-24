"""Return-series risk and performance metrics.

Annualized Sharpe ratio, annualized volatility, and maximum drawdown for a
series of periodic returns (or a price series, for drawdown).

Validates against: hand-computed worked examples; empyrical conventions.
"""

from pystatsfinance.performance._common import MaxDrawdown
from pystatsfinance.performance._metrics import (
    annualized_volatility,
    max_drawdown,
    sharpe_ratio,
)

__all__ = [
    "MaxDrawdown",
    "annualized_volatility",
    "max_drawdown",
    "sharpe_ratio",
]
