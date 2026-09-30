# laya-f1-strategy-pOc

Formula 1 race strategy proof-of-concept using OpenF1 historical data replay and typed probabilistic decisions from a future Laya integration.

## Objective

Build a replay-first strategy pipeline that simulates race decisions as if the race were live:

1. Replay historical events chronologically.
2. Construct a **point-in-time** race state with no future leakage.
3. Request typed probabilistic strategy decisions.
4. Store predictions.
5. Evaluate predictions later with future historical observations.

## Architecture

```text
OpenF1 Historical Data
        ↓
Replay Engine
        ↓
Point-in-Time Race State
        ↓
Laya
        ↓
Typed Probabilistic Decision
        ↓
Prediction Store
        ↓
Future Race Data
        ↓
Evaluator
        ↓
Calibration / Backtesting
```

Historical replay simulates a real-time feed. The same downstream architecture can later consume an actual live stream.

## Point-in-time principle (critical)

At simulated timestamp `T`, the decision path may only access data available at or before `T`.

Future data is only allowed in the evaluator after a prediction has been stored.

Examples of forbidden future leakage at lap `N`:
- future pit stops
- future race control events
- future weather updates
- final stint lengths
- future positions/lap times

## Prediction vs backtesting

- **Prediction**: model output created at timestamp `T` using only known data up to `T`.
- **Backtesting/Evaluation**: later comparison against outcomes observed after `T`.

Observed historical strategy is not automatically proof of the optimal counterfactual strategy.

## Project structure

```text
.github/
  copilot-instructions.md
src/
  __init__.py
  openf1_client.py
  race_state.py
  laya_engine.py
  replay_engine.py
  evaluator.py
  metrics.py
data/
  .gitkeep
tests/
  __init__.py
  test_openf1_client.py
app.py
requirements.txt
.gitignore
README.md
```

## Installation

### 1) Create and activate a virtual environment

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install requirements

```bash
pip install -r requirements.txt
```

## Run the OpenF1 Dutch GP check

The integration test uses real OpenF1 data and is skipped by default.

```bash
OPENF1_INTEGRATION=1 pytest -s tests/test_openf1_client.py
```

Alternative executable helper:

```bash
python -m src.openf1_client
```

Expected output fields:
- meeting name
- session name
- date
- session_key

## Run Streamlit

```bash
streamlit run app.py
```

## Project status

This is an initial scaffold:
- OpenF1 client foundation and Dutch GP session lookup are in place.
- RaceState/Laya/Replay/Evaluator/Metrics modules are intentionally skeletal.
- Complex replay logic, model integration, storage, and scoring are pending next iterations.
