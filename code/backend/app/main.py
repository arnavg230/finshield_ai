from fastapi import FastAPI

app = FastAPI(title="FinShield AI Backend")


@app.get("/")
def root():
    return {"message": "FinShield AI Backend Running"}