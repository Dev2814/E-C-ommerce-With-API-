from fastapi import APIRouter, HTTPException, Depends, status, Request, Form
from sqlalchemy.orm import Session
from app.users.auth import create_access_token 
from models.database import get_db
from app.users import schemas, crud, models
from app.users.schemas import *
from app.users.crud import *
from datetime import datetime, timedelta
import secrets
from fastapi.security import OAuth2PasswordRequestForm
import random
import hashlib
import string
import time
from fastapi.responses import JSONResponse
from config import FAST_API_URL, DJANGO_URL

print(DJANGO_URL)

router = APIRouter()

# Utility to generate OTP
def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))


@router.post("/signup", response_model=schemas.UserResponse)
def signup_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        print("Signup request received with email:", user_data.email)

        # Check if the email is already registered
        existing_user = crud.get_user_by_email(db, email=user_data.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Create the user without generating OTP
        user = crud.create_user(db, user_data, None)
        print("User created:", user.email)

        # Skip sending OTP here
        return user

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/token", response_model=TokenResponse)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": str(user.id)})
    return TokenResponse(access_token=access_token, token_type="bearer", message="Login successful")


otp_storage = {}

def generate_simple_otp():
    return str(random.randint(100000, 999999))

def store_otp_with_timestamp(email, otp):
    otp_storage[email] = {
        "otp": otp,
        "timestamp": time.time()
    }

def is_otp_expired(email, expiration_time=300):
    if email not in otp_storage:
        return True
    timestamp = otp_storage[email]["timestamp"]
    return time.time() - timestamp > expiration_time

@router.post("/login")
def login_user(login_data: schemas.UserLogin, db: Session = Depends(get_db)):
    if not login_data.email:
        raise HTTPException(status_code=400, detail="Email is required")
    if not login_data.password:
        raise HTTPException(status_code=400, detail="Password is required")

    user = crud.authenticate_user(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Expire any previous OTP before generating a new one
    otp_code = generate_simple_otp()
    store_otp_with_timestamp(user.email, otp_code)

    return {
        "message": "OTP generated successfully",
        "email": user.email,
        "username": user.username,
        "otp": otp_code  # This OTP will be sent via Django views
    }

@router.post("/verify-otp")
def verify_otp(otp_data: schemas.OTPVerify, db: Session = Depends(get_db)):
    if is_otp_expired(otp_data.email):
        raise HTTPException(status_code=400, detail="OTP has expired")

    stored_otp = otp_storage.get(otp_data.email, {}).get("otp")
    if stored_otp != otp_data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user = crud.get_user_by_email(db, email=otp_data.email)
    if user:
        crud.verify_user_otp(db, user)

    # Generate JWT token after successful verification
    token = create_access_token(data={"user_id": user.id, "email": user.email})

    # Remove OTP after successful verification
    otp_storage.pop(otp_data.email, None)

    data = {
        "message": "OTP verified successfully",
        "access_token": token,
        "token_type": "bearer"
    }

    return data

@router.post("/resend-otp")
def resend_otp(email: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = generate_simple_otp()
    store_otp_with_timestamp(email, otp)

    return {
        "message": "OTP resent successfully.",
        "email": email,
        "otp": otp  # Will be sent from Django view
    }


def generate_hashed_user_id(user_id: int) -> str:
    """Generate a sha256 hash of the user ID."""
    return hashlib.sha256(str(user_id).encode()).hexdigest()

@router.post("/forgot-password")
def forgot_password(email: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate a secure random token
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    # Save to DB
    reset_token = models.PasswordResetToken(
        user_id=user.id,
        token=token,
        expires_at=expires_at
    )
    db.add(reset_token)
    db.commit()

    # Reset link
    reset_link = f"{DJANGO_URL}/users/forgetpassword/{token}/"
    return {"reset_link": reset_link}

@router.post("/reset-password-by-link")
def reset_password_by_link(
    data: schemas.PasswordResetByToken, db: Session = Depends(get_db)
):
    token_entry = (
        db.query(models.PasswordResetToken)
        .filter_by(token=data.token, used=False)
        .first()
    )

    if not token_entry or token_entry.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=400, detail="Invalid or expired reset link"
        )

    user = db.query(models.CustomUser).filter_by(id=token_entry.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Update password
    crud.reset_user_password(db, user, data.new_password)

    # Mark token as used
    token_entry.used = True
    db.commit()

    return JSONResponse(content={"message": "Password has been reset"}, status_code=200)


@router.post("/add-address", response_model=schemas.AddressResponse)
def add_address(address_data: schemas.AddressCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, address_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_address(db, address_data)


@router.post("/add-secondary-address", response_model=schemas.SecondaryAddressResponse)
def add_secondary_address(address_data: schemas.SecondaryAddressCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, address_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_secondary_address(db, address_data)


@router.post("/add-payment", response_model=schemas.UserPayment)
def add_payment(payment_data: schemas.PaymentCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, payment_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_payment(db, payment_data)

# @router.post("/forgot-password")
# def forgot_password(email: str = Form(...), db: Session = Depends(get_db)):
#     """Generate reset link with hashed user ID and send it back to Django."""
#     # Get user by email
#     user = crud.get_user_by_email(db, email=email)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Generate hashed user ID
#     hashed_user_id = generate_hashed_user_id(user.id)

#     # Create password reset link
#     reset_link = f"{DJANGO_URL}/users/forgetpassword/{hashed_user_id}/"

#     # Return the generated reset link
#     return {"reset_link": reset_link}

# @router.post("/reset-password-by-link")
# def reset_password_by_link(
#     data: schemas.PasswordResetByHash, db: Session = Depends(get_db)
# ):
#     """Handles password reset using hashed user ID."""
    
#     # Find the user by comparing hashed ID
#     user = None
#     for u in db.query(models.CustomUser).all():
#         hashed_id = hashlib.sha256(str(u.id).encode()).hexdigest()
#         if hashed_id == data.hashed_user_id:
#             user = u
#             break

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Invalid or expired reset link",
#         )

#     # Ensure the new password and confirm password match
#     if data.new_password != data.confirm_password:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Passwords do not match",
#         )

#     # Update the password in the database
#     crud.reset_user_password(db, user, data.new_password)

#     return JSONResponse(
#         content={"message": "Password has been reset successfully"},
#         status_code=status.HTTP_200_OK,
#     )