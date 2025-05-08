# UrbanBazzar-API

UrbanBazzar-API is a robust e-commerce backend API built with FastAPI, providing a comprehensive set of endpoints for managing an online marketplace. This API supports user management, store operations, shopping cart functionality, and order processing.

## 🏗️ Project Architecture

### Backend (FastAPI)
The FastAPI backend serves as the core API layer, handling all data operations and business logic:

1. **API Layer (FastAPI)**
   - Handles all database operations
   - Manages business logic
   - Provides RESTful endpoints
   - Handles authentication and authorization
   - Manages file uploads and media

2. **Database Layer**
   - MySQL database for data storage
   - SQLAlchemy ORM for database operations
   - Handles all CRUD operations

### Frontend (Django)
The Django frontend serves as the web interface, consuming the FastAPI endpoints:

1. **Web Interface (Django)**
   - Renders web pages
   - Handles user interactions
   - Manages sessions
   - Provides user interface

2. **Integration Layer**
   - Makes HTTP requests to FastAPI
   - Handles API responses
   - Manages authentication tokens
   - Processes form submissions

## 🔄 How It Works

### 1. User Authentication Flow
```
User -> Django Frontend -> FastAPI Backend -> Database
     <- Django Frontend <- FastAPI Backend <-
```

1. User enters credentials in Django form
2. Django sends request to FastAPI
3. FastAPI validates and processes authentication
4. Response flows back to Django
5. Django manages user session

### 2. Product Management Flow
```
User -> Django Frontend -> FastAPI Backend -> Database
     <- Django Frontend <- FastAPI Backend <-
```

1. User browses products in Django interface
2. Django fetches product data from FastAPI
3. FastAPI retrieves data from database
4. Data flows back to Django for display

### 3. Shopping Cart Flow
```
User -> Django Frontend -> FastAPI Backend -> Database
     <- Django Frontend <- FastAPI Backend <-
```

1. User adds items to cart in Django
2. Django sends cart updates to FastAPI
3. FastAPI updates cart in database
4. Updated cart data returns to Django

### 4. Order Processing Flow
```
User -> Django Frontend -> FastAPI Backend -> Database
     <- Django Frontend <- FastAPI Backend <-
```

1. User places order in Django
2. Django sends order to FastAPI
3. FastAPI processes order and updates database
4. Order confirmation returns to Django

## 🔐 Security Implementation

### 1. Authentication
- JWT tokens for API authentication
- Session management in Django
- Secure password hashing
- OTP-based login system

### 2. Data Protection
- HTTPS for all communications
- Input validation on both ends
- SQL injection prevention
- XSS protection

## 📦 Data Flow

### 1. User Data
```
Django Form -> FastAPI Validation -> Database
           <- FastAPI Response <- Database
```

### 2. Product Data
```
Django Request -> FastAPI Query -> Database
              <- FastAPI Data <- Database
```

### 3. Order Data
```
Django Form -> FastAPI Processing -> Database
           <- FastAPI Confirmation <- Database
```

## 🚀 Development Workflow

1. **Backend Development (FastAPI)**
   - Develop and test API endpoints
   - Implement business logic
   - Handle database operations
   - Ensure API security

2. **Frontend Development (Django)**
   - Create user interfaces
   - Implement API integration
   - Handle user sessions
   - Manage form submissions

3. **Integration Testing**
   - Test API endpoints
   - Verify data flow
   - Check error handling
   - Validate security measures

## 🔧 Configuration

### FastAPI Configuration
```python
# config.py
DATABASE_URL = "mysql://user:password@localhost/dbname"
SECRET_KEY = "your-secret-key"
```

### Django Configuration
```python
# settings.py
FASTAPI_URL = "http://localhost:8000"
API_TOKEN = "your-api-token"
```

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

- **Security Features**
  - Secure password hashing
  - JWT token authentication
  - CORS protection
  - Input validation
  - SQL injection prevention

- **API Features**
  - RESTful API design
  - Comprehensive error handling
  - Rate limiting
  - Request validation
  - Response caching

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt
- **Media Handling**: FastAPI StaticFiles
- **API Documentation**: Swagger UI (automatically generated)

