from fastapi import FastAPI
import os
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import users
from routers import store
from routers import cart    
from routers import orders 
# from routers import payments  # ← if you have payments

app = FastAPI()

# Serve uploaded media from the same folder Django uses
MEDIA_DIR = os.path.join(os.getcwd(), "media")
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Users endpoints  
app.include_router(users.router, prefix="/users", tags=["Users"])

# Store endpoints   
app.include_router(store.router, prefix="/store", tags=["Store"])

# # Cart endpoints    
app.include_router(cart.router, prefix="/cart", tags=["Cart"])

# # Orders endpoints  
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# # Payments endpoints
# app.include_router(payments.router, prefix="/payments", tags=["Payments"])
