from pydantic import BaseModel


class Operation(BaseModel):
    op: str
    