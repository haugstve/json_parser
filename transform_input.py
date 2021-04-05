from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin, config
from typing import List, Optional
from datetime import date
from datetime import time
from pytz import timezone

from validate_input import Source


@dataclass
class Target((DataClassJsonMixin)):
    path: str
    id: str
    author_name: str
    author_id: str
    counters_total: int
    created_date: date = field(
        metadata=config(encoder=date.isoformat, decoder=date.fromisoformat)
    )
    created_time: time = field(
        metadata=config(encoder=time.isoformat, decoder=time.fromisoformat)
    )
    updated_date: Optional[date] = field(
        metadata=config(encoder=date.isoformat, decoder=date.fromisoformat),
        default=None,
    )
    updated_time: Optional[time] = field(
        metadata=config(encoder=time.isoformat, decoder=time.fromisoformat),
        default=None,
    )
    items: Optional[List[str]] = None
    body: Optional[str] = None

    def __init__(self, source: Source):
        self.path = source.address
        if source.content:
            self.items = [mark.text for mark in source.content.marks]
            self.body = source.content.description
        self.id = source.id
        self.author_name = source.author.username
        self.author_id = source.author.id
        created_UTC = source.created.astimezone(timezone("UTC"))
        self.created_date = created_UTC.date()
        self.created_time = created_UTC.time()
        if source.updated:
            updated_UTC = source.updated.astimezone(timezone("UTC"))
            self.updated_date = updated_UTC.date()
            self.updated_time = updated_UTC.time()
        self.counters_total = source.counters.mistakes + source.counters.score
