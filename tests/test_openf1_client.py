"""Tests for OpenF1 client foundations."""

from __future__ import annotations

import os

import pytest

from src.openf1_client import OpenF1Client, find_2023_dutch_gp_race_session


@pytest.mark.integration
def test_find_2023_dutch_gp_race_session_printable_output() -> None:
    """Fetch real OpenF1 session data for the 2023 Dutch GP race.

    This test is intentionally integration-only and can be skipped by default.
    """
    if os.getenv("OPENF1_INTEGRATION", "0") != "1":
        pytest.skip("Set OPENF1_INTEGRATION=1 to run live OpenF1 integration test")

    summary = find_2023_dutch_gp_race_session(OpenF1Client())

    print(f"meeting name: {summary.meeting_name}")
    print(f"session name: {summary.session_name}")
    print(f"date: {summary.date_start}")
    print(f"session_key: {summary.session_key}")

    assert summary.session_key is not None
    assert summary.session_name == "Race"
    assert summary.meeting_name is not None
