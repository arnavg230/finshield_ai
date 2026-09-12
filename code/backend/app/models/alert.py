from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.database.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(
        Integer,
        ForeignKey("transactions.id"),
        nullable=False
    )

    risk_score = Column(Float, nullable=False)
    risk_level = Column(String, nullable=False)
    reason = Column(String, nullable=False)

    status = Column(String, default="open")
    created_at = Column(DateTime, nullable=False)