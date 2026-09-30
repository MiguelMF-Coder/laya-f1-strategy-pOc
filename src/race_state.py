"""Race state structures.

`RaceState` is intentionally point-in-time only.
It must never include data from timestamps later than the state timestamp.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class RaceState:
    """Point-in-time state for one driver in one race session."""

    timestamp: datetime
    session_key: int
    driver_number: int | None = None
    driver_name: str | None = None
    lap_number: int | None = None
    position: int | None = None
    gap_to_leader: float | None = None
    interval_to_ahead: float | None = None
    compound: str | None = None
    tyre_age: int | None = None
    recent_lap_time: float | None = None
    rainfall: float | None = None
    air_temperature: float | None = None
    track_temperature: float | None = None
    safety_car: bool | None = None
    virtual_safety_car: bool | None = None
    flag: str | None = None
    recent_events: list[str] = field(default_factory=list)
