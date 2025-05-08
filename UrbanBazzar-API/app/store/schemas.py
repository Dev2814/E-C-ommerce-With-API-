from pydantic import BaseModel, root_validator
from typing import Optional, List
from datetime import datetime


# --------- Product Category Schemas ----------

class ProductCategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryResponse(ProductCategoryBase):
    id: int

    class Config:
        orm_mode = True


# --------- Product Image Schemas ----------

class ProductImageBase(BaseModel):
    image: str


class ProductImageCreate(ProductImageBase):
    pass


class ProductImageResponse(ProductImageBase):
    id: int
    product_id: int
    url: str

    class Config:
        from_attributes = True
    


# --------- TryOn Image Schemas ----------

class TryOnImageBase(BaseModel):
    image: str
    tag: Optional[str] = None


class TryOnImageCreate(TryOnImageBase):
    pass


class TryOnImageResponse(TryOnImageBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True


# --------- Product Schemas ----------

class ProductBase(BaseModel):
    name: str
    brand_name: Optional[str] = None
    description: str
    product_category_id: Optional[int] = None
    price: float
    vendor_id: Optional[int] = None
    stock: int = 0


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    product_images: List[ProductImageResponse] = []
    tryon_images: List[TryOnImageResponse] = []

    class Config:
        orm_mode = True
