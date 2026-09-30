"""Evaluation scaffolding for strategy predictions.

The evaluator is the only component allowed to inspect data from after the
prediction timestamp. This module intentionally separates prediction storage,
observed outcomes, and evaluation heuristics.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from src.laya_engine import LayaDecision


@dataclass(frozen=True)
class PredictionRecord:
    """Stored model output made at a point in simulated race time."""

    timestamp: datetime
    session_key: int
    driver_number: int
    decision: LayaDecision


@dataclass(frozen=True)
class ValidationResult:
    """Result of evaluating one prediction against future observed race data."""

    observed_outcome: dict[str, Any]
    evaluation_heuristic: str
    is_consistent: bool
    notes: str | None = None


class Evaluator:
    """Backtesting boundary.

    Notes
    -----
    - Historical outcomes are observations, not automatic proof of counterfactual
      optimality.
    - Future evaluation should keep explicit separation between:
      prediction, probability, observed outcome, heuristic, and validation result.
    """

    def evaluate_prediction(self, prediction: PredictionRecord) -> ValidationResult:
        """Evaluate a prediction using post-prediction historical race data.

        TODO: implement domain heuristics for outcome comparison and validation.
        """
        raise NotImplementedError("Prediction evaluation is not implemented yet")
