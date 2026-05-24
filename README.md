# PyStatsFinance

**Financial and quantitative statistical computing for Python.**

> **Status: `0.1.0` — first module shipped.** Return-series performance metrics
> are available now; more quantitative-finance methods are on the roadmap below.

PyStatsFinance is part of the open-core PyStatistics family:

| Package | Layer |
|---|---|
| [`pystatistics`](https://github.com/sgcx-org/pystatistics) | Fundamental, general statistics |
| [`pystatsbio`](https://github.com/sgcx-org/pystatsbio) | Biotech / pharma statistics |
| [`pystatsclinical`](https://github.com/sgcx-org/pystatsclinical) | Clinical-trial / clinical-research statistics |
| [`pystatsgenomic`](https://github.com/sgcx-org/pystatsgenomic) | Genomics / computational-biology statistics |
| **`pystatsfinance`** | Financial / quantitative statistics |
| [`pystatsinsurance`](https://github.com/sgcx-org/pystatsinsurance) | Actuarial / insurance statistics |

Like its siblings, it builds on `pystatistics` for the general statistical layer
and adds methods specific to quantitative finance.

## What's available now (0.1.0)

**Return-series risk and performance metrics:**

```python
from pystatsfinance import performance

returns = [0.01, -0.02, 0.03, -0.01, 0.02]

performance.sharpe_ratio(returns)              # annualized Sharpe ratio
performance.annualized_volatility(returns)     # annualized volatility
performance.max_drawdown(returns)              # worst peak-to-trough decline
```

`sharpe_ratio` annualizes `mean(excess) / std(excess)` (sample standard
deviation; per-period risk-free rate). `max_drawdown` works on returns or a
price series (`are_prices=True`) and reports the decline magnitude with its peak
and trough indices. All three fail loud on empty/non-finite input, and the
Sharpe ratio is raised — not returned as inf/nan — when volatility is zero.

## Roadmap (candidates, not commitments)

- Value-at-Risk and Conditional VaR (historical and parametric).
- Extended performance ratios (Sortino, Calmar, Information) and drawdown
  analytics.
- GARCH-family volatility and portfolio optimization.

## Installation

```bash
pip install pystatsfinance
```

## License

MIT © Hai-Shuo. Part of the [SGCX](https://sgcx.org) open-core ecosystem.
