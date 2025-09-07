from pydantic import BaseModel, field_validator

class NumRequest(BaseModel):
    num: list[int]
