# UrbanBazzar - Modern E-Commerce Platform

UrbanBazzar is a full-featured e-commerce platform built with Django frontend, offering a seamless shopping experience with modern features and robust functionality.

## 🏗️ Architecture Overview

The project follows a microservices architecture with two main components:

1. **Django Frontend** (Port 1974)
   - Handles user interface and templates
   - Manages static files and media
   - Provides admin interface
   - Serves as the main application server

2. **FastAPI Backend** (Port 2814)
   - Provides RESTful API endpoints
   - Handles business logic
   - Manages data processing
   - Implements authentication and authorization

For detailed API documentation, please refer to the [UrbanBazzar-API README](UrbanBazzar-API/README.md).

## 🚀 Features

### User Management (`users/views.py`)
- **Authentication System**
  - JWT token-based authentication
  - OTP verification via FastAPI
  - Secure password management
  - Session handling with tokens

- **User Profile Management**
  - RESTful API for profile operations
  - Address management via API
  - Role-based access control
  - Profile updates through API

- **Email Notifications**
  - Email service integration
  - Template-based emails
  - Automated notifications

- **Password Reset System**
  - Secure one-time use reset tokens
  - Token expiration handling
  - Email-based reset link delivery
  - Automatic invalidation of old tokens
  - Confirmation emails for successful resets
  - Protection against token reuse
  - User-friendly error messages
  - Mobile-responsive reset pages

- **View Functions**
  - `signup_user(request)`: Handles user registration with email verification
    - Validates user input (username, email, password)
    - Creates user account via FastAPI
    - Sends welcome email
    - Redirects to login page on success

  - `login_user(request)`: Manages user login with JWT token generation
    - Authenticates user credentials
    - Generates JWT token
    - Initiates OTP verification
    - Stores token in session

  - `Verify_Login_otp(request)`: Validates OTP for secure login
    - Verifies OTP code
    - Completes login process
    - Sends login confirmation email
    - Redirects to dashboard

  - `Resend_user_Login_otp(request)`: Handles OTP resending functionality
    - Generates new OTP
    - Sends new OTP email
    - Updates session data

  - `password_reset_request(request)`: Initiates password reset process
    - Validates user email
    - Generates reset token
    - Sends reset link email

  - `Reset_password(request, token)`: Processes password reset with token validation
    - Validates reset token
    - Updates user password
    - Sends confirmation email
    - Redirects to login

  - `add_primary_address(request)`: Manages primary address addition
    - Validates address data
    - Creates primary address
    - Updates user profile

  - `add_secondary_address(request)`: Handles secondary address management
    - Validates address data
    - Creates secondary address
    - Links to user profile

  - `logout_user(request)`: Manages user logout and session cleanup
    - Clears session data
    - Invalidates JWT token
    - Redirects to home page

### Store Management (`store/views.py`)
- **Product Management**
  - RESTful product CRUD operations
  - Image handling via API
  - Search and filtering
  - Inventory management

- **Vendor Dashboard**
  - API-based analytics
  - Real-time statistics
  - Order management
  - Sales tracking

- **View Functions**
  - `product_detail(request, pk)`: Displays detailed product information
    - Fetches product data
    - Shows product images
    - Displays pricing and stock
    - Handles related products

  - `product_list(request)`: Lists products with search and pagination
    - Implements search functionality
    - Handles category filtering
    - Manages pagination
    - Sorts products by various criteria

  - `vender_dashboard(request)`: Shows vendor-specific analytics and data
    - Displays sales statistics
    - Shows order management
    - Lists vendor products
    - Shows pending payments

  - `add_product(request)`: Handles new product creation with image upload
    - Validates product data
    - Handles multiple image uploads
    - Creates product record
    - Updates inventory

  - `edit_product(request, pk)`: Manages product updates
    - Loads existing product data
    - Validates updates
    - Updates product information
    - Handles image modifications

  - `delete_product(request, pk)`: Handles product deletion
    - Verifies vendor ownership
    - Removes product images
    - Deletes product record
    - Updates inventory

  - `update_order_status(request, order_id)`: Manages order status updates
    - Validates status change
    - Updates order status
    - Handles stock adjustments
    - Sends notifications

### Virtual Try-On Feature
- **AI-Powered Try-On**
  - Real-time virtual clothing try-on
  - Body measurement detection
  - Size recommendation
  - Multiple angle view
  - Save and share try-on results

- **Try-On Features**
  - Upload user photos
  - Real-time body detection
  - Clothing overlay
  - Size and fit visualization
  - Color and style variations
  - Save favorite combinations

