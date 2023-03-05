"""Modules"""
import uvicorn
from fastapi import FastAPI
from . import schema

app = FastAPI()

@app.get('/')
def index():
    """ Initial root"""
    return {'message': 'Welcome to Logo Prediction app'}

@app.post("/items")
async def root(item: schema.LogoInfo):
    return [{'message':item}]

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



"""
uvicorn main:app --reload
"""
