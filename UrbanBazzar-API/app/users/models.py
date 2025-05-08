from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from models.database import Base

# Role Enum
class RoleEnum(PyEnum):
    admin = "admin"
    vendor = "vendor"
    buyer = "buyer"

# Custom User Model
class CustomUser(Base):
    __tablename__ = "users_customuser"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.buyer)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    # created_at = Column(DateTime, default=datetime.utcnow)

    # reset_link_used = Column(Boolean, default=False)

    addresses = relationship("UserAddress", back_populates="user")
    secondary_addresses = relationship("UserSecondaryAddress", back_populates="user")
    payments = relationship("UserPayment", back_populates="user")
    products = relationship("Product", back_populates="vendor")
    


# Base address model (abstract concept)
class BaseAddress:
    address = Column(String(255))
    city = Column(String(100))
    pincode = Column(String(10))
    country = Column(String(100))
    mobile = Column(String(15))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Primary Address
class UserAddress(Base, BaseAddress):
    __tablename__ = "users_useraddress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_customuser.id"))
    user = relationship("CustomUser", back_populates="addresses")


# Secondary Address
class UserSecondaryAddress(Base, BaseAddress):
    __tablename__ = "users_usersecondaryaddress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_customuser.id"))
    user = relationship("CustomUser", back_populates="secondary_addresses")


# Payment Information
class UserPayment(Base):
    __tablename__ = "users_userpayment"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_customuser.id"))
    payment_type = Column(String(50))
    provider = Column(String(50))
    account_no = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("CustomUser", back_populates="payments")

class PasswordResetToken(Base):
    __tablename__ = "users_passwordresettoken"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_customuser.id"), nullable=False)
    token = Column(String(100), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
