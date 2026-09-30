"""Replay engine scaffold.

Future responsibilities:
- merge and sort race events chronologically
- advance simulated race time
- construct point-in-time RaceState instances
- detect strategy-relevant moments
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Iterable

from src.race_state import RaceState


@dataclass(frozen=True)
class ReplayEvent:
    """Normalized replay event."""

    timestamp: datetime
    event_type: str
    payload: dict[str, Any]


class ReplayEngine:
    """Chronological race replay skeleton."""

    def __init__(self, session_key: int) -> None:
        self.session_key = session_key
        self._events: list[ReplayEvent] = []
        self._cursor: int = 0

    def load_events(self, events: Iterable[ReplayEvent]) -> None:
        """Load and sort events in ascending timestamp order."""
        self._events = sorted(events, key=lambda event: event.timestamp)
        self._cursor = 0

    def next_event(self) -> ReplayEvent | None:
        """Return the next event in replay order, if available."""
        if self._cursor >= len(self._events):
            return None
        event = self._events[self._cursor]
        self._cursor += 1
        return event

    def build_race_state(self, timestamp: datetime, driver_number: int) -> RaceState:
        """Build a point-in-time race state for a driver.

        TODO: implement state construction from replay stream data while
        preventing future data leakage.
        """
        raise NotImplementedError("RaceState construction is not implemented yet")
