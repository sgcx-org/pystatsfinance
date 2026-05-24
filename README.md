# PyStatsFinance

**Financial and quantitative statistical computing for Python.**

> **Status: early / reserved (`0.0.1`).** This package reserves the
> `pystatsfinance` name within the **PyStatistics open-core ecosystem** and will
> grow into a full quantitative-finance statistics library. The public API is
> forthcoming.

PyStatsFinance is part of the open-core PyStatistics family:

| Package | Layer |
|---|---|
| [`pystatistics`](https://github.com/sgcx-org/pystatistics) | Fundamental, general statistics |
| [`pystatsbio`](https://github.com/sgcx-org/pystatsbio) | Biotech / pharma statistics |
| **`pystatsfinance`** | Financial / quantitative statistics |

Like its siblings, it builds on `pystatistics` for the general statistical layer
and adds methods specific to quantitative finance.

## Planned scope (candidates, not commitments)

- Return-series risk/performance metrics: Sharpe ratio, maximum drawdown,
  annualized volatility.
- Value-at-Risk (historical and parametric).

## Installation

```bash
pip install pystatsfinance
```

## License

MIT © Hai-Shuo. Part of the [SGCX](https://sgcx.org) open-core ecosystem.
