from fastapi import FastAPI
from pydantic import BaseModel
from crack import getCode

app = FastAPI()

class CrackQuery(BaseModel):
    data_url: str

@app.post('/crack')
def crack_handler():
    return {"ans": getCode()}
