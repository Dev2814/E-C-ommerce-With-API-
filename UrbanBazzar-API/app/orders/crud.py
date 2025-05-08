from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.orders.models import OrderDetails, OrderItems
from app.orders.schemas import OrderDetailsCreate, OrderDetailsResponse, OrderItemCreate
from app.store.models import Product


def create_order(db: Session, order: OrderDetailsCreate, user_id: int):
    # Create order object
    db_order = OrderDetails(
        user_id=user_id,
        address=order.address,
        city=order.city,
        pincode=order.pincode,
        country=order.country,
        mobile=order.mobile,
        total=order.total,
        status=order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Add order items and update stock
    for item in order.items:
        db_item = OrderItems(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_item)
        db.commit()

        # Decrease stock (assuming this part is done via SQLAlchemy)
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            product.stock -= item.quantity
            db.commit()

    return db_order


def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(OrderDetails).filter(OrderDetails.user_id == user_id).offset(skip).limit(limit).all()
