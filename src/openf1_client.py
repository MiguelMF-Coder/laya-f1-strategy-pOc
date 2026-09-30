"""OpenF1 API client utilities.

This module exposes a thin, typed client for OpenF1 endpoints used by the
strategy replay proof-of-concept.
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
from typing import Any

import requests

LOGGER = logging.getLogger(__name__)


class OpenF1APIError(RuntimeError):
    """Raised when the OpenF1 API cannot be queried successfully."""


@dataclass(frozen=True)
class SessionSummary:
    """Minimal OpenF1 session metadata used by this PoC scaffold."""

    meeting_name: str | None
    session_name: str | None
    date_start: str | None
    session_key: int | None


class OpenF1Client:
    """Simple OpenF1 REST client.

    Parameters
    ----------
    base_url:
        Base API URL. Defaults to the OpenF1 v1 endpoint.
    timeout:
        Request timeout in seconds for all API calls.
    session:
        Optional preconfigured ``requests.Session`` (useful for testing).
    """

    def __init__(
        self,
        base_url: str = "https://api.openf1.org/v1",
        timeout: float = 10.0,
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests.Session()

    def _get(self, endpoint: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            LOGGER.debug("Requesting OpenF1 endpoint", extra={"url": url, "params": params})
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            payload = response.json()
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else "unknown"
            message = f"OpenF1 request failed with status {status} for {url}"
            LOGGER.exception(message)
            raise OpenF1APIError(message) from exc
        except requests.RequestException as exc:
            message = f"OpenF1 request failed for {url}: {exc}"
            LOGGER.exception(message)
            raise OpenF1APIError(message) from exc
        except ValueError as exc:
            message = f"OpenF1 response was not valid JSON for {url}"
            LOGGER.exception(message)
            raise OpenF1APIError(message) from exc

        if not isinstance(payload, list):
            message = f"Unexpected OpenF1 payload type for {url}: {type(payload).__name__}"
            LOGGER.error(message)
            raise OpenF1APIError(message)

        return payload

    def get_sessions(
        self,
        *,
        year: int | None = None,
        country_name: str | None = None,
        location: str | None = None,
        session_name: str | None = None,
        meeting_name: str | None = None,
    ) -> list[dict[str, Any]]:
        """Fetch sessions with optional filters."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        if country_name is not None:
            params["country_name"] = country_name
        if location is not None:
            params["location"] = location
        if session_name is not None:
            params["session_name"] = session_name
        if meeting_name is not None:
            params["meeting_name"] = meeting_name
        return self._get("sessions", params=params or None)

    def get_drivers(self, session_key: int) -> list[dict[str, Any]]:
        return self._get("drivers", params={"session_key": session_key})

    def get_laps(self, session_key: int, driver_number: int | None = None) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"session_key": session_key}
        if driver_number is not None:
            params["driver_number"] = driver_number
        return self._get("laps", params=params)

    def get_positions(self, session_key: int, driver_number: int | None = None) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"session_key": session_key}
        if driver_number is not None:
            params["driver_number"] = driver_number
        return self._get("position", params=params)

    def get_intervals(self, session_key: int, driver_number: int | None = None) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"session_key": session_key}
        if driver_number is not None:
            params["driver_number"] = driver_number
        return self._get("intervals", params=params)

    def get_pit_stops(self, session_key: int, driver_number: int | None = None) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"session_key": session_key}
        if driver_number is not None:
            params["driver_number"] = driver_number
        return self._get("pit", params=params)

    def get_stints(self, session_key: int, driver_number: int | None = None) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"session_key": session_key}
        if driver_number is not None:
            params["driver_number"] = driver_number
        return self._get("stints", params=params)

    def get_weather(self, session_key: int) -> list[dict[str, Any]]:
        return self._get("weather", params={"session_key": session_key})

    def get_race_control(self, session_key: int) -> list[dict[str, Any]]:
        return self._get("race_control_messages", params={"session_key": session_key})


def find_2023_dutch_gp_race_session(client: OpenF1Client) -> SessionSummary:
    """Find the 2023 Dutch GP race session at Zandvoort using OpenF1 data."""
    sessions = client.get_sessions(year=2023, country_name="Netherlands", session_name="Race")

    filtered = [
        session
        for session in sessions
        if "zandvoort" in str(session.get("location", "")).lower()
        or "dutch" in str(session.get("meeting_name", "")).lower()
    ]

    if not filtered:
        raise OpenF1APIError("Could not find 2023 Dutch Grand Prix race session in OpenF1 data")

    filtered.sort(key=lambda item: str(item.get("date_start", "")))
    race_session = filtered[0]

    return SessionSummary(
        meeting_name=race_session.get("meeting_name"),
        session_name=race_session.get("session_name"),
        date_start=race_session.get("date_start"),
        session_key=race_session.get("session_key"),
    )


def print_2023_dutch_gp_race_session() -> None:
    """Executable helper that prints the 2023 Dutch GP race session details."""
    summary = find_2023_dutch_gp_race_session(OpenF1Client())
    print(f"meeting name: {summary.meeting_name}")
    print(f"session name: {summary.session_name}")
    print(f"date: {summary.date_start}")
    print(f"session_key: {summary.session_key}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print_2023_dutch_gp_race_session()
