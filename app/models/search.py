from pydantic import BaseModel

class SearchRequest(BaseModel):
    data: list[int]
    target: int = None  

class SearchResponse(BaseModel):
    algorithm: str
    input: list[int] 
    steps: list
    result: str | list[int]
