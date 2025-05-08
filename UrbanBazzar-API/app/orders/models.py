from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from models.database import Base
from app.users.models import CustomUser
from app.store.models import Product
# Avoid circular import for PaymentDetails; use string for relationship reference if needed

# Order status enumeration
class OrderStatus(PyEnum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    completed = "completed"
    cancelled = "cancelled"

# Order Details
class OrderDetails(Base):
    __tablename__ = "orders_orderdetails"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_customuser.id"), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    pincode = Column(String(10), nullable=False)
    country = Column(String(100), nullable=False)
    mobile = Column(String(15), nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("CustomUser", backref="orders")
    order_items = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
    paymentdetails = relationship("PaymentDetails", back_populates="order", uselist=False)

# Order Items
class OrderItems(Base):
    __tablename__ = "orders_orderitems"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders_orderdetails.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("store_product.id"), nullable=False)
    quantity = Column(Integer, default=1)

    order = relationship("OrderDetails", back_populates="order_items")
    product = relationship("Product")
