# UrbanBazzar - Modern E-Commerce Platform

UrbanBazzar is a full-featured e-commerce platform built with Django frontend and FastAPI backend, offering a seamless shopping experience with modern features and robust functionality.

## 🏗️ Architecture Overview

The project follows a microservices architecture with two main components:

### 1. Django Frontend (Port 1974)
- Handles user interface and templates
- Manages static files and media
- Provides admin interface
- Serves as the main application server
- Renders web pages
- Handles user interactions
- Manages sessions
- Provides user interface

### 2. FastAPI Backend (Port 2814)
- Provides RESTful API endpoints
- Handles business logic
- Manages data processing
- Implements authentication and authorization
- Handles all database operations
- Manages file uploads and media
- Provides comprehensive API documentation

## 🔄 How It Works

### Data Flow Architecture
```
User -> Django Frontend -> FastAPI Backend -> Database
     <- Django Frontend <- FastAPI Backend <-
```

### Key Workflows:
1. **User Authentication Flow**
   - User enters credentials in Django form
   - Django sends request to FastAPI
   - FastAPI validates and processes authentication
   - Response flows back to Django
   - Django manages user session

2. **Product Management Flow**
   - User browses products in Django interface
   - Django fetches product data from FastAPI
   - FastAPI retrieves data from database
   - Data flows back to Django for display

3. **Shopping Cart Flow**
   - User adds items to cart in Django
   - Django sends cart updates to FastAPI
   - FastAPI updates cart in database
   - Updated cart data returns to Django

4. **Order Processing Flow**
   - User places order in Django
   - Django sends order to FastAPI
   - FastAPI processes order and updates database
   - Order confirmation returns to Django

## 🚀 Features

### 👤 User Management
- **Authentication System**
  - JWT token-based authentication
  - OTP verification via FastAPI
  - Secure password management
  - Session handling with tokens
  - Password reset functionality
  - Email notifications

- **User Profile Management**
  - RESTful API for profile operations
  - Address management (Primary and Secondary)
  - Role-based access control
  - Profile updates through API
  - Payment method management
  - Order history tracking

### 🏪 Store Management
- **Product Management**
  - RESTful product CRUD operations
  - Image handling via API
  - Search and filtering
  - Inventory management
  - Product categories and subcategories
  - Brand management

- **Vendor Dashboard**
  - API-based analytics
  - Real-time statistics
  - Order management
  - Sales tracking
  - Low stock alerts
  - Stock updates on order

### 🛒 Shopping Cart
- **Cart Management**
  - API-based cart operations
  - Real-time updates
  - Session management
  - Stock validation
  - Save for later
  - Cart persistence
  - Price calculations

### 📦 Order Processing
- **Order Management**
  - API-based order creation
  - Status tracking
  - History management
  - Payment integration
  - Multiple payment methods
  - Order cancellation
  - Order confirmation

### 🔍 Search & Discovery
- **Product Search**
  - Text-based search
  - Category-based filtering
  - Price range filtering
  - Brand filtering
  - Sort by various parameters

### 👕 Virtual Try-On Feature
- **AI-Powered Try-On**
  - Real-time virtual clothing try-on
  - Body measurement detection
  - Size recommendation
  - Multiple angle view
  - Save and share try-on results
  - Color and style variations

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
- CORS protection
- Rate limiting

## 🛠️ Technology Stack

- **Python Version**: 3.13.2
- **Frontend**: Django 5.0+
- **Backend**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Image Processing**: OpenCV, MediaPipe
- **AI/ML**: TensorFlow

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

## 📁 Complete Project Structure

