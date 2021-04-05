from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin, config
from typing import List
from datetime import datetime
from marshmallow import fields


@dataclass(frozen=True)
class Text(DataClassJsonMixin):
    text: str


@dataclass(frozen=True)
class Content(DataClassJsonMixin):
    marks: List[Text]
    description: str


@dataclass(frozen=True)
class Author(DataClassJsonMixin):
    username: str
    id: str


@dataclass(frozen=True)
class Counters(DataClassJsonMixin):
    score: int
    mistakes: int


@dataclass
class Input((DataClassJsonMixin)):
    address: str
    content: Content
    id: str
    author: Author
    created: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    updated: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    counters: Counters
