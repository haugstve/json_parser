from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class Text(BaseModel):
    text: str


class Content(BaseModel):
    marks: List[Text]
    description: str


class Author(BaseModel):
    username: str
    id: str


class Counters(BaseModel):
    score: int
    mistakes: int


class Source(BaseModel):
    address: str
    id: str
    author: Author
    created: datetime
    counters: Counters
    updated: Optional[datetime]
    content: Optional[Content]