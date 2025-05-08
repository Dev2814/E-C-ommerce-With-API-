from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.database import Base  


class ProductCategory(Base):
    __tablename__ = "store_productcategory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    products = relationship("Product", back_populates="product_category", cascade="all, delete-orphan")

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = "store_product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=True)
    description = Column(Text, nullable=False)
    product_category_id = Column(Integer, ForeignKey("store_productcategory.id"), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    vendor_id = Column(Integer, ForeignKey("users_customuser.id"), nullable=True)  # Correct table name
    stock = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    product_category = relationship("ProductCategory", back_populates="products")
    vendor = relationship("CustomUser", back_populates="products") 
    product_images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    tryon_images = relationship("TryOnImage", back_populates="product", cascade="all, delete-orphan")

    def __str__(self):
        return self.name


class ProductImage(Base):
    __tablename__ = "store_productimage"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("store_product.id"))
    image = Column(String, nullable=False)

    product = relationship("Product", back_populates="product_images")

    def __str__(self):
        return f"Image for {self.product.name}"


class TryOnImage(Base):
    __tablename__ = "store_tryonimage"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("store_product.id"))
    image = Column(String, nullable=False)
    tag = Column(String(100), nullable=True)

    product = relationship("Product", back_populates="tryon_images")

    def __str__(self):
        return f"Try-On Image for {self.product.name}"