```
UrbanBazzar/                      # Root Project Directory
├── UrbanBazzar/                  # Django Frontend
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env                      # Environment variables
│   ├── .gitignore
│   ├── static/                   # Static files
│   │   ├── css/
│   │   │   ├── base.css
│   │   │   ├── home.css
│   │   │   ├── products.css
│   │   │   ├── cart.css
│   │   │   └── orders.css
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   ├── cart.js
│   │   │   ├── try-on.js
│   │   │   └── payment.js
│   │   └── images/
│   │       ├── logo/
│   │       ├── products/
│   │       └── try-on/
│   ├── media/                    # User uploaded files
│   │   ├── products/
│   │   │   ├── images/
│   │   │   └── try-on/
│   │   └── user_profiles/
│   ├── templates/               # HTML templates
│   │   ├── base.html
│   │   ├── home/
│   │   │   ├── index.html
│   │   │   └── about.html
│   │   ├── products/
│   │   │   ├── list.html
│   │   │   ├── detail.html
│   │   │   └── try-on.html
│   │   ├── cart/
│   │   │   ├── view.html
│   │   │   └── checkout.html
│   │   └── orders/
│   │       ├── list.html
│   │       └── detail.html
│   └── apps/                    # Django applications
│       ├── users/              # User management
│       │   ├── __init__.py
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── forms.py
│       │   ├── models.py
│       │   ├── urls.py
│       │   ├── views.py
│       │   └── tests.py
│       ├── store/             # Store management
│       │   ├── __init__.py
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── forms.py
│       │   ├── models.py
│       │   ├── urls.py
│       │   ├── views.py
│       │   └── tests.py
│       ├── cart/              # Shopping cart
│       │   ├── __init__.py
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── forms.py
│       │   ├── models.py
│       │   ├── urls.py
│       │   ├── views.py
│       │   └── tests.py
│       └── orders/            # Order processing
│           ├── __init__.py
│           ├── admin.py
│           ├── apps.py
│           ├── forms.py
│           ├── models.py
│           ├── urls.py
│           ├── views.py
│           └── tests.py
│
└── UrbanBazzar-API/            # FastAPI Backend
    ├── main.py                # FastAPI application entry point
    ├── requirements.txt       # Python dependencies
    ├── .env                  # Environment variables
    ├── .gitignore
    ├── config.py             # Configuration settings
    ├── database.py           # Database connection setup
    ├── models/               # SQLAlchemy database models
    │   ├── __init__.py
    │   ├── base.py          # Base model class
    │   ├── user.py          # User model
    │   ├── product.py       # Product model
    │   ├── cart.py          # Cart model
    │   └── order.py         # Order model
    ├── schemas/              # Pydantic schemas
    │   ├── __init__.py
    │   ├── user.py          # User schemas
    │   ├── product.py       # Product schemas
    │   ├── cart.py          # Cart schemas
    │   └── order.py         # Order schemas
    ├── routers/              # API endpoints
    │   ├── __init__.py
    │   ├── auth.py          # Authentication endpoints
    │   ├── users.py         # User management endpoints
    │   ├── products.py      # Product management endpoints
    │   ├── cart.py          # Cart management endpoints
    │   └── orders.py        # Order management endpoints
    ├── services/             # Business logic
    │   ├── __init__.py
    │   ├── auth.py          # Authentication service
    │   ├── user.py          # User service
    │   ├── product.py       # Product service
    │   ├── cart.py          # Cart service
    │   └── order.py         # Order service
    ├── utils/                # Utility functions
    │   ├── __init__.py
    │   ├── security.py      # Security utilities
    │   ├── email.py         # Email utilities
    │   ├── validators.py    # Input validation
    │   └── helpers.py       # Helper functions
    ├── middleware/           # Custom middleware
    │   ├── __init__.py
    │   ├── auth.py          # Authentication middleware
    │   └── logging.py       # Logging middleware
    ├── tests/               # API tests
    │   ├── __init__.py
    │   ├── conftest.py      # Test configuration
    │   ├── test_auth.py     # Authentication tests
    │   ├── test_users.py    # User management tests
    │   ├── test_products.py # Product management tests
    │   ├── test_cart.py     # Cart management tests
    │   └── test_orders.py   # Order management tests
    └── docs/                # API documentation
        ├── openapi.json     # OpenAPI specification
        └── swagger.json     # Swagger documentation
```

### Key Components Description

#### Django Frontend (UrbanBazzar/)
- **static/**: Contains all static files organized by type (CSS, JS, images)
- **media/**: Stores user-uploaded files like product images and try-on results
- **templates/**: HTML templates organized by feature with base template
- **apps/**: Django applications for different features
  - **users/**: User authentication and profile management
  - **store/**: Product catalog and vendor management
  - **cart/**: Shopping cart functionality
  - **orders/**: Order processing and management

#### FastAPI Backend (UrbanBazzar-API/)
- **main.py**: Entry point for the FastAPI application
- **models/**: SQLAlchemy database models with base model class
- **schemas/**: Pydantic models for request/response validation
- **routers/**: API endpoint definitions organized by feature
- **services/**: Business logic implementation
- **utils/**: Helper functions and utilities
- **middleware/**: Custom middleware for authentication and logging
- **tests/**: API endpoint tests with test configuration
- **docs/**: API documentation including OpenAPI and Swagger specs 