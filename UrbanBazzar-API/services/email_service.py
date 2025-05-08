import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL", SMTP_USERNAME)


def send_email(to_email: str, subject: str, body: str) -> bool:
    try:
        # Construct email message
        msg = MIMEMultipart()
        msg["From"] = FROM_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "html"))

        # Connect and send
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def send_otp_email(to_email: str, otp: str) -> bool:
    subject = "Your OTP Code"
    body = f"""
        <h3>Your OTP Code</h3>
        <p>Your OTP is: <strong>{otp}</strong></p>
        <p>This code will expire in 10 minutes.</p>
    """
    return send_email(to_email, subject, body)


def send_verification_email(to_email: str, verification_link: str) -> bool:
    subject = "Verify Your Account"
    body = f"""
        <h3>Account Verification</h3>
        <p>Click the link below to verify your email:</p>
        <a href="{verification_link}">Verify Email</a>
    """
    return send_email(to_email, subject, body)