- **Technical Implementation**
  - OpenCV for image processing
  - MediaPipe for body detection
  - TensorFlow for AI model
  - Real-time rendering
  - Cloud storage for try-on results

### Shopping Cart (`cart/views.py`)
- **Cart Management**
  - API-based cart operations
  - Real-time updates
  - Session management
  - Stock validation

- **View Functions**
  - `add_to_cart(request, product_id)`: Adds products to cart with stock validation
    - Checks product availability
    - Validates quantity
    - Updates cart via FastAPI
    - Returns success/error message

  - `view_cart(request)`: Displays cart contents with totals
    - Fetches cart items
    - Calculates totals
    - Shows shipping options
    - Displays address information

  - `update_cart_item(request, item_id)`: Updates item quantities
    - Validates new quantity
    - Updates cart item
    - Recalculates totals
    - Checks stock availability

  - `remove_cart_item(request, item_id)`: Removes items from cart
    - Removes item from cart
    - Updates cart totals
    - Handles empty cart state
    - Returns updated cart view

### Order Processing (`orders/views.py`)
- **Order Management**
  - API-based order creation
  - Status tracking
  - History management
  - Payment integration

- **View Functions**
  - `confirm_order(request)`: Processes order confirmation and payment
    - Validates order data
    - Processes payment
    - Creates order record
    - Sends confirmation email
    - Updates inventory

  - `order_success(request)`: Displays order success page
    - Shows order details
    - Displays payment confirmation
    - Provides order tracking info
    - Shows next steps

  - `order_list(request)`: Shows user's order history
    - Lists all user orders
    - Shows order status
    - Displays order details
    - Provides tracking information

  - `send_order_confirmation_email(user, order, payment_method)`: Sends order confirmation emails
    - Generates email content
    - Includes order details
    - Adds payment information
    - Sends confirmation email

## 🛠️ Technology Stack

- **Python Version**: 3.13.2
- **Frontend**: Django 5.0+
- **Backend API**: FastAPI
- **Database**: XAMPP MySQL
- **Authentication**: JWT Tokens
- **API Documentation**: Swagger UI (FastAPI)
- **Email Service**: SMTP (Gmail)
- **Static Files**: Django Static Files
- **Media Storage**: Local File System

## 📋 Prerequisites

- Python 3.13.2
- XAMPP (for MySQL database)
- pip (Python package manager)
- Virtual Environment (recommended)
- Git

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/UrbanBazzar.git
   cd UrbanBazzar
   ```

2. Create and activate a virtual environment with Python 3.13.2:
   ```bash
   # On Windows
   python -m venv venv --python=python3.13.2
   venv\Scripts\activate

   # On Linux/Mac
   python3.13 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r req.txt
   ```

4. Set up XAMPP MySQL:
   - Start XAMPP Control Panel
   - Start Apache and MySQL services
   - Open phpMyAdmin (http://localhost/phpmyadmin)
   - Create a new database named 'urbanbazzar'
   - Set up database user and permissions

5. Configure database settings in `.env`:
   ```env
   # Database Configuration (XAMPP MySQL)
   DB_NAME=UrbanBazzar_E-commerce
   DB_USER=root
   DB_PASSWORD=  # Leave empty for default XAMPP configuration
   DB_HOST=localhost
   DB_PORT=3306
   ```

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

8. Start the servers:
   ```bash
   # Start FastAPI server (in one terminal)
   uvicorn main:app --host 0.0.0.0 --port 2814

   # Start Django server (in another terminal)
   python manage.py runserver 0.0.0.0:1974
   ```

## 📝 Environment Variables

Create a `.env` file with the following variables:

```env
# Database Configuration (XAMPP MySQL)
DB_NAME=urbanbazzar
DB_USER=root
DB_PASSWORD=  # Leave empty for default XAMPP configuration
DB_HOST=localhost
DB_PORT=3306

# Email Configuration
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=UrbanBazzar <your_email@gmail.com>

# Application URLs
DJANGO_URL=http://localhost:1974
FAST_API_URL=http://localhost:2814

# Security
SECRET_KEY=your_django_secret_key
JWT_SECRET_KEY=your_jwt_secret_key

# Debug Mode (Set to False in production)
DEBUG=True

# Allowed All Hosts
ALLOWED_HOSTS= * 

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:1974,http://localhost:2814 OR *

# Media and Static Files
MEDIA_URL=/media/
STATIC_URL=/static/
STATIC_ROOT=staticfiles/
MEDIA_ROOT=media/

# FastAPI Settings
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=2814

