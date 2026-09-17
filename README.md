# Automated RAG Evaluation & Hallucination Guardrail Engine

Runnable portfolio project for evaluating RAG query/context/response triplets and blocking regressions.

## Included
- Python evaluation harness with typed datasets
- Faithfulness, context precision, semantic relevancy
- Deterministic local evaluator for CI
- Optional Ragas adapter (`pip install -e ".[ragas]"`)
- DeepEval adapter boundary
- Configurable faithfulness deployment gate (default 0.85)
- Baseline regression comparison
- JSON/CSV artifacts
- Optional MLflow logging (`pip install -e ".[mlflow]"`)
- Docker + GitHub Actions

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m rag_eval.cli --dataset data/sample.jsonl --out artifacts
```

The sample dataset is synthetic.

## CI gate
```bash
python -m rag_eval.cli --dataset data/sample.jsonl --out artifacts --threshold 0.85
```
The process exits non-zero when mean faithfulness is below the threshold.

## MLflow
Add `--mlflow` after installing the MLflow extra. Metrics and generated artifacts are logged to the active MLflow run.
