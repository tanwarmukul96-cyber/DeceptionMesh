#  DeceptionMesh

An adaptive cybersecurity deception framework designed to detect attacker behaviour, analyze interaction patterns, and dynamically evolve deception mechanisms.

##  Overview

DeceptionMesh is a modular cybersecurity project that simulates a defensive deception environment.

The system:
- Collects attacker interaction events
- Analyzes behavioural patterns
- Calculates risk and confidence
- Tracks Deception DNA
- Adapts deception based on attacker behaviour
- Maintains mutation history
- Generates attacker intelligence reports

##  Architecture

DeceptionMesh is organized into modular components:

- `core/` — Core project functionality
- `decoys/` — Deception and decoy management
- `dna/` — Behavioural DNA, scoring and evolution
- `adaptation/` — Adaptive deception engine
- `services/` — Behaviour analysis and event collection
- `models/` — Data models
- `reports/` — Generated intelligence reports
- `tests/` — Pipeline and adaptation tests

##  Adaptive Deception Loop

```text
Attacker Interaction
        ↓
Event Collection
        ↓
Behaviour Analysis
        ↓
Risk Scoring
        ↓
Deception DNA
        ↓
Adaptive Decision
        ↓
Decoy Mutation
        ↓
New Attacker Interaction
        ↺

``` 

## Key Features
Behaviour-based attacker analysis
Risk scoring and confidence evaluation
Adaptive deception decisions
Dynamic decoy evolution
Interaction-depth tracking
Mutation history logging
Attacker intelligence reporting
Modular architecture
## Example Behaviour

The system can distinguish between different interaction levels such as:

repeated_interaction
deep_interaction

Higher-risk interaction can trigger deeper deception strategies such as an advanced-decoy.

## Technologies
Python
Cybersecurity
Threat Detection
Behaviour Analysis
Deception Technology
Git & GitHub


## Running the Project

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the main application

```bash
python main.py
```

### 5. Run the pipeline tests

```bash
python -m tests.test_pipeline
```

### 6. Run the adaptation loop tests

```bash
python -m tests.test_adaptation_loop
```

