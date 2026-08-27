# 🛡️ DeceptionMesh

An adaptive cybersecurity deception framework designed to detect attacker behaviour, analyze interaction patterns, and dynamically evolve deception mechanisms.

## 🚀 Overview

DeceptionMesh is a modular cybersecurity project that simulates a defensive deception environment.

The system:
- Collects attacker interaction events
- Analyzes behavioural patterns
- Calculates risk and confidence
- Tracks Deception DNA
- Adapts deception based on attacker behaviour
- Maintains mutation history
- Generates attacker intelligence reports

## 🧠 Architecture

DeceptionMesh is organized into modular components:

- `core/` — Core project functionality
- `decoys/` — Deception and decoy management
- `dna/` — Behavioural DNA, scoring and evolution
- `adaptation/` — Adaptive deception engine
- `services/` — Behaviour analysis and event collection
- `models/` — Data models
- `reports/` — Generated intelligence reports
- `tests/` — Pipeline and adaptation tests

## 🔄 Adaptive Deception Loop

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
Create and activate a virtual environment:

python -m venv venv

Activate on Windows:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run the main application:

python main.py

Run the pipeline:

python -m tests.test_pipeline

Run the adaptation loop:

python -m tests.test_adaptation_loop