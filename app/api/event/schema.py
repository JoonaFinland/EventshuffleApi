from typing import List
from pydantic import BaseModel

class Event(BaseModel):
    name: str
    dates: List[str]

class Vote(BaseModel):
    name: str
    dates: List[str]