from typing import List
from pydantic import BaseModel

class EventDate(BaseModel):
    date: str

class Event(BaseModel):
    name: str
    dates: List[EventDate]

class Vote(BaseModel):
    name: str
    votes: List[EventDate]