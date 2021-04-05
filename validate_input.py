from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin, config
from typing import List, Optional
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


# Hack, https://github.com/lidatong/dataclasses-json/issues/254
def datetime_fromisoformat(input):
    if input:
        return datetime.fromisoformat(input)
    return None


@dataclass
class Source((DataClassJsonMixin)):
    address: str
    id: str
    author: Author
    created: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        )
    )
    counters: Counters
    updated: Optional[datetime] = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime_fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
        default=None,
    )
    content: Optional[Content] = None