## 📁 Project Structure

# UrbanBazzar API Structure

This document shows the exact folder structure of the UrbanBazzar-API project.

```
UrbanBazzar-API/
│
├── README.md                # API documentation
├── req.txt                  # Python dependencies
├── main.py                  # FastAPI application entry point
├── config.py                # Configuration settings
│
├── __pycache__/            # Python cache directory
│
├── app/                    # Main application code
│   ├── __pycache__/
│   ├── dependencies.py     # Shared dependencies
│   ├── users/             # User-related business logic
│   │   ├── __init__.py
│   │   ├── models.py      # User data models
│   │   ├── schemas.py     # User Pydantic schemas
│   │   ├── crud.py        # User CRUD operations
│   │   └── auth.py        # Authentication logic
│   │
│   ├── store/             # Store-related business logic
│   │   ├── __init__.py
│   │   ├── models.py      # Store and product models
│   │   ├── schemas.py     # Store Pydantic schemas
│   │   ├── crud.py        # Store CRUD operations
│   │   └── inventory.py   # Inventory management
│   │
│   ├── cart/              # Cart-related business logic
│   │   ├── __init__.py
│   │   ├── models.py      # Cart data models
│   │   ├── schemas.py     # Cart Pydantic schemas
│   │   └── crud.py        # Cart CRUD operations
│   │
│   ├── orders/            # Order-related business logic
│   │   ├── __init__.py
│   │   ├── models.py      # Order data models
│   │   ├── schemas.py     # Order Pydantic schemas
│   │   └── crud.py        # Order CRUD operations
│   │
│   ├── payments/          # Payment processing logic
│   │   ├── __init__.py
│   │   ├── models.py      # Payment data models
│   │   ├── schemas.py     # Payment Pydantic schemas
│   │   └── processor.py   # Payment processing logic
│   │
│   └── utils/             # Utility functions
│       ├── __init__.py
│       └── security.py    # Security utilities
│
├── routers/               # API route definitions
│   ├── __pycache__/
│   ├── users.py          # User-related endpoints
│   ├── store.py          # Store-related endpoints
│   ├── cart.py           # Cart-related endpoints
│   └── orders.py         # Order-related endpoints
│
├── models/                # Data models
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   └── order.py
│
├── services/             # Business logic
│   └──email_service.py
│
├── UA/                 # Python Virtual Environment
│   ├── Lib/             # Python packages
│   ├── Scripts/         # Executable scripts
│   └── pyvenv.cfg       # Virtual environment config
│
└── media/               # API media files
```

## App Directory Structure Details

### 1. Users Module (`app/users/`)
- **models.py**: Defines user-related database models
  - User model with authentication fields
  - Address model for user addresses
  - Payment method model
- **schemas.py**: Pydantic models for request/response validation
  - UserCreate schema for registration
  - UserResponse schema for user data
  - Address schemas for address management
- **crud.py**: Database operations for users
  - User creation and retrieval
  - Address management
  - Payment method management
- **auth.py**: Authentication logic
  - Password hashing
  - JWT token generation
  - OTP handling

### 2. Store Module (`app/store/`)
- **models.py**: Store and product database models
  - Product model with details
  - Category model
  - Inventory model
- **schemas.py**: Store-related Pydantic models
  - Product schemas
  - Category schemas
  - Inventory schemas
- **crud.py**: Store database operations
  - Product management
  - Category management
  - Inventory updates
- **inventory.py**: Inventory management logic
  - Stock tracking
  - Low stock alerts
  - Stock updates

### 3. Cart Module (`app/cart/`)
- **models.py**: Cart database models
  - Cart model
  - CartItem model
- **schemas.py**: Cart Pydantic models
  - Cart schemas
  - CartItem schemas
- **crud.py**: Cart database operations
  - Add/remove items
  - Update quantities
  - Cart calculations

### 4. Orders Module (`app/orders/`)
- **models.py**: Order database models
  - Order model
  - OrderItem model
  - OrderStatus model
- **schemas.py**: Order Pydantic models
  - Order schemas
  - OrderItem schemas
  - OrderStatus schemas
