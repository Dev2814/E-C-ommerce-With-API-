from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import os
from dotenv import load_dotenv

# Secret key used to sign JWT tokens (should be kept secure in production)
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# Algorithm used to sign the JWT
ALGORITHM = "HS256"

# Access token expiration time: 30 days 
ACCESS_TOKEN_EXPIRE_DAYS = 30

# Refresh token expiration time: 30 days
REFRESH_TOKEN_EXPIRE_DAYS = 30

# FastAPI dependency to extract the token from the Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

# In-memory store for blacklisted refresh tokens (only for demo/testing; use Redis/DB in production)
blacklisted_refresh_tokens = set()

# Function to create a JWT access token with expiration time
def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)  # Set expiry
    data.update({"exp": expire})  # Add expiry to payload
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)  # Encode and return JWT

# Function to create a JWT refresh token with expiration time
def create_refresh_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)  # Set expiry
    data.update({"exp": expire})  # Add expiry to payload
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)  # Encode and return JWT

# Function to decode and verify a JWT access token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decode token
        return payload  # Return payload if successful
    except JWTError:
        return None  # Return None if decoding fails (e.g., invalid or expired token)

# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)  # Decode token payload
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")  # Raise error if invalid
    return payload  # Return the decoded payload (typically contains user info like user_id)

# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from fastapi.security import OAuth2PasswordBearer

# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 1

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")

# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def decode_access_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except JWTError:
#         return None