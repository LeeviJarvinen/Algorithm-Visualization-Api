from pydantic import BaseModel

class Request(BaseModel):
    data: list[int]
    target: int = None

class Response(BaseModel):
    algorithm: str
    input: list[int] 
    steps: list
    result: str | list[int]
