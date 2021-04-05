from validate_input import Source
import pytest


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
    Source.from_json(input_payload)


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
    Source.from_json(input_payload)


def test_error_when_missing_address():
    input_payload = """
    {
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
    with pytest.raises(KeyError):
        Source.from_json(input_payload)


def test_error_when_dateformat_is_wrong():
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
        "updated": "2021/02/26T08:21:20+00:00",
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
    with pytest.raises(ValueError):
        Source.from_json(input_payload)


def test_error_when_path_used_as_input():
    input_payload = """
    {
        "path": "https://www.google.com ",
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
    with pytest.raises(KeyError):
        Source.from_json(input_payload)
