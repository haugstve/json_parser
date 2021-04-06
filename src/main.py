from fastapi import FastAPI
import uvicorn

from validate_input import Source
from transform_input import Target

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.post("/transform")
def transform_json(input: Source):
    target = Target(input)
    return JSONResponse(content=jsonable_encoder(target))


@app.post("/validate")
def validate_json(input: Source):
    return JSONResponse(content=jsonable_encoder(input))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
