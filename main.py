from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# this class creates a schema that takes in a str and float data
class ItemCreate(BaseModel):
    name: str
    price: float 