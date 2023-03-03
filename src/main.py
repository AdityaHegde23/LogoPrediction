"""Modules"""
from fastapi import FastAPI
from . import schema

app = FastAPI()


@app.post("/items")
async def root(item: schema.Item):
    """ Initial root"""
    return {item}