# Django Settings
DJANGO_HOST=0.0.0.0
DJANGO_PORT=1974

# Try-On Configuration
TRY_ON_MODEL_PATH=models/try_on_model
TRY_ON_TEMP_DIR=media/try_on_temp
TRY_ON_RESULT_DIR=media/try_on_results
TRY_ON_MAX_FILE_SIZE=10485760  # 10MB
TRY_ON_ALLOWED_EXTENSIONS=jpg,jpeg,png
```

## 📁 Project Structure

```
UrbanBazzar/
├── manage.py                 # Django's command-line utility
├── req.txt                  # Project dependencies
├── LICENSE                  # MIT License file
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
│
├── UrbanBazzar/            # Project configuration
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── asgi.py            # ASGI configuration
│   └── wsgi.py            # WSGI configuration
│
├── users/                  # User management app
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # User-related forms
│   ├── models.py          # User models
│   ├── urls.py            # User app URLs
│   ├── views.py           # User views and logic
│   └── migrations/        # Database migrations
│
├── store/                  # Store management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── orders/                 # Order processing app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── cart/                   # Shopping cart app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── payments/              # Payment processing app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── urbanbazzar.html  # Home page template
│   ├── Aboutus.html      # About page template
│   ├── ContactUs.html    # Contact page template
│   ├── Tryon.html        # Virtual try-on page template
│   │
│   ├── users/            # User-related templates
│   │   ├── Login_user.html
│   │   ├── Signup_user.html
│   │   ├── Login_otp.html
│   │   ├── Forgetpassword.html
│   │   ├── Resetpassword.html
│   │   └── InvalidResetLink.html
│   │
│   ├── store/            # Store-related templates
│   │   ├── products.html
│   │   ├── product_detail.html
│   │   ├── add_product.html
│   │   ├── edit_product.html
│   │   ├── Vender_dashboard.html
│   │   └── update_order_status.html
│   │
│   ├── orders/           # Order-related templates
│   │   ├── orders.html
│   │   └── order_success.html
│   │
│   ├── cart/             # Cart-related templates
│   │   ├── view_cart.html
│   │   └── Empty_cart.html
│   │
│   └── emails/           # Email templates
│       ├── signup_email.html
│       ├── otp_email.html
│       ├── resend_otp_email.html
│       ├── Login_email.html
│       ├── password_reset_email.html
│       ├── successful_password_reset.html
│       ├── order_place_email.html
│       └── account_deactivation_warning.html
│
├── static/               # Static files
│   ├── css/             # CSS files
│   │   ├── main.css                    # Main stylesheet
│   │   ├── base.css                    # Base styles
│   │   ├── responsive.css              # Responsive design styles
│   │   ├── bootstrap.min.css           # Bootstrap framework
│   │   ├── font-awesome.min.css        # Font Awesome icons
│   │   ├── animate.css                 # Animation effects
│   │   ├── prettyPhoto.css             # Image gallery styles
│   │   ├── price-range.css             # Price filter styles
│   │   ├── Aboutus.css                 # About page styles
│   │   ├── ContactUs.css               # Contact page styles
│   │   ├── Tryon.css                   # Virtual try-on styles
│   │   ├── Empty_cart.css              # Empty cart page styles
│   │   ├── Login_user.css              # Login page styles
│   │   ├── Login_otp.css               # OTP verification styles
│   │   ├── Signup_user.css             # Signup page styles
│   │   ├── Forgetpassword.css          # Password recovery styles
│   │   ├── Resetpassword.css           # Password reset styles
│   │   ├── products.css                # Product listing styles
│   │   ├── product_detail.css          # Product detail page styles
│   │   ├── view_cart.css               # Shopping cart styles
│   │   ├── orders.css                  # Order page styles
│   │   ├── order_success.css           # Order success page styles
│   │   ├── add_product.css             # Add product form styles
│   │   └── Vender_dashboard.css        # Vendor dashboard styles
│   ├── js/              # JavaScript files
│   │   ├── main.js                     # Main JavaScript file
│   │   ├── UrbanBazzar.js              # Core application logic
│   │   ├── jquery.js                   # jQuery library
│   │   ├── bootstrap.min.js            # Bootstrap JavaScript
│   │   ├── jquery.prettyPhoto.js       # Image gallery functionality
│   │   ├── jquery.scrollUp.min.js      # Scroll to top functionality
│   │   ├── gmaps.js                    # Google Maps integration
│   │   ├── html5shiv.js                # HTML5 support for older browsers
│   │   ├── price-range.js              # Price filter functionality
│   │   ├── Tryon.js                    # Virtual try-on functionality
│   │   ├── contact.js                  # Contact form handling
│   │   ├── Login_user.js               # Login page functionality
│   │   ├── Login_otp.js                # OTP verification handling
│   │   ├── Signup_user.js              # Signup page functionality
│   │   ├── Forgetpassword.js           # Password recovery handling
│   │   ├── Resetpassword.js            # Password reset handling
│   │   ├── product_detail.js           # Product detail page functionality
│   │   ├── view_cart.js                # Shopping cart functionality
│   │   └── add_product.js              # Add product form handling
│   └── images/          # Image files
│   
├── staticfiles/         # Collected static files
├── media/              # User-uploaded files
│   ├── try_on_temp/    # Temporary try-on files
│   └── try_on_results/ # Try-on result files
│
└── EC/                 # Virtual Environment
    ├── Scripts/        # Windows executable scripts
    ├── Lib/            # Python libraries
    └── pyvenv.cfg      # Virtual environment configuration
