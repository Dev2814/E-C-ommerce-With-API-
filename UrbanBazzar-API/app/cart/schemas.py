from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal

# Base schema for a cart item (common fields for create/update)
class CartItemBase(BaseModel):
    product_id: int  
    quantity: int = 1  

# Schema for creating a new cart item (inherits from base)
class CartItemCreate(CartItemBase):
    pass

# Schema for updating a cart item (e.g., change quantity or action like remove)
class CartItemUpdate(BaseModel):
    action: str = None  
    quantity: int = None


# Schema for returning cart item details to the client
class CartItemOut(BaseModel):
    id: int  
    product_id: int 
    quantity: int
    subtotal: Optional[Decimal]  
    product_name: str
    product_category: str
    product_brand:str
    price: float
    image: Optional[str] = None 

    class Config:
        orm_mode = True  # Pydantic ORM support for SQLAlchemy models

# Shopping session schema for returning cart details
class ShoppingSessionOut(BaseModel):
    id: int  
    user_id: int  
    total: Optional[Decimal] 
    cart_items: List[CartItemOut] 

    class Config:
        orm_mode = True  

# User Address schema for creating and viewing addresses
class UserAddressBase(BaseModel):
    address_line1: str  
    address_line2: Optional[str] = None  
    city: str  
    state: str 
    postal_code: str  
    country: str  

# Create address schema (inherit from UserAddressBase)
class UserAddressCreate(UserAddressBase):
    pass

# Returnable address schema
class UserAddressOut(UserAddressBase):
    id: int 

    class Config:
        orm_mode = True  

# User Secondary Address schema (if applicable)
class UserSecondaryAddressOut(UserAddressBase):
    id: int  

    class Config:
        orm_mode = True  

# Payment Details schema
class PaymentDetailsOut(BaseModel):
    id: int  
    amount: Decimal 
    payment_method: str  
    payment_status: str  

    class Config:
        orm_mode = True  

