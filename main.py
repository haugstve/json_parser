from fastapi import FastAPI
import uvicorn

from validate_input import Source
from transform_input import Target

app = FastAPI()


@app.post("/transform")
def transform_json(input: Source):
    target = Target(input)
    return target.to_json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
