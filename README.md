# Python test assignment

## Assumptions

These points could have been clearified but just making some assumptions solves the task. Demonstrating my Python skills.

- If Content is present in the input JSON, it must have both a marks field and a description field
- Time in postgres is stored as UTC

## Running the app

docker compose up

A web app will be running on localhost port 8000

Go to [docs](http://127.0.0.1:8000/docs) to se the endpoints or run the curl commands to see it in action

```bash
curl --location --request POST 'localhost:8000/validate' \
--header 'Content-Type: text/plain' \
--data-raw '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},{"text": "foo"},{"text": "bar"}],"description" : "Some description"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" : 0},"type" : "main"}'
```

```bash
curl --location --request POST 'localhost:8000/transform' \
--header 'Content-Type: text/plain' \
--data-raw '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},{"text": "foo"},{"text": "bar"}],"description" : "Some description"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" : 0},"type" : "main"
```

## Run the tests

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements-dev.txt
PYTHONPATH=$(pwd)/src/ python3 -m pytest -v
```
