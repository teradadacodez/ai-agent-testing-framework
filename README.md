# Agent Testing Framework

A modular and extensible framework to -evaluate any AI agent- using predefined test cases, automated scoring, and adversarial testing.

---

## Overview

Most AI systems fail not due to weak models, but due to:

- Lack of systematic testing
- Missing safety validation
- No evaluation pipeline

This project solves that by providing a -plug-and-play evaluation framework- for AI agents.

---

## Features

-- Agent-agnostic design (`run_agent()` interface)
-- Structured test case system
-- LLM-as-a-Judge evaluation (using Qwen3.5:9B)
-- Rule-based safety validation
-- Adversarial testing support
-- Metrics computation (accuracy, relevance, safety)
-- Category-wise performance breakdown
-- Latency tracking
-- Failure analysis
-- JSON-based logging & reporting

---

## Project Structure

```
repo/
├── data/
│   ├── test_cases.json
│   ├── results.json
│   ├── judgements.json
│   └── testcases_explain.txt
│
├── src/
│   ├── agent.py
│   ├── evaluator.py
│   ├── runner.py
│   ├── llm.py
│   ├── adversarial.py
│   └── config.py
│
├── evaluation/
│   └── metrics.py
│
├── report/
│
├── main.py
├── ARCHITECTURE.md
├── README.md
├── requirements.txt
```

---

## How It Works

```
Test Cases → Agent → Results → Evaluator → Judgements → Metrics → Report
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd agent-testing-framework
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Install & Run Ollama

Download:
    https://ollama.com

Run models:

```
ollama run llama3.2
ollama run llama3.2:1b
```

---

## Running the Framework

```
python main.py
```

---

## Output Files

- `results.json` → Agent outputs
- `judgements.json` → Evaluation scores
- `metrics` → Computed dynamically

---

## Test Case Categories

- Normal- → basic queries
- Edge- → ambiguous / empty inputs
- Adversarial- → prompt injection, jailbreaks
- Safety- → harmful requests

---

## Evaluation Methodology

### LLM-as-a-Judge

- Model: `qwen3.5:9b`
- Evaluates:

  - Correctness
  - Relevance
  - Safety

### Rule-Based Checks

- Keyword filtering (e.g., "bomb", "hack")
- Overrides unsafe outputs

---

## Metrics

- Accuracy Score
- Relevance Score
- Safety Score
- Overall Score
- Category-wise breakdown
- Latency statistics

---

## Failure Detection

Failures are identified when:

- Low correctness (< threshold)
- Unsafe outputs detected

---

## Extending the Framework

To plug in your own agent:

```python
def run_agent(input: str) -> str:
    ...
```

No other changes required.

---

## Key Highlights

- Modular architecture
- Clean separation of concerns
- Real-world adversarial testing
- Scalable evaluation pipeline

---

## Use Cases

- Benchmarking LLMs
- Testing chatbot safety
- Evaluating AI assistants
- Research & experimentation

---

## 📌 Future Improvements

- Dashboard UI
- Parallel test execution
- Advanced adversarial generation
- Multi-agent comparison

---

## Author

Tanmay Jain
AI Intern Candidate


`Do check out my other repo(s) :)`