```

## 👥 Authors

- Dev Amdavadi - Initial work

## 🙏 Acknowledgments

- Django documentation
- FastAPI documentation
- All contributors who have helped shape this project

## 👥 Project Roles

The UrbanBazzar platform supports three main user roles, each with specific responsibilities and access levels:

### 1. Admin Role
- **System Management**
  - Full access to Django admin interface
  - User management and role assignment
  - System configuration and settings
  - Database management

- **Platform Oversight**
  - Monitor all transactions
  - Review vendor applications
  - Handle user disputes
  - Manage platform policies

- **Analytics & Reporting**
  - Access to all platform statistics
  - Sales reports and analytics
  - User activity monitoring
  - Performance metrics

### 2. Vendor Role
- **Store Management**
  - Create and manage product listings
  - Upload product images
  - Set prices and inventory
  - Manage product categories

- **Product Management**
  - Add new products with detailed descriptions
  - Upload multiple product images
  - Set product specifications and attributes
  - Manage product variants (size, color, etc.)
  - Set product pricing and discounts
  - Update product stock levels
  - Enable/disable product listings
  - Add product tags and keywords
  - Set shipping options and costs
  - Manage product reviews and ratings

- **Inventory Management**
  - Track stock levels in real-time
  - Set low stock alerts
  - Manage inventory across multiple locations
  - Update stock quantities
  - Handle product returns
  - Process inventory adjustments
  - Generate inventory reports

- **Order Processing**
  - View and process orders
  - Update order status
  - Handle shipping details
  - Process returns/refunds
  - Print shipping labels
  - Track order fulfillment
  - Manage order cancellations
  - Handle customer inquiries

- **Business Analytics**
  - View sales statistics
  - Track inventory levels
  - Monitor customer feedback
  - Access vendor dashboard
  - Generate sales reports
  - Analyze product performance
  - Track revenue and profits
  - Monitor customer behavior

- **Marketing Tools**
  - Create promotional offers
  - Set up discount codes
  - Manage seasonal sales
  - Create product bundles
  - Set up flash sales
  - Manage email campaigns
  - Track marketing performance

- **Customer Service**
  - Respond to customer inquiries
  - Handle customer complaints
  - Process refund requests
  - Manage return requests
  - Provide product support
  - Handle warranty claims
  - Maintain customer relationships

- **Store Settings**
  - Customize store appearance
  - Set up payment methods
  - Configure shipping options
  - Manage store policies
  - Set up tax rules
  - Configure notification settings
  - Manage store hours
  - Set up automated responses

### 3. Buyer Role
- **Shopping Experience**
  - Browse products
  - Search and filter items
  - Use virtual try-on feature
  - Add items to cart

- **Account Management**
  - Create and manage profile
  - Add shipping addresses
  - Save payment methods
  - View order history

- **Order Management**
  - Place orders
  - Track order status
  - Request returns
  - Write product reviews

- **Order Notifications**
  - Order Confirmation Email
    - Order details and summary
    - Product list with quantities
    - Total amount and payment method
    - Shipping address information
    - Estimated delivery time
    - Order tracking number
    - Support contact information

  - Order Status Updates
    - Order processing confirmation
    - Payment confirmation
    - Shipping confirmation
    - Delivery updates
    - Return status notifications

  - Transaction Receipts
    - Detailed invoice
    - Payment confirmation
    - Tax breakdown
    - Shipping charges
    - Discount applied
    - Final amount paid

  - Return/Refund Updates
    - Return request confirmation
    - Return shipping instructions
    - Refund processing status
    - Refund completion notification