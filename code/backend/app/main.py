from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine, Base
from app.models import User, Transaction, Alert, Case, AuditLog

app = FastAPI(title="FinShield AI Backend")


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "FinShield AI Backend Running"}


@app.get("/db-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}