from fastapi import FastAPI
from contextlib import asynccontextmanager

from .db.databes import engine,SessionLocal, get_db, BASE

# BASE.metadata.create_all(engine)



app = FastAPI()



@app.get("/")
def read_root():
  return {f'this frist Python FastAPI DEMO'}