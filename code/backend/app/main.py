from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine

app = FastAPI(title="FinShield AI Backend")


@app.get("/")
def root():
    return {"message": "FinShield AI Backend Running"}


@app.get("/db-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}