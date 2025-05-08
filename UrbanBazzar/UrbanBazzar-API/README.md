# UrbanBazzar-API

UrbanBazzar-API is a robust e-commerce backend API built with FastAPI, providing a comprehensive set of endpoints for managing an online marketplace. This API supports user management, store operations, shopping cart functionality, and order processing.

## 🚀 Features

### 👤 User Management
- **Authentication & Authorization**
  - Secure user registration and login
  - JWT-based authentication
  - OTP-based login system
  - Password reset functionality
  - Session management

- **User Profile**
  - Profile creation and management
  - Multiple address support (Primary and Secondary)
  - Payment method management
  - Order history tracking
  - User preferences

### 🏪 Store Management
- **Product Catalog**
  - Product categories and subcategories
  - Product listings with detailed information
  - Product search and filtering
  - Product images and try-on images
  - Stock management
  - Price management
  - Brand management

- **Inventory Management**
  - Real-time stock tracking
  - Low stock alerts
  - Stock updates on order
  - Product availability status

### 🛒 Shopping Cart
- **Cart Management**
  - Add/remove products
  - Update quantities
  - Save for later
  - Cart persistence
  - Price calculations
  - Stock validation

- **Cart Features**
  - Real-time price updates
  - Stock availability check
  - Multiple items management
  - Cart total calculation
  - Cart item validation

### 📦 Order Processing
- **Order Management**
  - Order creation and tracking
  - Multiple payment methods
  - Order status updates
  - Order history
  - Order cancellation
  - Order confirmation

- **Payment Processing**
  - Multiple payment options
  - Payment status tracking
  - Payment verification
  - Payment history
  - Refund processing

### 🔍 Search & Discovery
- **Product Search**
  - Text-based search
  - Category-based filtering
  - Price range filtering
  - Brand filtering
  - Sort by various parameters

### 📱 Additional Features
- **Media Management**
  - Product image upload
  - Try-on image support
  - Image optimization
  - Multiple image support

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt
- **Media Handling**: FastAPI StaticFiles
- **API Documentation**: Swagger UI (automatically generated)

## 📁 Project Structure

```
UrbanBazzar-API/
├── app/                    # Application core
│   ├── users/             # User-related business logic
│   │   ├── models.py      # User database models
│   │   ├── schemas.py     # User Pydantic schemas
│   │   ├── router.py      # User API routes
│   │   ├── crud.py        # User CRUD operations
│   │   └── auth.py        # Authentication logic
│   │
│   ├── store/             # Store-related business logic
│   │   ├── models.py      # Store database models
│   │   ├── schemas.py     # Store Pydantic schemas
│   │   ├── routers.py     # Store API routes
│   │   └── crud.py        # Store CRUD operations
│   │
│   ├── cart/              # Cart-related business logic
│   │   ├── models.py      # Cart database models
│   │   ├── schemas.py     # Cart Pydantic schemas
│   │   └── router.py      # Cart API routes
│   │
│   ├── orders/            # Order-related business logic
│   │   ├── models.py      # Order database models
│   │   ├── schemas.py     # Order Pydantic schemas
│   │   ├── router.py      # Order API routes
│   │   └── crud.py        # Order CRUD operations
│   │
│   ├── payments/          # Payment processing logic
│   │   ├── models.py      # Payment database models
│   │   └── schemas.py     # Payment Pydantic schemas
│   │
│   ├── utils/             # Utility functions
│   │   └── security.py    # Security utilities
│   │
│   └── dependencies.py    # Shared dependencies
│
├── routers/               # API route handlers
│   ├── users.py          # User-related endpoints
│   ├── store.py          # Store-related endpoints
│   ├── cart.py           # Cart-related endpoints
│   └── orders.py         # Order-related endpoints
│
├── models/               # Database models
│   └── database.py      # Database configuration
│
├── services/            # Business logic services
├── media/              # Media storage for uploads
├── UA/                 # Virtual Environment directory
├── config.py           # Configuration settings
├── main.py            # Application entry point
└── req.txt            # Project dependencies
```

## 📚 API Documentation

### Users API Endpoints (`/users`)

1. **User Registration**
   - `POST /users/signup`
   - Creates a new user account
   - Required fields: email, password, username

2. **User Authentication**
   - `POST /users/token`
   - Generates JWT access token
   - Required fields: username (email), password

3. **Login with OTP**
   - `POST /users/login`
   - Generates and sends OTP
   - Required fields: email, password

4. **OTP Verification**
   - `POST /users/verify-otp`
   - Verifies OTP and generates JWT token
   - Required fields: email, OTP

5. **Resend OTP**
   - `POST /users/resend-otp`
   - Resends OTP to user's email
   - Required fields: email

6. **Password Management**
   - `POST /users/forgot-password`
   - Initiates password reset process
   - Required fields: email
   - `POST /users/reset-password-by-link`
   - Resets password using token
   - Required fields: token, new_password, confirm_password

7. **Address Management**
   - `POST /users/add-address`
   - Adds primary address
   - `POST /users/add-secondary-address`
   - Adds secondary address
   - `POST /users/add-payment`
   - Adds payment method

### Store API Endpoints (`/store`)

1. **Product Categories**
   - `POST /store/categories/`
   - Creates new product category
   - `GET /store/categories/`
   - Lists all categories
   - `GET /store/categories/{category_id}`
   - Gets specific category details

2. **Products**
   - `POST /store/products/`
   - Creates new product
   - `GET /store/products/`
   - Lists all products with pagination
   - `GET /store/products/{product_id}`
   - Gets specific product details

3. **Product Images**
   - `POST /store/products/{product_id}/images/`
   - Adds image to product
   - `POST /store/products/{product_id}/tryon-images/`
   - Adds try-on image to product

### Cart API Endpoints (`/cart`)

1. **Cart Management**
   - `POST /cart/add/{product_id}`
   - Adds product to cart
   - `GET /cart/view`
   - Views cart contents
   - `POST /cart/update/{item_id}`
   - Updates cart item quantity
   - `POST /cart/remove/{item_id}`
   - Removes item from cart

### Orders API Endpoints (`/orders`)

1. **Order Management**
   - `POST /orders/`
   - Creates new order
   - Required fields: address, city, pincode, country, mobile, payment_method
   - `GET /orders/`
   - Lists all orders for current user

## 🚀 Getting Started

### Prerequisites

- Python 3.13.2
- xampp MySQL Server
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/UrbanBazzar-API.git
   cd UrbanBazzar-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r req.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```
   DATABASE_URL=mysql://user:password@localhost/dbname
   SECRET_KEY=your_secret_key
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS middleware configuration
- Secure media file handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Dev Amdavadi - Initial work

## 🙏 Acknowledgments

- FastAPI documentation
- SQLAlchemy documentation
- All contributors who have helped shape this project 