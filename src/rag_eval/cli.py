import argparse,json
from pathlib import Path
from .models import EvalCase
from .local_metrics import LocalMetrics
from .adapters import RagasMetrics
from .runner import run,summarize
from .artifacts import write
from .gate import enforce
from .mlflow_logger import log
def main():
    p=argparse.ArgumentParser();p.add_argument("--dataset",required=True);p.add_argument("--out",default="artifacts")
    p.add_argument("--threshold",type=float,default=.85);p.add_argument("--backend",choices=["local","ragas"],default="local");p.add_argument("--mlflow",action="store_true")
    a=p.parse_args()
    cases=[EvalCase.model_validate_json(x) for x in Path(a.dataset).read_text().splitlines() if x.strip()]
    metric=LocalMetrics() if a.backend=="local" else RagasMetrics()
    results=run(cases,metric);summary=summarize(results);paths=write(results,summary,a.out)
    print(json.dumps(summary,indent=2))
    if a.mlflow:log(summary,paths)
    enforce(summary,a.threshold)
if __name__=="__main__":main()
