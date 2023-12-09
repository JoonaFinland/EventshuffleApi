from typing import List
from pydantic import BaseModel, constr, validator
from datetime import datetime
import re

DATE_FORMAT_REGEX = r'\d{4}-\d{2}-\d{2}'

def validate_date_format(value):
    if not re.match(DATE_FORMAT_REGEX, value):
        raise ValueError("Invalid date format. Must be in 'yyyy-mm-dd' format.")
    return value

class Event(BaseModel):
    name: str
    dates: List[constr(strict=True)]

    @validator("dates", each_item=True)
    def validate_date_format(cls, value):
        return validate_date_format(value)

class Vote(BaseModel):
    name: str
    dates: List[constr(strict=True)]

    @validator("dates", each_item=True)
    def validate_date_format(cls, value):
        return validate_date_format(value)