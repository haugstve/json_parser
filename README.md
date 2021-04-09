# Python test assignment

## Assumptions

These points could have been clearified but just making some assumptions solves the task. Demonstrating my Python skills.

- If Content is present in the input JSON, it must have both a marks field and a description field
- Time in postgres is stored as UTC (Best practise would be to save with the time zone information)

## Running the app

docker-compose up -d

A web app will be running on localhost port 8000, postgres will run on 5432

Go to [docs](http://127.0.0.1:8000/docs) to se the endpoints or run the curl commands to see it in action.

### Check if the input is valid

```bash
curl --location --request POST 'localhost:8000/validate' \
--header 'Content-Type: text/plain' \
--data-raw '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},{"text": "foo"},{"text": "bar"}],"description" : "Some description"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" : 0},"type" : "main"}'
```

### Validate input, transform to target format and return

```bash
curl --location --request POST 'localhost:8000/transform' \
--header 'Content-Type: text/plain' \
--data-raw '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},{"text": "foo"},{"text": "bar"}],"description" : "Some description"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" : 0},"type" : "main"}'
```

### Validate input, transform to target format and store to DB

```bash
curl --location --request POST 'localhost:8000/store' \
--header 'Content-Type: text/plain' \
--data-raw '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},{"text": "foo"},{"text": "bar"}],"description" : "Some description"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" : 0},"type" : "main"}'
```

### Return results from the DB

```bash
curl --location --request GET 'localhost:8000/retrive'
```

## Inspect the databse

Log on to the database

```bash
PGPASSWORD=magical_password psql -h localhost -p 5432  -d rainbow_database -U unicorn_user
```

and then run the query

```SQL
SELECT * FROM target;
```

## Run the tests

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements-dev.txt
PYTHONPATH=$(pwd)/app/ python3 -m pytest -v
```
