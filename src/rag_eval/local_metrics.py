import re
from .models import EvalCase,Scores
STOP={"the","a","an","is","are","was","were","to","of","and","or","in","on","for","with","what","how"}
def toks(s): return {x for x in re.findall(r"[a-z0-9]+",s.lower()) if x not in STOP}
def recall(a,b):
    a,b=toks(a),toks(b)
    return len(a&b)/max(1,len(a))
class LocalMetrics:
    def score(self,c:EvalCase):
        context=" ".join(c.contexts)
        faith=recall(c.response,context)
        cp=sum(recall(x,c.query) for x in c.contexts)/max(1,len(c.contexts))
        rel=recall(c.query,c.response)
        return Scores(faithfulness=faith,context_precision=cp,semantic_relevancy=rel)
