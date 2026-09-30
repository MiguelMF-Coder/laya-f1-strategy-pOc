"""Streamlit app entrypoint for the Laya F1 Strategy Engine PoC."""

from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Laya F1 Strategy Engine", layout="wide")

st.title("Laya F1 Strategy Engine")
st.subheader("Probabilistic Formula 1 race strategy using historical replay")

st.markdown("---")

st.header("Race")
st.info("Waiting for replay pipeline race/session input.")

st.header("Driver")
st.info("Waiting for replay pipeline driver input.")

st.header("Current Race State")
st.info("Point-in-time race state will appear here once replay is connected.")

st.header("Laya Strategy Decision")
st.info("No decision available yet. Waiting for Laya integration.")

st.header("Strategy probabilities")
st.info("Probability distribution will be shown when model outputs are available.")

st.header("Recommended tyre")
st.info("Tyre recommendation will appear here.")

st.header("Confidence")
st.info("Decision confidence is not available yet.")

st.header("Decision Validation")
st.info("Validation is pending evaluator implementation.")

st.header("Backtest Metrics")
st.info("Metrics will appear after predictions and evaluation results are available.")
