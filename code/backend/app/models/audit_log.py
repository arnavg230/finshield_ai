from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    action = Column(String, nullable=False)
    details = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)