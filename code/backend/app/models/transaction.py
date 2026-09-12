from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    transaction_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    status = Column(String, default="pending")

    fraud_score = Column(Float, nullable=True)
    aml_score = Column(Float, nullable=True)
    behavior_score = Column(Float, nullable=True)
    risk_score = Column(Float, nullable=True)
    risk_level = Column(String, nullable=True)