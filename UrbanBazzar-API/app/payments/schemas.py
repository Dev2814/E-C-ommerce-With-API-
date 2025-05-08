from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enum to represent different payment statuses
class PaymentStatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    processing = "processing"


# Pydantic schema for the payment details
class PaymentSchema(BaseModel):
    provider: str
    status: PaymentStatusEnum

    class Config:
        orm_mode = True
