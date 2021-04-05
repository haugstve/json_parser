from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin, config
from typing import List
from datetime import date
from datetime import time

from validate_input import Source


@dataclass
class Target((DataClassJsonMixin)):
    path: str
    items: List[str]
    body: str
    id: str
    author_name: str
    author_id: str
    created_date: date = field(
        metadata=config(encoder=date.isoformat, decoder=date.fromisoformat)
    )
    created_time: time = field(
        metadata=config(encoder=time.isoformat, decoder=time.fromisoformat)
    )
    updated_date: date = field(
        metadata=config(encoder=date.isoformat, decoder=date.fromisoformat)
    )
    updated_time: time = field(
        metadata=config(encoder=time.isoformat, decoder=time.fromisoformat)
    )
    counters_total: int

    def __init__(self, source: Source):
        self.path = source.address
        if source.content:
            self.items = [mark.text for mark in source.content.marks]
            self.body = source.content.description
        self.id = source.id
        self.author_name = source.author.username
        self.author_id = source.author.id
        self.created_date = source.created.date()
        self.created_time = source.created.time()
        if source.updated:
            self.updated_date = source.updated.date()
            self.updated_time = source.updated.time()
        self.counters_total = source.counters.mistakes + source.counters.score
