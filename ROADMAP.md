# Roadmap — pystatsfinance

A working **checklist** of features that plausibly belong at the *financial /
quantitative-finance / econometrics* layer. Tick items off as they land, in
roughly the way `pystatistics/docs/ROADMAP.md` tracks its modules.

**This list is not a commitment.** It captures *what kind of thing belongs here*
and in roughly what order we'd build it. Re-order, drop, or promote/demote
freely. Tiers are priority bands, not deadlines.

## Layer rules (the gate every item must pass)

- **Stay in this layer.** Only genuinely *finance-specific* methods. General
  statistics (mean/std/distributions, regression, time-series fitting) live in
  `pystatistics`; this layer adds the finance framing on top.
- **Build on `pystatistics`** — regression for CAPM/factor models, `timeseries`
  for unit-root/ACF, `montecarlo` for simulation. Don't reimplement.
- **The canonical example (from our layer rules):** **GARCH** is estimated *via*
  MLE (a `pystatistics` primitive) but is a finance/econometrics *model* nobody
  in medicine uses → it belongs **here**, not in `pystatistics`. "Uses MLE"
  never promotes a model upward.
- **Promotion rule:** a mechanic shared by ≥2 separate domains (e.g.
  extreme-value tail fitting, also used by insurance) is a candidate to promote
  to `pystatistics`. See *Ambiguous*.
- Conventions: `pystatsbio` Coding Bible, typed, ruff/mypy clean, tests, version
  bump via the release flow.

## Tier 1 — return-series risk & performance

- [ ] **Performance metrics** — Sharpe, annualized volatility, max drawdown.
  *v0.1.0 target — full spec in [FIRST_FEATURES.md](FIRST_FEATURES.md).*
- [ ] **Value-at-Risk** — historical and parametric (Gaussian). *See
  FIRST_FEATURES.md.*
- [ ] **Extended performance ratios** — Sortino, Calmar, Information ratio,
  Treynor.
- [ ] **Conditional VaR / Expected Shortfall** — historical and parametric.
- [ ] **Return utilities** — simple↔log returns, cumulative/compounded returns,
  annualization helpers (document the conventions, fail loud on mismatches).

## Tier 2 — risk analytics & factor models

- [ ] **Drawdown analytics** — underwater curve, drawdown durations, recovery
  time.
- [ ] **Rolling / EWMA volatility** — windowed and exponentially weighted.
- [ ] **CAPM & factor models** — beta/alpha, Fama–French regressions (thin
  framing over `pystatistics` regression). *(Thinness is ambiguous — see below.)*
- [ ] **VaR backtesting** — Kupiec POF test, Christoffersen independence /
  conditional-coverage.

## Tier 3 — models & optimization

- [ ] **GARCH-family volatility** — GARCH(1,1) and friends via MLE; the
  canonical domain model for this layer.
- [ ] **Portfolio optimization** — mean–variance / efficient frontier, risk
  parity.
- [ ] **Monte Carlo risk** — simulated VaR / scenario paths (consumes
  `pystatistics` montecarlo).

## Ambiguous — discuss before building

- **Option pricing (Black–Scholes, Greeks)** — quant-finance, but is it
  *statistics*? It may sit outside this library's scope entirely. Decide whether
  pricing belongs at all.
- **Extreme-value theory / GPD peaks-over-threshold (tail risk)** — generic EVT
  machinery, and insurance large-loss modeling needs the identical mechanic.
  **Decided: promote to `pystatistics`** (on its roadmap as a demand-driven
  primitive) — do *not* build it here. Implement in `pystatistics` when the
  first finance feature needs it, then peg the new version. Same for the generic
  **parametric distribution fitting (`fitdist`)** primitive used by parametric
  VaR / return-distribution work.
- **Cointegration / unit-root extensions (Engle–Granger, Johansen)** — ADF/KPSS
  already live in `pystatistics.timeseries`. Are these general econometric
  primitives (promote) or finance-specific (here)?
- **CAPM / Fama–French** — so thin over `pystatistics` regression that they may
  not earn their own module; or the convenience framing is exactly the point.
  Worth it?
