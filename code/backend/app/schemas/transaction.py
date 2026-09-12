from datetime import datetime

from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    sender: str
    receiver: str
    transaction_type: str
    amount: float = Field(gt=0)
    timestamp: datetime


class TransactionResponse(BaseModel):
    id: int
    user_id: int
    sender: str
    receiver: str
    transaction_type: str
    amount: float
    timestamp: datetime
    status: str

    fraud_score: float | None = None
    aml_score: float | None = None
    behavior_score: float | None = None
    risk_score: float | None = None
    risk_level: str | None = None

    class Config:
        from_attributes = True