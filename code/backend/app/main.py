from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.database import engine, get_db

app = FastAPI(title="FinShield AI Backend")


@app.get("/")
def root():
    return {"message": "FinShield AI Backend Running"}


@app.get("/db-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}


@app.get("/db-session-test")
def database_session_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"database": result.scalar()}