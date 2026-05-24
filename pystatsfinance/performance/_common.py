"""Result type for maximum-drawdown analysis."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MaxDrawdown:
    """Largest peak-to-trough decline of a cumulative wealth curve.

    Attributes
    ----------
    max_drawdown : float
        Magnitude of the largest decline as a non-negative fraction, e.g. 0.25
        means a 25% peak-to-trough drop. Zero when the curve never declines.
    peak_index : int
        Index (into the input series) of the peak preceding the worst trough.
    trough_index : int
        Index (into the input series) of the worst trough.
    """

    max_drawdown: float
    peak_index: int
    trough_index: int

    def summary(self) -> str:
        """Human-readable one-line summary."""
        return (
            f"Max drawdown: {self.max_drawdown:.4%} "
            f"(peak @ {self.peak_index} -> trough @ {self.trough_index})"
        )
