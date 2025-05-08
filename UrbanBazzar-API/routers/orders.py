from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List

# Import models and dependencies
from app.orders.models import OrderDetails, OrderItems, OrderStatus
from app.cart.models import CartItem, ShoppingSession
from app.payments.models import PaymentDetails
from app.store.models import Product
from models.database import get_db
from app.orders.schemas import OrderCreateSchema, OrderResponseSchema
from app.dependencies import get_current_user
from app.users.models import CustomUser

router = APIRouter()

# Confirm order 
@router.post("/", response_model=OrderResponseSchema)
def create_order(
    order_data: OrderCreateSchema,  # Incoming request data
    db: Session = Depends(get_db),  # Inject database session
    current_user: CustomUser = Depends(get_current_user)  # Get current logged-in user
):
    # Get the current user's shopping session
    session = db.query(ShoppingSession).filter_by(user_id=current_user.id).first()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shopping session not found.")

    # Get all cart items for the session
    cart_items = db.query(CartItem).filter_by(session_id=session.id).all()
    if not cart_items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Your cart is empty.")

    # Calculate total amount from cart items
    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    # Create the order with address and total
    order = OrderDetails(
        user_id=current_user.id,
        address=order_data.address,
        city=order_data.city,
        pincode=order_data.pincode,
        country=order_data.country,
        mobile=order_data.mobile,
        total=total_amount,
        status=OrderStatus.pending,  # Default status
    )
    db.add(order)
    db.commit()
    db.refresh(order)  # Get order ID after creation

    # Create order items and update product stock
    for item in cart_items:

        product = db.query(Product).filter_by(id=item.product_id).with_for_update().first()
        if not product or product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock for {product.name if product else 'unknown product'}."
            )

        # Create order item
        order_item = OrderItems(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(order_item)

        # Update product stock
        product = db.query(Product).filter_by(id=item.product_id).first()
        if product:
            if product.stock < item.quantity:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not enough stock for {product.name}.")
            product.stock -= item.quantity  # Deduct purchased quantity

    db.commit()

    # Create payment details
    payment = PaymentDetails(
        order_id=order.id,
        amount=total_amount,
        provider=order_data.payment_method,
        status="pending" if order_data.payment_method.lower() == "cod" else "processing",  
    )
    db.add(payment)
    db.commit()

    # Link payment ID to order
    order.payment_id = payment.id
    db.commit()

    # Clear the cart after successful order
    db.query(CartItem).filter_by(session_id=session.id).delete()
    db.commit()

    # Reload order with related order items and payment info
    order_with_items = db.query(OrderDetails)\
        .options(
            joinedload(OrderDetails.order_items), 
            joinedload(OrderDetails.paymentdetails)
        )\
        .filter(OrderDetails.id == order.id)\
        .first()

    return order_with_items  # Return complete order details with nested info

# Endpoint to list all orders for the current user
@router.get("/", response_model=List[OrderResponseSchema])
def list_orders(
    db: Session = Depends(get_db),
    current_user: CustomUser = Depends(get_current_user)
):
    # Fetch all orders for the user with order items
    orders = db.query(OrderDetails)\
        .options(joinedload(OrderDetails.order_items))\
        .filter_by(user_id=current_user.id)\
        .order_by(OrderDetails.created_at.desc())\
        .all()
    return orders