- **crud.py**: Order database operations
  - Order creation
  - Status updates
  - Order retrieval

### 5. Payments Module (`app/payments/`)
- **models.py**: Payment database models
  - Payment model
  - Transaction model
- **schemas.py**: Payment Pydantic models
  - Payment schemas
  - Transaction schemas
- **processor.py**: Payment processing logic
  - Payment validation
  - Transaction handling
  - Refund processing

### 6. Utils Module (`app/utils/`)
- **security.py**: Security utilities
  - Password hashing
  - Token generation
  - Security checks
- **email.py**: Email utilities
  - Email templates
  - Email sending
  - OTP emails
- **validators.py**: Input validation
  - Data validation
  - Format checking
  - Custom validators

### 7. Dependencies (`app/dependencies.py`)
- Shared dependencies for the application
- Database session management
- Authentication dependencies
- Common utilities

## File Descriptions

### Root Level Files
- `README.md`: Project documentation and setup instructions
- `req.txt`: List of Python package dependencies
- `main.py`: Main FastAPI application entry point
- `config.py`: Configuration settings for the API

### Directories

#### app/
Contains the core application code and business logic
- `dependencies.py`: Shared dependencies and utilities
- `users/`: User management functionality
- `store/`: Store and product management
- `cart/`: Shopping cart functionality
- `orders/`: Order processing
- `payments/`: Payment processing
- `utils/`: Utility functions and helpers

#### routers/
Contains all API route definitions and endpoints

1. **users.py** - User Management Endpoints
   - `POST /users/signup`: Register new user
     - Required fields: email, password, username
     - Returns: User details with JWT token
   - `POST /users/token`: User login
     - Required fields: username (email), password
     - Returns: JWT access token
   - `POST /users/login`: OTP-based login
     - Required fields: email, password
     - Returns: OTP for verification
   - `POST /users/verify-otp`: Verify OTP
     - Required fields: email, OTP
     - Returns: JWT token on successful verification
   - `POST /users/resend-otp`: Resend OTP
     - Required fields: email
     - Returns: New OTP
   - `POST /users/forgot-password`: Password reset request
     - Required fields: email
     - Returns: Password reset link
   - `POST /users/reset-password-by-link`: Reset password
     - Required fields: token, new_password, confirm_password
     - Returns: Success message
   - `POST /users/add-address`: Add user address
     - Required fields: user_id, address details
     - Returns: Address details
   - `POST /users/add-secondary-address`: Add secondary address
     - Required fields: user_id, address details
     - Returns: Secondary address details
   - `POST /users/add-payment`: Add payment method
     - Required fields: user_id, payment details
     - Returns: Payment method details

2. **store.py** - Store and Product Management Endpoints
   - `POST /store/categories/`: Create product category
     - Required fields: category details
     - Returns: Created category details
   - `GET /store/categories/`: List all categories
     - Optional: skip, limit for pagination
     - Returns: List of categories
   - `GET /store/categories/{category_id}`: Get category details
     - Required: category_id
     - Returns: Category details
   - `POST /store/products/`: Create new product
     - Required fields: product details
     - Returns: Created product details
   - `GET /store/products/`: List all products
     - Optional: skip, limit for pagination
     - Returns: List of products with images
   - `GET /store/products/{product_id}`: Get product details
     - Required: product_id
     - Returns: Product details with images
   - `POST /store/products/{product_id}/images/`: Add product image
     - Required: product_id, image file
     - Returns: Image details
   - `POST /store/products/{product_id}/tryon-images/`: Add try-on image
     - Required: product_id, try-on image file
     - Returns: Try-on image details

3. **cart.py** - Shopping Cart Management Endpoints
   - `POST /cart/add/{product_id}`: Add product to cart
     - Required: product_id
     - Returns: Cart item details
   - `GET /cart/view`: View cart contents
     - Returns: Cart details with items and total
   - `POST /cart/update/{item_id}`: Update cart item
     - Required: item_id, quantity
     - Returns: Updated cart item details
   - `POST /cart/remove/{item_id}`: Remove item from cart
     - Required: item_id
     - Returns: Success message

