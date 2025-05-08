from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserAddress
from .forms import UserAddressForm, UserSecondaryAddressForm
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import pyotp
import hashlib
import random
import requests
import io as io_module
import qrcode
from io import BytesIO
import io as io_module
from django.utils.html import strip_tags

# Fast_API_URL = settings.Fast_API_URL
FAST_API_URL = settings.FAST_API_URL
DJANGO_URL = settings.DJANGO_URL

# Get the user model
User = get_user_model()

def send_signup_email(request, email, firstname):
    """Sends a signup confirmation email to the user."""
    subject = "🎉 Welcome to UrbanBazzar! Your Signup is Successful"
    from_email = "UrbanBazzar Support <support@urbanbazzar.com>"
    to_email = [email]

    # Context for rendering the email template
    context = {
        'firstname': firstname,
        'support_email': 'support@urbanbazzar.com',
        'help_center_url': F'{DJANGO_URL}/contact',  
    }

    # Render email content
    message = render_to_string('emails/signup_email.html', context)

    # Send email
    email_message = EmailMultiAlternatives(subject, message, from_email, to_email)
    email_message.content_subtype = "html"
    email_message.send()

def sending_login_otp_email(user_email, otp_code):
    """Sends the OTP email with the generated OTP code."""

    # Render email template with context including otp_code
    html_content = render_to_string("emails/otp_email.html", {
        "user_email": user_email,
        "otp_code": otp_code,  # <-- Include the OTP here
    })

    # Send email
    subject = "UrbanBazzar Login OTP"
    email = EmailMultiAlternatives(
        subject,
        strip_tags(html_content),
        'UrbanBazzar Security <support@urbanbazzar.com>',
        [user_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def sending_resended_otp_email(user_email, otp_code):
    """Sends a resent OTP email."""
    html_content = render_to_string("emails/resend_otp_email.html", {
        "otp_code": otp_code,         
        "user_email": user_email      
    })

    subject = "UrbanBazzar Resent OTP"
    email = EmailMultiAlternatives(
        subject,
        strip_tags(html_content),
        'UrbanBazzar Security <support@urbanbazzar.com>',
        [user_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()



def send_Login_email(request, email, firstname):
    """Sends a Login confirmation email to the user."""
    subject = "🎉 Welcome to UrbanBazzar! Your Login In UrbanBazzar is Successful"
    from_email = "UrbanBazzar Support <support@urbanbazzar.com>"
    to_email = [email]

    # Context for rendering the email template
    context = {
        'firstname': firstname,
        'support_email': 'support@urbanbazzar.com', #update when live with own domain
        'help_center_url': 'http://localhost:2814/contact',  # Update when live
    }

    # Render email content
    message = render_to_string('emails/Login_email.html', context)

    # Send email
    email_message = EmailMultiAlternatives(subject, message, from_email, to_email)
    email_message.content_subtype = "html"
    email_message.send()

def Deactivate_account_sending_email(email):
    """Sends an email warning about account deactivation due to multiple failed OTP attempts."""
    context = {'support_email': 'support@urbanbazzar.com'}
    html_content = render_to_string("emails/account_deactivation_warning.html", context)

    email_message = EmailMultiAlternatives(
        "UrbanBazzar Account Warning",
        strip_tags(html_content),
        "UrbanBazzar Security <support@urbanbazzar.com>",
        [email]
    )
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()

def send_password_reset_email(user, reset_link):
    """Sends a password reset email using an HTML template."""
    subject = "🔐 UrbanBazzar: Reset Your Password"
    from_email = "UrbanBazzar Support <support@urbanbazzar.com>"
    to_email = [user.email]

    # Render the email template from 'emails/password_reset_email.html'
    message = render_to_string("emails/password_reset_email.html", {"user": user, "reset_link": reset_link})

    mail = EmailMultiAlternatives(subject, message, from_email, to_email)
    mail.content_subtype = "html"  # Set email content as HTML
    mail.send()

def send_successful_reset_password_mail(user):
    """Sends an email notifying the user that their password has been successfully changed."""
    subject = " UrbanBazzar: Password Successfully Changed"
    from_email = "UrbanBazzar Support <support@urbanbazzar.com>"
    to_email = [user.email]
    login_url = f"{settings.DJANGO_URL}/login/user/" 
    
    # Render the email content from a template
    html_message = render_to_string("emails/successful_password_reset.html", {"user": user, "login_url": login_url })
    plain_message = strip_tags(html_message)
    
    mail = EmailMultiAlternatives(subject, plain_message, from_email, to_email)
    mail.attach_alternative(html_message, "text/html")
    mail.send()

def signup_user(request):
    """Handles user signup, validates input, and sends a confirmation email."""
    FAST_API_SIGNUP = f"{FAST_API_URL}/users/signup/"
    if request.method == "POST":
        fullname = request.POST.get("fullname", "").strip()
        first_name, last_name = (fullname.split(" ", 1) + [""])[:2]
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        role = request.POST.get("role", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirmpassword", "").strip()

        # Server-side validation
        if not fullname:
            messages.error(request, "Full Name is required.")
        elif not username:
            messages.error(request, "Username is required.")
        elif not email:
            messages.error(request, "Email is required.")
        elif not password:
            messages.error(request, "Password is required.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
        else:
            data = {
                "username": username,
                "email": email,
                "role": role,
                "password": password,
            }

            try:
                response = requests.post(FAST_API_SIGNUP, json=data)
                if response.status_code == 200:
                    request.session['first_name'] = first_name
                    send_signup_email(request, email, first_name)
                    messages.success(
                        request, "Signup successful! A verification link has been sent to your email."
                    )
                    return redirect("users:Login_user")
                else:
                    error_detail = response.json().get("detail", "Signup failed. Please try again.")
                    messages.error(request, error_detail)
            except Exception as e:
                messages.error(request, f"Error connecting to signup service: {str(e)}")

        return redirect('users:Signup_user')

    return render(request, "users/Signup_user.html")   

def login_user(request):
    """Handles user login with email and password authentication via FastAPI."""
    FASTAPI_LOGIN_URL = f"{FAST_API_URL}/users/login/"
    FASTAPI_Authorized_User_URL = f"{FAST_API_URL}/users/token/"

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        # Validate input
        if not email:
            messages.error(request, "Email ID is required")
            return redirect('users:Login_user')
        if not password:
            messages.error(request, "Password is required")
            return redirect('users:Login_user')

        # Prepare data for FastAPI
        login_data = {
            "email": email,
            "password": password
        }

        auth_data = {
            "username": email,  # OAuth2 expects 'username' not 'email'
            "password": password
        }
        
        # Authorized API Based on user 
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            response = requests.post(FASTAPI_Authorized_User_URL, data=auth_data, headers=headers)
            print("FastAPI raw response:", response.text)  # DEBUG

            if response.status_code == 200:
                print("Authorized Successfully")
                token_data = response.json()
                access_token = token_data.get("access_token")
                request.session["access_token"] = access_token  # Store in session
                # print("😀🥸🥳☺️😔😲",access_token)  # DEBUG
            else:
                messages.error(request, "Authorization failed")
                return redirect('users:Login_user')
        except Exception as e:
            print("🔴 Exception while calling token endpoint:", str(e))
            messages.error(request, f"Authorization error: {str(e)}")
            return redirect('users:Login_user')

        try:
            response = requests.post(FASTAPI_LOGIN_URL, json=login_data)
            # print("FastAPI raw response:", response.text)  # 🔍 DEBUG

            if response.status_code == 200:
                user_data = response.json()

                # Set session data
                request.session['otp_code'] = user_data.get('otp')
                request.session['email'] = user_data.get('email')
                request.session['user_name'] = user_data.get('username')

                # Optionally authenticate in Django (optional if you're not using Django auth)
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)

                # Send OTP to user's email
                sending_login_otp_email(user_data['email'], user_data['otp'])

                messages.success(request, "Enter the OTP sent to your email to log in to UrbanBazzar")
                return redirect("users:Login_otp")

            else:
                # Handle error response from FastAPI
                try:
                    error_data = response.json()
                    messages.error(request, error_data.get('detail', 'Login failed'))
                except:
                    messages.error(request, "Login failed: Unexpected response format")
                return redirect('users:Login_user')

        except Exception as e:
            print("🔴 Exception while calling FastAPI:", str(e))
            messages.error(request, f"Error connecting to FastAPI: {str(e)}")
            return redirect('users:Login_user')

    return render(request, "users/Login_user.html")

def Verify_Login_otp(request):
    if request.method == "POST":
        entered_otp = "".join(
            filter(str.isdigit, ''.join(request.POST.get(f'otp{i}', "") for i in range(1, 7)))
        )
        session_otp = request.session.get('otp_code')
        email = request.session.get('email')

        if not session_otp or not email:
            messages.error(request, "Session expired. Please log in again.")
            return redirect('users:Login_user')

        attempt_count = request.session.get('otp_attempts', 0)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('users:Login_user')

        if entered_otp == session_otp:
            FASTAPI_VERIFY_OTP_URL = f"{FAST_API_URL}/users/verify-otp"
            otp_data = {"email": email, "otp": entered_otp}

            try:
                response = requests.post(FASTAPI_VERIFY_OTP_URL, json=otp_data)

                if response.status_code == 200:
                    data = response.json()

                    #  Extract JWT token from FastAPI
                    token = data.get("access_token")
                    token_type = data.get("token_type")

                    #  Optionally store the token
                    request.session['jwt_token'] = token
                    request.session['jwt_token_type'] = token_type

                    # print(token, token_type)

                    login(request, user)
                    request.session['otp_attempts'] = 0
                    messages.success(request, "OTP Verified! You are logged in.")

                    send_Login_email(request, email, user.first_name)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid OTP! Please try again.")
                    return redirect('users:Login_otp')

            except requests.exceptions.RequestException as e:
                messages.error(request, f"Error connecting to FastAPI: {e}")
                return redirect('users:Login_otp')

        else:
            attempt_count += 1
            request.session['otp_attempts'] = attempt_count

            if attempt_count >= 3:
                user.is_active = False
                user.save()
                Deactivate_account_sending_email(email)
                messages.error(request, "Too many failed OTP attempts! Contact the admin.")
                return redirect('users:Login_user')

            messages.error(request, "Invalid OTP! Please try again.")
            return redirect('users:Login_otp')

    return render(request, 'users/Login_otp.html')

def Resend_user_Login_otp(request):
    email = request.session.get('email')
    
    if not email:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('users:Login_user')

    user = User.objects.filter(email=email).first()
    if not user:
        messages.error(request, "User not found. Please log in again.")
        return redirect('users:Login_user')

    try:
        # Call FastAPI endpoint to generate a new OTP
        FASTAPI_RESEND_OTP_URL = f"{FAST_API_URL}/users/resend-otp/"  
        response = requests.post(FASTAPI_RESEND_OTP_URL, data={"email": email})
        
        if response.status_code == 200:
            data = response.json()
            otp_code = data.get("otp")

            request.session['otp_code'] = otp_code
            sending_resended_otp_email(email, otp_code)  

            messages.success(request, "A new OTP has been sent to your email.")
            return redirect('users:Login_otp')
        else:
            messages.error(request, "Failed to resend OTP. Please try again.")
            return redirect('users:Login_otp')

    except Exception as e:
        messages.error(request, f"Error contacting OTP service: {str(e)}")
        return redirect('users:Login_user')


def password_reset_request(request):
    """Handles password reset requests and sends a reset link to the user's email."""
    if request.method == "POST":
        email = request.POST.get("email")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print("User Exists with Email!!")

            FAST_API_PASSWORD_RESET_REQUEST = f"{FAST_API_URL}/users/forgot-password"
            data = {"email": email}

            try:
                response = requests.post(FAST_API_PASSWORD_RESET_REQUEST, data=data)
                if response.status_code == 200:
                    reset_link = response.json().get("reset_link")
                    send_password_reset_email(user, reset_link)
                    messages.success(request, "Password reset link sent to your email.")
                else:
                    messages.error(request, "Failed to send reset link via FastAPI.")
            except requests.exceptions.RequestException as e:
                messages.error(request, "Error while contacting FastAPI: " + str(e))
        else:
            messages.error(request, "User does not exist.")

    return render(request, 'users/Forgetpassword.html')


def Reset_password(request, token):
    """Handles password reset via token (provided by FastAPI)."""

    FASTAPI_RESET_PASSWORD_URL = f"{FAST_API_URL}/users/reset-password-by-link"

    if request.method == "POST":
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if not password or not confirmpassword:
            messages.error(request, "All fields are required.")
            return redirect("users:Reset_password", token=token)

        if password != confirmpassword:
            messages.error(request, "Passwords do not match.")
            return redirect("users:Reset_password", token=token)

        data = {
            "token": token,
            "new_password": password,
            "confirm_password": confirmpassword
        }

        try:
            response = requests.post(FASTAPI_RESET_PASSWORD_URL, json=data)
            if response.status_code == 200:
                # You may optionally fetch user via token, or skip login if not possible
                messages.success(request, "Password reset successfully.")
                return redirect("users:Login_user")
            else:
                messages.error(request, "Failed to reset the password.")
        except requests.exceptions.RequestException as e:
            if e. response.status_code == 400:
                try:
                    error_detail = e.response.json().get("detail", "Something went wrong.")
                    messages.error(request, error_detail)
                except ValueError:
                    messages.error(request, f"Error connecting to the API: {str(e)}")
            else:
                messages.error(request, "An unexpected error occurred. Please try again.")

    return render(request, "users/Resetpassword.html", {"token": token})

# View to add a primary address
@login_required
def add_primary_address(request):
    if request.method == 'POST':
        form = UserAddressForm(request.POST)
        if form.is_valid():
            primary_address = form.save(commit=False)
            primary_address.user = request.user
            primary_address.save()
            messages.success(request, "Primary address saved successfully.")
            return redirect('cart:view_cart')  # Redirect to the cart view after saving
    else:
        form = UserAddressForm()
    return render(request, 'users/add_address_modal.html', {'form': form})

# View to add a secondary address
@login_required
def add_secondary_address(request):
    if request.method == 'POST':
        form = UserSecondaryAddressForm(request.POST)
        if form.is_valid():
            secondary_address = form.save(commit=False)
            secondary_address.user = request.user
            secondary_address.save()
            messages.success(request, "Secondary address saved successfully.")
            return redirect('cart:view_cart')  # Redirect to the cart view after saving
    else:
        form = UserSecondaryAddressForm()
    return render(request, 'users/add_address_modal.html', {'form': form})


def logout_user(request):
    """Logs out the user and redirects to the login page."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('users:Login_user')
