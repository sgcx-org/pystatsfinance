# First Features — pystatsfinance

This package is currently a **reserved `0.0.1` skeleton**. This file specifies the
first 1–2 features a future session should implement to turn it into a real
`0.1.0` (the "harden later" step of SGC-Bio roadmap item B-3).

## Ground rules (read first)

- **Stay in this layer.** Only implement things that are genuinely *financial /
  quantitative-finance*. General statistics (mean, std, distributions) belong in
  `pystatistics`; this package adds the finance-specific framing on top.
- **Build on `pystatistics`** for the general statistical layer; don't
  reimplement it.
- **Follow `pystatsbio`'s conventions** — hatchling packaging, the Coding Bible
  (`CLAUDE.md` there: fail loud, one job per module, tests first, deterministic),
  typed, ruff/mypy clean.
- **Ship with tests** (normal / edge / failure) and bump to `0.1.0` once landed.

## Feature 1 (primary): return-series risk/performance metrics

The bread-and-butter readouts for a series of periodic returns. Group them in a
`performance` module.

- Suggested APIs:
  - `sharpe_ratio(returns, *, risk_free=0.0, periods_per_year=252) -> float`
    — annualized: `mean(excess)/std(excess) * sqrt(periods_per_year)`.
  - `annualized_volatility(returns, *, periods_per_year=252) -> float`
    — `std(returns) * sqrt(periods_per_year)`.
  - `max_drawdown(returns_or_prices, *, are_prices=False) -> MaxDrawdown`
    — largest peak-to-trough decline of the cumulative curve; report magnitude
    plus peak/trough indices.
- Decisions to make explicit: sample vs population std (document the choice);
  whether `risk_free` is per-period or annual (document and convert).
- Failure behavior (fail loud): reject empty input; zero volatility → Sharpe
  undefined, raise rather than return `inf`/`nan` silently.
- Tests: a known return series with hand-computed Sharpe / vol / drawdown;
  the zero-vol and empty-input failure paths; price-vs-return input modes.

## Feature 2 (optional secondary): Value-at-Risk

- Suggested API: `value_at_risk(returns, *, alpha=0.05, method="historical") ->
  float` with `method` ∈ {`"historical"`, `"parametric"`} (parametric = Gaussian
  using mean/std from `pystatistics`).
- Tests: historical VaR = empirical quantile; parametric VaR matches the
  closed-form Gaussian quantile.
