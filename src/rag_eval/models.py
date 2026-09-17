from pydantic import BaseModel, Field
class EvalCase(BaseModel):
    id:str; query:str; contexts:list[str]; response:str; reference:str|None=None
class Scores(BaseModel):
    faithfulness:float=Field(ge=0,le=1)
    context_precision:float=Field(ge=0,le=1)
    semantic_relevancy:float=Field(ge=0,le=1)
class EvalResult(BaseModel):
    case:EvalCase; scores:Scores
