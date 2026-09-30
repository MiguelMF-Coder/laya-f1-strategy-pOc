# Copilot Instructions for laya-f1-strategy-pOc

## Core rule

**FUTURE DATA LEAKAGE IS A CRITICAL BUG.**

At simulated timestamp `T`, only data available at or before `T` may be used by:
- data acquisition adapters
- replay state construction
- decision engine inputs
- UI race-state views

Only the evaluator can inspect data that occurred after prediction timestamp `T`.

## Architectural boundaries

Keep clear separation between:
1. data acquisition (`src/openf1_client.py`)
2. race state (`src/race_state.py`)
3. decision engine interface (`src/laya_engine.py`)
4. replay orchestration (`src/replay_engine.py`)
5. future evaluation (`src/evaluator.py`)
6. metrics (`src/metrics.py`)
7. UI (`app.py`)

## Modeling constraints

- Never fabricate Formula 1 race data.
- Never fabricate Laya decision outputs.
- If external API behavior is unknown, leave a clear TODO/NotImplemented path.
- Never assume observed historical strategy is automatically the optimal counterfactual strategy.

## Code quality

- Use type hints and explicit error handling.
- Prefer dataclasses for structured data.
- Keep modules focused and composable.
