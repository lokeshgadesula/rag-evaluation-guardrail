import csv,json
from pathlib import Path
def write(results,summary,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    with (out/"results.csv").open("w",newline="") as f:
        w=csv.writer(f);w.writerow(["id","faithfulness","context_precision","semantic_relevancy"])
        for x in results:w.writerow([x.case.id,x.scores.faithfulness,x.scores.context_precision,x.scores.semantic_relevancy])
    return [out/"summary.json",out/"results.csv"]
