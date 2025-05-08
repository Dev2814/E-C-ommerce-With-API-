from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import CustomUser
from app.users import models as user_models, schemas
from app.utils.security import get_password_hash, verify_password
from passlib.context import CryptContext

# Password hashing context using bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- User CRUD Operations ---

# Retrieve a user by their email address
def get_user_by_email(db: Session, email: str):
    return db.query(user_models.CustomUser).filter(user_models.CustomUser.email == email).first()

# Retrieve a user by their ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(user_models.CustomUser).filter(user_models.CustomUser.id == user_id).first()

# Create a new user with a hashed password
def create_user(db: Session, user_data: schemas.UserCreate, hashed_password: str):
    try:
        hashed_password = get_password_hash(user_data.password)  # Hash the user's password
        new_user = user_models.CustomUser(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password,
            role=user_data.role,
            is_active=False  # User starts as inactive (e.g., pending verification)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()  # Rollback in case of error to avoid partial DB writes
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")

# Mark a user as verified and clear their OTP
def verify_user_otp(db: Session, user: user_models.CustomUser):
    user.is_active = True
    user.otp = None
    db.commit()
    db.refresh(user)
    return user

# Update a user's OTP (e.g., for login or password reset)
def update_user_otp(db: Session, user: user_models.CustomUser, otp: str):
    user.otp = otp
    db.commit()
    db.refresh(user)
    return user

# Update a user's password with a new hashed password
def update_user_password(db: Session, user_id: int, new_password: str):
    user = db.query(CustomUser).filter(CustomUser.id == user_id).first()
    if user:
        user.password = new_password
        db.commit()
        db.refresh(user)
        return user
    return None

# Authenticate a user by checking email and password
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        print(f"Authentication failed: No user found with email {email}")
        return None

    # Check if the stored password is hashed using bcrypt
    if user.password.startswith('$2b$') or user.password.startswith('$2a$'):
        if not verify_password(password, user.password):
            print(f"Authentication failed: Incorrect password for user {email}")
            return None
    else:
        # If password is not hashed properly, rehash it
        print(f"Password for {email} needs to be rehashed")
        new_hashed_password = get_password_hash(password)
        update_user_password(db, user.id, new_hashed_password)
        if not verify_password(password, new_hashed_password):
            print(f"Authentication failed: Incorrect password for user {email}")
            return None

    return user

# Reset a user's password and clear their OTP
def reset_user_password(db: Session, user: user_models.CustomUser, new_password: str):
    user.password = get_password_hash(new_password)  # Hash the new password
    user.otp = None  # Clear OTP after successful reset
    db.commit()
    db.refresh(user)
    return user

# --- Address CRUD Operations ---

# Create a primary address for a user
def create_address(db: Session, address_data: schemas.AddressCreate):
    address = user_models.UserAddress(**address_data.dict())
    db.add(address)
    db.commit()
    db.refresh(address)
    return address

# Create a secondary address for a user
def create_secondary_address(db: Session, address_data: schemas.SecondaryAddressCreate):
    secondary_address = user_models.UserSecondaryAddress(**address_data.dict())
    db.add(secondary_address)
    db.commit()
    db.refresh(secondary_address)
    return secondary_address

# --- Payment CRUD Operation ---

# Create a payment record for a user
def create_user_payment(db: Session, payment_data: schemas.PaymentCreate):
    payment = user_models.UserPayment(**payment_data.dict())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
