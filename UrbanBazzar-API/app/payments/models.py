from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from models.database import Base


class PaymentStatus(PyEnum):
    pending = "pending"
    completed = "completed"
    failed = "failed"


class PaymentDetails(Base):
    __tablename__ = "payments_paymentdetails"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders_orderdetails.id"), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    provider = Column(String(100), nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    order = relationship("OrderDetails", back_populates="paymentdetails")
