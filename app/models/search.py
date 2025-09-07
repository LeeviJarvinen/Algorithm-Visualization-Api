from pydantic import BaseModel

class SearchRequest(BaseModel):
    data: list[int]
    target: int