4. **orders.py** - Order Processing Endpoints
   - `POST /orders/`: Create new order
     - Required fields: 
       - address
       - city
       - pincode
       - country
       - mobile
       - payment_method
     - Returns: Order details with items
   - `GET /orders/`: List user orders
     - Returns: List of orders with details
   - Order Status Updates:
     - Pending
     - Processing
     - Shipped
     - Delivered
     - Cancelled

Each router file includes:
- Input validation
- Error handling
- Authentication checks
- Database operations
- Response formatting

#### models/
Contains data models
- `__init__.py`: Package initialization
- `user.py`: User data models
- `product.py`: Product data models
- `order.py`: Order data models

#### services/
Contains business logic
- `__init__.py`: Package initialization
- `auth_service.py`: Authentication service
- `order_service.py`: Order processing service

#### UA/
Python Virtual Environment directory
- `Lib/`: Contains installed Python packages
- `Scripts/`: Contains executable scripts (activate, python, pip, etc.)
- `pyvenv.cfg`: Virtual environment configuration file
- Used to isolate project dependencies and Python versions

#### media/
Directory for storing media files
- Used for storing uploaded files and images

#### __pycache__/
Python cache directory
- Contains compiled Python bytecode files
- Automatically generated by Python

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

### Step-by-Step Installation Guide

1. **Install Required Software**
   - Install Python 3.13.2 from [python.org](https://www.python.org/downloads/)
   - Install XAMPP from [apachefriends.org](https://www.apachefriends.org/download.html)
   - Verify installations:
     ```bash
     python --version
     pip --version
     ```

2. **Start MySQL Server**
   - Open XAMPP Control Panel
   - Start MySQL service
   - Create a new database named `urbanbazzar`:
     ```sql
     CREATE DATABASE urbanbazzar;
     ```

3. **Clone and Setup Project**
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/UrbanBazzar-API.git
   
   # Navigate to project directory
   cd UrbanBazzar-API
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   # Install all required packages
   pip install -r req.txt
   ```

5. **Configure Environment**
   - Create a `.env` file in the root directory
   - Add the following configuration:
     ```
     DATABASE_URL=mysql://root:@localhost/urbanbazzar
     SECRET_KEY=your_secret_key_here
     ```

6. **Database Migration**
   ```bash
   # Initialize database tables
   python -m alembic upgrade head
   ```

7. **Run the Application**
   ```bash
   # Start the FastAPI server
   uvicorn main:app --reload
   ```

8. **Access the Application**
   - API Documentation: http://localhost:8000/docs
   - Alternative API Documentation: http://localhost:8000/redoc
   - API Base URL: http://localhost:8000

### Testing the Installation

1. **Check API Health**
   - Visit http://localhost:8000/health
   - Should return: `{"status": "healthy"}`

2. **Test User Registration**
   - Open http://localhost:8000/docs
   - Navigate to `/users/signup` endpoint
   - Try creating a new user with:
     ```json
     {
       "email": "test@example.com",
       "password": "testpassword123",
       "username": "testuser"
     }
     ```

3. **Test Authentication**
   - Use the `/users/token` endpoint
   - Login with created credentials
   - Verify JWT token is received

### Common Issues and Solutions

1. **Database Connection Error**
   - Ensure MySQL is running in XAMPP
   - Verify database credentials in `.env`
   - Check if database `urbanbazzar` exists

2. **Port Already in Use**
   - Change port in uvicorn command:
     ```bash
     uvicorn main:app --reload --port 8001
     ```

3. **Module Not Found Errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed:
     ```bash
     pip list
     ```

4. **Permission Issues**
   - Run terminal as administrator
   - Check file permissions in project directory

### Development Workflow

1. **Making Changes**
   - Create a new branch for features
   - Make changes in the code
   - Test locally using uvicorn
   - Commit and push changes

2. **Testing Endpoints**
   - Use Swagger UI at `/docs`
   - Test all endpoints manually
   - Verify database updates

3. **Debugging**
   - Check logs in terminal
   - Use FastAPI's debug mode
   - Monitor database changes

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
