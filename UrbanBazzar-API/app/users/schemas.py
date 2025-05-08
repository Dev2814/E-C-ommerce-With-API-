from pydantic import BaseModel, EmailStr,  Field
from typing import List, Optional
from enum import Enum
from datetime import datetime


# Role Enum
class RoleEnum(str, Enum):
    admin = "admin"
    vendor = "vendor"
    buyer = "buyer"


# User Schema (for creating a new user)
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: RoleEnum = RoleEnum.buyer


# User Schema (for returning user details)
class User(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: RoleEnum
    is_active: bool
    is_superuser: bool
    is_staff: bool
    created_at: datetime

    class Config:
        orm_mode = True


# User Response Schema (for returning user details)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: RoleEnum
    is_active: bool
    is_superuser: bool
    is_staff: bool
    # created_at: datetime

    class Config:
        orm_mode = True


# Address Schema
class BaseAddress(BaseModel):
    address: str
    city: str
    pincode: str
    country: str
    mobile: str


# User Address Schema
class UserAddress(BaseAddress):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# User Secondary Address Schema
class UserSecondaryAddress(BaseAddress):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Address Creation Schema (for creating new addresses)
class AddressCreate(BaseModel):
    address: str
    city: str
    pincode: str
    country: str
    mobile: str

    class Config:
        orm_mode = True

class AddressResponse(BaseAddress):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # for Pydantic v2+


# Secondary Address Creation Schema (for creating new secondary addresses)
class SecondaryAddressCreate(BaseModel):
    address: str
    city: str
    pincode: str
    country: str
    mobile: str

    class Config:
        orm_mode = True
        
class SecondaryAddressResponse(BaseAddress):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Payment Schema
class UserPayment(BaseModel):
    id: int
    user_id: int
    payment_type: str
    provider: str
    account_no: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Payment Creation Schema
class PaymentCreate(BaseModel):
    payment_type: str
    provider: str
    account_no: str

    class Config:
        orm_mode = True

class PaymentResponse(BaseModel):
    id: int
    user_id: int
    payment_type: str
    provider: str
    account_no: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 


# Password Reset Schema (for resetting a user's password)
class PasswordResetByHash(BaseModel):
    hashed_user_id: str
    new_password: str = Field(..., min_length=6)
    confirm_password: str


# OTP Verification Schema (for verifying the OTP)
class OTPVerify(BaseModel):
    email: EmailStr
    otp: str


# User Login Schema (for user login)
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Tocken Schema     
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    message: str

class PasswordResetByToken(BaseModel):
    token: str
    new_password: str
    confirm_password: str
