from .models import Scores
class RagasMetrics:
    """Optional real Ragas adapter. Requires ragas/datasets and provider configuration."""
    def score(self,c):
        try:
            from datasets import Dataset
            from ragas import evaluate
            from ragas.metrics import faithfulness, context_precision, answer_relevancy
        except ImportError as e:
            raise RuntimeError('Install with: pip install -e ".[ragas]"') from e
        ds=Dataset.from_dict({"question":[c.query],"answer":[c.response],"contexts":[c.contexts],
                              "ground_truth":[c.reference or c.response]})
        result=evaluate(ds,metrics=[faithfulness,context_precision,answer_relevancy])
        row=result.to_pandas().iloc[0]
        return Scores(faithfulness=float(row["faithfulness"]),
                      context_precision=float(row["context_precision"]),
                      semantic_relevancy=float(row["answer_relevancy"]))

class DeepEvalMetrics:
    """Explicit adapter boundary; use DeepEval's current metric API in your environment."""
    def score(self,c):
        raise RuntimeError("DeepEval is optional; configure provider-specific metrics before use.")
