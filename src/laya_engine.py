"""Laya strategy engine interface.

This module defines typed strategy outputs while leaving actual Laya integration
for a later iteration once API contracts are confirmed.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping

from src.race_state import RaceState


class StrategyChoice(str, Enum):
    PIT_NOW = "PIT_NOW"
    STAY_OUT = "STAY_OUT"
    PIT_NEXT_LAP = "PIT_NEXT_LAP"


class TyreChoice(str, Enum):
    SOFT = "SOFT"
    MEDIUM = "MEDIUM"
    HARD = "HARD"
    INTERMEDIATE = "INTERMEDIATE"
    WET = "WET"
    KEEP_CURRENT = "KEEP_CURRENT"


@dataclass(frozen=True)
class LayaDecision:
    """Typed probabilistic strategy decision.

    Full probability distributions are retained for downstream evaluation and
    calibration. Recommended values are optional conveniences.
    """

    strategy_probabilities: Mapping[StrategyChoice, float]
    tyre_probabilities: Mapping[TyreChoice, float]
    urgency: int
    recommended_strategy: StrategyChoice | None = None
    recommended_tyre: TyreChoice | None = None


class LayaStrategyEngine:
    """Adapter boundary for future Laya integration."""

    def decide(self, race_state: RaceState) -> LayaDecision:
        """Return a probabilistic strategy decision for a point-in-time state.

        TODO: integrate with real Laya APIs once the invocation contract and
        response schema are confirmed.
        """
        raise NotImplementedError("Laya integration is not implemented yet")
