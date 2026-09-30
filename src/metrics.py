"""Metrics interfaces for strategy backtesting."""

from __future__ import annotations

from typing import Sequence

from src.evaluator import ValidationResult


def top1_match_rate(results: Sequence[ValidationResult]) -> float:
    """Compute top-1 strategy match rate."""
    raise NotImplementedError


def average_confidence(confidences: Sequence[float]) -> float:
    """Compute average model confidence."""
    raise NotImplementedError


def brier_score(probabilities: Sequence[float], outcomes: Sequence[int]) -> float:
    """Compute Brier score for probabilistic forecasts."""
    raise NotImplementedError


def calibration_buckets(probabilities: Sequence[float], outcomes: Sequence[int]) -> dict[str, float]:
    """Compute reliability statistics by confidence bucket."""
    raise NotImplementedError


def high_confidence_accuracy(
    probabilities: Sequence[float],
    outcomes: Sequence[int],
    threshold: float = 0.8,
) -> float:
    """Compute accuracy above confidence threshold."""
    raise NotImplementedError
