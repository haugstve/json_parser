from validate_input import Source
from transform_input import Target
import json


def test_no_error_example_input():
    input_payload = """
    {
        "address": "https://www.google.com ",
        "content": {
            "marks": [
                {
                    "text": "marks"
                },
                {
                    "text": "season"
                }
            ],
            "description": "Some description"
        },
        "updated": "2021-02-26T08:21:20+00:00",
        "author": {
            "username": "Bob",
            "id": "68712648721648271"
        },
        "id": "543435435",
        "created": "2021-02-25T16:25:21+00:00",
        "counters": {
            "score": 3,
            "mistakes": 0
        },
        "type": "main"
    }""".strip()
    source = Source.from_json(input_payload)
    Target(source)


def test_to_json_example_input():
    input_payload = """
    {
        "address": "https://www.google.com ",
        "content": {
            "marks": [
                {
                    "text": "marks"
                },
                {
                    "text": "season"
                },
                {
                    "text": "foo"
                },
                {
                    "text": "bar"
                }
            ],
            "description": "Some description"
        },
        "updated": "2021-02-26T08:21:20+00:00",
        "author": {
            "username": "Bob",
            "id": "68712648721648271"
        },
        "id": "543435435",
        "created": "2021-02-25T16:25:21+00:00",
        "counters": {
            "score": 3,
            "mistakes": 0
        },
        "type": "main"
    }""".strip()
    source = Source.from_json(input_payload)
    target = Target(source)
    target_payload = """
    {
        "path": "https://www.google.com ",
        "items": ["marks", "season", "foo", "bar"],
        "body": "Some description",
        "id": "543435435",
        "author_name": "Bob",
        "author_id": "68712648721648271",
        "created_date": "2021-02-25",
        "created_time": "16:25:21",
        "updated_date": "2021-02-26",
        "updated_time": "08:21:20",
        "counters_total": 3
    }
    """.strip()
    assert target.to_json(sort_keys=True) == json.dumps(
        json.loads(target_payload), sort_keys=True
    )


def test_no_error_missing_content():
    input_payload = """
    {
        "address": "https://www.google.com ",
        "updated": "2021-02-26T08:21:20+00:00",
        "author": {
            "username": "Bob",
            "id": "68712648721648271"
        },
        "id": "543435435",
        "created": "2021-02-25T16:25:21+00:00",
        "counters": {
            "score": 3,
            "mistakes": 0
        },
        "type": "main"
    }
    """.strip()
    source = Source.from_json(input_payload)
    target = Target(source)
    target.to_json()


def test_no_error_missing_updated():
    input_payload = """
    {
        "address": "https://www.google.com ",
        "content": {
            "marks": [
                {
                    "text": "marks"
                },
                {
                    "text": "season"
                }
            ],
            "description": "Some description"
        },
        "author": {
            "username": "Bob",
            "id": "68712648721648271"
        },
        "id": "543435435",
        "created": "2021-02-25T16:25:21+00:00",
        "counters": {
            "score": 3,
            "mistakes": 0
        },
        "type": "main"
    }""".strip()
    source = Source.from_json(input_payload)
    target = Target(source)
    target.to_json()


def test_created_not_utc():
    input_payload = """
    {
        "address": "https://www.google.com ",
        "content": {
            "marks": [
                {
                    "text": "marks"
                },
                {
                    "text": "season"
                }
            ],
            "description": "Some description"
        },
        "updated": "2021-02-26T08:21:20+00:00",
        "author": {
            "username": "Bob",
            "id": "68712648721648271"
        },
        "id": "543435435",
        "created": "2021-02-25T16:25:21+01:00",
        "counters": {
            "score": 3,
            "mistakes": 0
        },
        "type": "main"
    }""".strip()
    source = Source.from_json(input_payload)
    target = Target(source)
    assert str(target.created_time) == "15:25:21"


def test_counters_correct():
    input_payload = """
    {
        "address": "https://www.google.com ",
        "content": {
            "marks": [
                {
                    "text": "marks"
                },
                {
                    "text": "season"
                },
                {
                    "text": "foo"
                },
                {
                    "text": "bar"
                }
            ],
            "description": "Some description"
        },
        "updated": "2021-02-26T08:21:20+00:00",
        "author": {
            "username": "Bob",
            "id": "68712648721648271"
        },
        "id": "543435435",
        "created": "2021-02-25T16:25:21+00:00",
        "counters": {
            "score": 6,
            "mistakes": 2
        },
        "type": "main"
    }""".strip()
    source = Source.from_json(input_payload)
    target = Target(source)
    assert target.counters_total == 8
