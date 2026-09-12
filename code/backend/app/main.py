from fastapi import FastAPI
from sqlalchemy import text

from app.auth.router import router as auth_router
from app.database.database import engine, Base
from app.models import User, Transaction, Alert, Case, AuditLog
from app.transactions.router import router as transaction_router

app = FastAPI(title="FinShield AI Backend")


Base.metadata.create_all(bind=engine)


app.include_router(auth_router)
app.include_router(transaction_router)

@app.get("/")
def root():
    return {"message": "FinShield AI Backend Running"}


@app.get("/db-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}