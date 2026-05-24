"""Tests for performance.sharpe_ratio, annualized_volatility, max_drawdown."""

import numpy as np
import pytest

from pystatsfinance import performance

RETURNS = [0.01, -0.02, 0.03, -0.01, 0.02]


# ---------------------------------------------------------------------------
# sharpe_ratio
# ---------------------------------------------------------------------------

def test_sharpe_matches_hand_computation():
    # mean=0.006, sample std=0.0207364, annualized with sqrt(252)
    s = performance.sharpe_ratio(RETURNS)
    assert s == pytest.approx(4.593220484431883, rel=1e-9)


def test_sharpe_with_risk_free_reduces_value():
    base = performance.sharpe_ratio(RETURNS)
    with_rf = performance.sharpe_ratio(RETURNS, risk_free=0.005)
    assert with_rf < base


def test_sharpe_periods_per_year_scales_by_sqrt():
    daily = performance.sharpe_ratio(RETURNS, periods_per_year=252)
    monthly = performance.sharpe_ratio(RETURNS, periods_per_year=12)
    assert daily / monthly == pytest.approx(np.sqrt(252 / 12), rel=1e-9)


def test_sharpe_zero_volatility_raises():
    with pytest.raises(ValueError, match="undefined"):
        performance.sharpe_ratio([0.01, 0.01, 0.01])


# ---------------------------------------------------------------------------
# annualized_volatility
# ---------------------------------------------------------------------------

def test_annualized_volatility_matches_hand_computation():
    v = performance.annualized_volatility(RETURNS)
    assert v == pytest.approx(0.32918080138428485, rel=1e-9)


def test_annualized_volatility_zero_for_constant_returns():
    assert performance.annualized_volatility([0.02, 0.02, 0.02]) == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# max_drawdown
# ---------------------------------------------------------------------------

def test_max_drawdown_from_prices():
    md = performance.max_drawdown(
        [100.0, 120.0, 90.0, 95.0, 80.0, 130.0], are_prices=True
    )
    assert md.max_drawdown == pytest.approx(1.0 / 3.0)
    assert md.peak_index == 1
    assert md.trough_index == 4


def test_max_drawdown_from_returns():
    # wealth = [1.1, 0.55, 0.66]; worst drawdown is 50% at index 1.
    md = performance.max_drawdown([0.1, -0.5, 0.2])
    assert md.max_drawdown == pytest.approx(0.5)
    assert md.peak_index == 0
    assert md.trough_index == 1


def test_max_drawdown_monotonic_increase_is_zero():
    md = performance.max_drawdown([0.01, 0.02, 0.03])
    assert md.max_drawdown == pytest.approx(0.0)


def test_max_drawdown_summary_is_string():
    md = performance.max_drawdown([0.1, -0.5, 0.2])
    assert isinstance(md.summary(), str)


# ---------------------------------------------------------------------------
# Failure cases
# ---------------------------------------------------------------------------

def test_empty_input_raises():
    with pytest.raises(ValueError, match="non-empty"):
        performance.sharpe_ratio([])
    with pytest.raises(ValueError, match="non-empty"):
        performance.annualized_volatility([])
    with pytest.raises(ValueError, match="non-empty"):
        performance.max_drawdown([])


def test_non_finite_raises():
    with pytest.raises(ValueError, match="finite"):
        performance.annualized_volatility([0.01, np.nan, 0.02])


def test_single_observation_raises_for_sharpe_and_vol():
    with pytest.raises(ValueError, match="at least 2"):
        performance.sharpe_ratio([0.01])
    with pytest.raises(ValueError, match="at least 2"):
        performance.annualized_volatility([0.01])


def test_non_positive_price_raises():
    with pytest.raises(ValueError, match="strictly positive"):
        performance.max_drawdown([100.0, 0.0, 90.0], are_prices=True)


def test_bad_periods_per_year_raises():
    with pytest.raises(ValueError, match="periods_per_year"):
        performance.annualized_volatility(RETURNS, periods_per_year=0)


def test_two_dimensional_input_raises():
    with pytest.raises(ValueError, match="1-dimensional"):
        performance.annualized_volatility([[0.01, 0.02], [0.03, 0.04]])
