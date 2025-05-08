from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Float
from sqlalchemy.orm import relationship
from models.database import Base

# CartItem model
class CartItem(Base):
    __tablename__ = 'cart_cartitem'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('cart_shoppingsession.id'))  
    product_id = Column(Integer, ForeignKey('store_product.id'))
    quantity = Column(Integer, default=1)

    # Relationships
    shopping_session = relationship('ShoppingSession', back_populates='cart_items')
    product = relationship('Product')

# ShoppingSession model
class ShoppingSession(Base):
    __tablename__ = 'cart_shoppingsession'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users_customuser.id'))
    total = Column(Integer, default=0)

    cart_items = relationship('CartItem', back_populates='shopping_session')