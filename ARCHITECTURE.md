# Architecture Overview

This document explains the internal design of the --Agent Testing Framework--.

---

## System Design

```
                ┌──────────────────┐
                │   Test Cases     │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Test Runner    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │      Agent       │
                │ (generator_llm)  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │     Results      │
                │  (results.json)  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Evaluator      │
                │ (LLM-as-Judge)   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Judgements     │
                │ (judgements.json)│
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Metrics       │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │     Report       │
                └──────────────────┘
```

---

## Components

---

### 1. Agent (`src/agent.py`)

- Provides a standard interface:

```python
def run_agent(input: str) -> str
```

- Uses `generator_llm()` internally
- Can be replaced with any AI system

---

### 2. LLM Layer (`src/llm.py`)

Handles communication with models:

- `generator_llm()` → response generation
- `evaluator_llm()` → evaluation model

Supports:

- Ollama local models
- Extendable to APIs

---

### 3. Test Runner (`src/runner.py`)

Responsibilities:

- Iterates through test cases
- Calls agent
- Measures latency
- Stores results

---

### 4. Evaluator (`src/evaluator.py`)

#### LLM-as-a-Judge

- Uses `qwen3.5:9b`
- Produces:

  - correctness
  - relevance
  - safety

#### Rule-Based Validation

- Keyword filtering
- Safety override logic

---

### 5. Data Layer (`data/`)

| File            | Purpose            |
| --------------- | ------------------ |
| test_cases.json | Input dataset      |
| results.json    | Agent outputs      |
| judgements.json | Evaluation results |

---

### 6. Metrics Engine (`evaluation/metrics.py`)

Computes:

- Aggregate scores
- Category-wise performance
- Normalization (1–10 → 0–1)

---

### 7. Reporting Layer (`report/`)

Generates:

- Summary metrics
- Failure analysis
- Latency insights

---

## Data Flow

1. Load test cases
2. Run agent → generate outputs
3. Store results
4. Evaluate outputs
5. Store judgements
6. Compute metrics
7. Generate report

---

## Key Design Principles

---

### 1. Agent-Agnostic Design

Any system can plug into:

```python
run_agent(input: str) -> str
```

---

### 2. Separation of Concerns

| Layer     | Responsibility |
| --------- | -------------- |
| Agent     | Generation     |
| Evaluator | Scoring        |
| Metrics   | Aggregation    |
| Report    | Presentation   |

---

### 3. Modular Architecture

Each module:

- Independent
- Replaceable
- Testable

---

### 4. Robustness

- Handles invalid JSON
- Filters bad IDs
- Prevents crashes

---

### 5. Extensibility

Easily extendable for:

- New models
- New metrics
- New evaluation strategies

---

## Evaluation Strategy

### Hybrid Approach:

1. --LLM-based evaluation--
2. --Rule-based safety checks--

Final safety = `min(LLM, Rule)`

---

## Performance Considerations

- Sequential execution (can be parallelized)
- Latency tracking included
- Local inference (Ollama)

---

## Future Enhancements

- Parallel processing
- Dashboard visualization
- Real-time monitoring
- Multi-agent benchmarking

---

## Summary

This system provides a --complete evaluation pipeline-- for AI agents with:

- Standardized interface
- Automated scoring
- Safety validation
- Detailed reporting

It is designed to be:

> Modular, extensible, and production-ready
