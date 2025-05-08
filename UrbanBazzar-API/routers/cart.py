# Import necessary modules and dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.database import get_db
from app.cart import models, schemas
from app.users.models import CustomUser  
from app.store.models import Product
from app.dependencies import get_current_user
from config import FAST_API_URL, DJANGO_URL

# Create a router for the cart endpoints
router = APIRouter()
FASTAPI_URL = FAST_API_URL

# Endpoint to add a product to the cart
@router.post("/add/{product_id}", response_model=schemas.CartItemOut)
def add_to_cart(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: CustomUser = Depends(get_current_user)
):
    # Fetch the product by ID
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Correct: checks the stock of the specific product
    if product.stock == 0: 
        raise HTTPException(status_code=400, detail="Product is out of stock")

    # Check if the user already has a shopping session (cart)
    session = db.query(models.ShoppingSession).filter_by(user_id=current_user.id).first()
    if not session:
        # Create new shopping session if none exists
        session = models.ShoppingSession(user_id=current_user.id)
        db.add(session)
        db.commit()
        db.refresh(session)

    # Check if the product is already in the cart
    cart_item = db.query(models.CartItem).filter_by(session_id=session.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1  # If exists, increase the quantity
    else:
        # Otherwise, create a new cart item
        cart_item = models.CartItem(session_id=session.id, product_id=product_id, quantity=1)
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)

    # Calculate subtotal for the item
    subtotal = cart_item.quantity * product.price

    # Return detailed cart item info
    return schemas.CartItemOut(
        id=cart_item.id,
        product_id=cart_item.product_id,
        quantity=cart_item.quantity,
        subtotal=subtotal,
        product_name=product.name,
        product_brand=product.brand_name,
        price=product.price,
        product_category=product.product_category.name if product.product_category else None
    )


# Endpoint to view all items in the user's cart
@router.get("/view", response_model=schemas.ShoppingSessionOut)
def view_cart(
    db: Session = Depends(get_db),
    current_user: CustomUser = Depends(get_current_user)
):
    # Get the shopping session for the user
    session = db.query(models.ShoppingSession).filter_by(user_id=current_user.id).first()
    if not session:
        raise HTTPException(status_code=404, detail="No shopping session found")

    # Get all cart items for that session
    items = db.query(models.CartItem).filter_by(session_id=session.id).all()

    cart_items_out = []
    for ci in items:
        product = ci.product  # Get the product associated with the cart item
        cart_items_out.append({
            "id": ci.id,
            "product_id": product.id,
            "product_name": product.name,
            "product_category": product.product_category.name if product.product_category else None,
            "product_brand": product.brand_name,
            "price": float(product.price),
            "quantity": ci.quantity,
            "subtotal": float(ci.quantity * product.price),
            "image": f"{FASTAPI_URL}/media/{product.product_images[0].image}" if product.product_images else None
        })

    # Calculate the total for the cart
    total = sum(item["subtotal"] for item in cart_items_out)

    # Return session info and all cart items
    return {
        "id": session.id,
        "user_id": session.user_id,
        "total": total,
        "cart_items": cart_items_out
    }


# Endpoint to update a cart item (increase/decrease quantity or set specific quantity)
@router.post("/update/{item_id}")
def update_cart_item(
    item_id: int,
    item_update: schemas.CartItemUpdate,
    db: Session = Depends(get_db),
    current_user: CustomUser = Depends(get_current_user)
):
    # Find the cart item that belongs to the user
    cart_item = db.query(models.CartItem).join(models.ShoppingSession).filter(
        models.CartItem.id == item_id,
        models.ShoppingSession.user_id == current_user.id
    ).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    # Update the quantity based on the action or specific value
    if item_update.action == "increase":
        cart_item.quantity += 1
    elif item_update.action == "decrease":
        cart_item.quantity = max(1, cart_item.quantity - 1)
    elif item_update.quantity:
        cart_item.quantity = max(1, item_update.quantity)  # Avoid quantity < 1

    db.commit()
    return {"detail": "Cart item updated"}


# Endpoint to remove a cart item
@router.post("/remove/{item_id}")
def remove_cart_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: CustomUser = Depends(get_current_user)
):
    # Get the cart item if it belongs to the user
    cart_item = db.query(models.CartItem).join(models.ShoppingSession).filter(
        models.CartItem.id == item_id,
        models.ShoppingSession.user_id == current_user.id
    ).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    # Delete the item from the cart
    db.delete(cart_item)
    db.commit()
    return {"detail": "Cart item removed"}
