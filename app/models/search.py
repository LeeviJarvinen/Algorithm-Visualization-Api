from pydantic import BaseModel

class SearchRequest(BaseModel):
    data: list[int]
    target: int

class Step(BaseModel):
    step: int
    action: str
    found: bool

class SearchResponse(BaseModel):
    algorithm: str
    input: list[int] 
    steps: list[Step] = None
    result: str
