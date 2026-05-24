# Changelog

## 0.1.1

### Documentation
- Expanded the README to document the performance-metrics module
  (`performance`) with a usage example, and to list the full PyStatistics
  open-core ecosystem.


## 0.1.0

### Added
- `performance` subpackage with return-series risk and performance metrics:
  - `performance.sharpe_ratio(...)`: annualized Sharpe ratio (sample std,
    per-period risk-free rate).
  - `performance.annualized_volatility(...)`: annualized volatility.
  - `performance.max_drawdown(...)`: largest peak-to-trough decline of the
    cumulative wealth curve (from returns or a price series), with peak and
    trough indices.
  Fails loud on empty/non-finite input and on an undefined (zero-volatility)
  Sharpe ratio rather than returning inf/nan.

First feature release, promoting the package from a reserved skeleton.
