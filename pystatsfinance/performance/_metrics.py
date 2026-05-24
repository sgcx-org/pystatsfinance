"""Return-series risk and performance metrics.

Bread-and-butter readouts for a series of periodic returns: the annualized
Sharpe ratio, annualized volatility, and maximum drawdown.

Conventions (made explicit, per the project's fail-loud philosophy):

- **Standard deviation** uses the *sample* estimator (``ddof=1``), the usual
  choice for return series of finite length.
- **risk_free** in :func:`sharpe_ratio` is a *per-period* rate, expressed in the
  same period as ``returns`` (e.g. a daily rate for daily returns). It is not
  annualized internally.
- **Annualization** multiplies by ``sqrt(periods_per_year)``.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

from pystatsfinance.performance._common import MaxDrawdown


def _as_1d_finite(values: ArrayLike, name: str) -> NDArray[np.float64]:
    """Coerce to a 1-D float64 array and validate it is non-empty and finite."""
    arr = np.asarray(values, dtype=np.float64)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be 1-dimensional, got {arr.ndim}-D")
    if arr.size == 0:
        raise ValueError(f"{name} must be non-empty")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must contain only finite values")
    return arr


def sharpe_ratio(
    returns: ArrayLike,
    *,
    risk_free: float = 0.0,
    periods_per_year: int = 252,
) -> float:
    """Annualized Sharpe ratio of a periodic return series.

    ``mean(excess) / std(excess) * sqrt(periods_per_year)``, where
    ``excess = returns - risk_free`` and ``std`` is the sample standard
    deviation (ddof=1).

    Parameters
    ----------
    returns : array-like
        Periodic returns (e.g. daily simple returns).
    risk_free : float
        Per-period risk-free rate, in the same period as ``returns``.
    periods_per_year : int
        Number of periods per year used for annualization (e.g. 252 trading
        days). Must be positive.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``returns`` is empty, non-finite, has fewer than two observations,
        ``periods_per_year`` is not positive, or the excess-return volatility
        is zero (Sharpe undefined — raised rather than returning inf/nan).
    """
    arr = _as_1d_finite(returns, "returns")
    if arr.size < 2:
        raise ValueError("returns must have at least 2 observations for a Sharpe ratio")
    if periods_per_year <= 0:
        raise ValueError(f"periods_per_year must be positive, got {periods_per_year}")

    excess = arr - risk_free
    vol = float(np.std(excess, ddof=1))
    if vol == 0.0:
        raise ValueError(
            "excess-return volatility is zero; the Sharpe ratio is undefined"
        )
    return float(np.mean(excess)) / vol * np.sqrt(periods_per_year)


def annualized_volatility(
    returns: ArrayLike,
    *,
    periods_per_year: int = 252,
) -> float:
    """Annualized volatility of a periodic return series.

    ``std(returns, ddof=1) * sqrt(periods_per_year)``.

    Parameters
    ----------
    returns : array-like
        Periodic returns.
    periods_per_year : int
        Number of periods per year used for annualization. Must be positive.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``returns`` is empty, non-finite, has fewer than two observations,
        or ``periods_per_year`` is not positive.
    """
    arr = _as_1d_finite(returns, "returns")
    if arr.size < 2:
        raise ValueError("returns must have at least 2 observations for volatility")
    if periods_per_year <= 0:
        raise ValueError(f"periods_per_year must be positive, got {periods_per_year}")
    return float(np.std(arr, ddof=1)) * np.sqrt(periods_per_year)


def max_drawdown(
    returns_or_prices: ArrayLike,
    *,
    are_prices: bool = False,
) -> MaxDrawdown:
    """Maximum peak-to-trough decline of a cumulative wealth curve.

    Parameters
    ----------
    returns_or_prices : array-like
        Either periodic returns (default) or a price/level series
        (``are_prices=True``). With returns, the wealth curve is the cumulative
        product of ``1 + returns``.
    are_prices : bool
        If True, treat the input as a price/level series and use it directly as
        the wealth curve. Prices must be strictly positive.

    Returns
    -------
    MaxDrawdown
        Magnitude of the worst decline (non-negative fraction) and the peak and
        trough indices into the input series.

    Raises
    ------
    ValueError
        If the input is empty, non-finite, or (when ``are_prices``) contains a
        non-positive price.
    """
    arr = _as_1d_finite(returns_or_prices, "returns_or_prices")

    if are_prices:
        if np.any(arr <= 0.0):
            raise ValueError("prices must be strictly positive")
        wealth = arr
    else:
        wealth = np.cumprod(1.0 + arr)

    running_max = np.maximum.accumulate(wealth)
    drawdown = wealth / running_max - 1.0  # <= 0 everywhere

    trough_index = int(np.argmin(drawdown))
    magnitude = float(-drawdown[trough_index])
    # The relevant peak is the running max attained at or before the trough.
    peak_index = int(np.argmax(wealth[: trough_index + 1]))

    return MaxDrawdown(
        max_drawdown=magnitude,
        peak_index=peak_index,
        trough_index=trough_index,
    )
