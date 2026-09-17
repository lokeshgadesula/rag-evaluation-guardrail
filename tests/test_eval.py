import pytest
from rag_eval.models import EvalCase
from rag_eval.local_metrics import LocalMetrics
from rag_eval.runner import run,summarize
from rag_eval.gate import enforce,GateFailed
def test_grounded():
 c=EvalCase(id="1",query="refund window 30 days",contexts=["refund window is 30 days"],response="refund window is 30 days")
 assert run([c],LocalMetrics())[0].scores.faithfulness==1
def test_gate_pass(): enforce({"faithfulness":.9},.85)
def test_gate_fail():
 with pytest.raises(GateFailed):enforce({"faithfulness":.8},.85)
def test_summary():
 c=EvalCase(id="1",query="x",contexts=["x"],response="x")
 assert summarize(run([c],LocalMetrics()))["faithfulness"]==1
