from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum
from app.payments.schemas import * 

# Enum to represent allowed order statuses
class OrderStatusEnum(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    completed = "completed"
    cancelled = "cancelled"

# Schema for creating a new order
class OrderCreateSchema(BaseModel):
    address: str
    city: str
    pincode: str
    country: str
    mobile: str
    payment_method: str  # e.g., "cod" or "upi"

# Schema for each item in an order
class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

# Full response schema for an order, including items and payment details
class OrderResponseSchema(BaseModel):
    id: int
    address: str
    city: str
    pincode: str
    country: str
    mobile: str
    total: float
    status: OrderStatusEnum
    created_at: datetime
    updated_at: datetime
    order_items: List[OrderItemSchema] = [] 
    paymentdetails: Optional[PaymentSchema]

    class Config:
        orm_mode = True
