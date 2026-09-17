from .models import EvalResult
def run(cases,metric): return [EvalResult(case=c,scores=metric.score(c)) for c in cases]
def summarize(results):
    if not results:return {"faithfulness":0.0,"context_precision":0.0,"semantic_relevancy":0.0}
    return {k:sum(getattr(x.scores,k) for x in results)/len(results)
            for k in ("faithfulness","context_precision","semantic_relevancy")}
