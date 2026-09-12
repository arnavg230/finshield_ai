from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.database import Base


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)

    alert_id = Column(
        Integer,
        ForeignKey("alerts.id"),
        nullable=False
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    status = Column(String, default="open")
    priority = Column(String, default="medium")

    findings = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    closed_at = Column(DateTime, nullable=True)