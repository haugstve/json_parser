from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from validate_input import Source
from transform_input import Target
from connect import DataBase


app = FastAPI()
db = DataBase("target")


@app.post("/transform")
def transform_json(input: Source):
    target = Target(input)
    return JSONResponse(content=jsonable_encoder(target))


@app.post("/validate")
def validate_json(input: Source):
    return JSONResponse(content=jsonable_encoder(input))


@app.post("/store")
def store_to_db(input: Source):
    target = Target(input)
    db.add_json_to_table(target)


@app.get("/retrive")
def retrive_all():
    return db.read_all_entries()
