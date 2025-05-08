# Import necessary Django modules and app models
from django.shortcuts import render, redirect, get_object_or_404
from users.models import UserAddress, UserSecondaryAddress
from cart.models import CartItem, ShoppingSession
from orders.models import OrderDetails, OrderItems
from payments.models import PaymentDetails
from store.models import Product
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.views.decorators.http import require_POST

FAST_API_URL = settings.FAST_API_URL
DJANGO_URL = settings.DJANGO_URL


def send_order_confirmation_email(user, order, payment_method):
    email_subject = '🛍️ Your Order Confirmation - UrbanBazzar'

    email_context = {
        'firstname': user.first_name,
        'order_number': order['id'],
        'total_amount': order['total'],
        'shipping_address': f"{order['address']}, {order['city']}, {order['pincode']}, {order['country']}",
        'payment_method': payment_method.upper(),
        'support_email': 'support@urbanbazzar.com',
        'help_center_url': f'{DJANGO_URL}/Contact-Us/',
    }

    email_body = render_to_string('emails/order_place_email.html', email_context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
    )
    email.content_subtype = "html"
    email.send(fail_silently=False)

@login_required
def confirm_order(request):
    if request.method == "POST":
        address_id = request.POST.get('selected_address')
        payment_method = request.POST.get('payment_method')
        # print(payment_method)
        upi_id = request.POST.get('upi_id', '')

        if not address_id:
            messages.error(request, "Please select a shipping address.")
            return redirect('cart:view_cart')

        address_obj = (
            UserAddress.objects.filter(id=address_id, user=request.user).first() or
            UserSecondaryAddress.objects.filter(id=address_id, user=request.user).first()
        )


        if not address_obj:
            messages.error(request, "Invalid address selection.")
            return redirect('cart:view_cart')

        # Existing variables 
        address = address_obj.address
        city = address_obj.city
        pincode = address_obj.pincode
        country = address_obj.country
        mobile = address_obj.mobile

        # Call the FastAPI order creation endpoint
        try:
            api_url = f"{FAST_API_URL}/orders/"  
            payload = {
                "address": address,
                "city": city,
                "pincode": pincode,
                "country": country,
                "mobile": mobile,
                "payment_method": payment_method,
                "upi_id": upi_id,
            }
            # print(payload.payment_method)

            headers = {
                "Authorization": f"Bearer {request.session.get('access_token')}"
            }

            response = requests.post(api_url, json=payload, headers=headers)
            response.raise_for_status()
            order_data = response.json()

            send_order_confirmation_email(request.user, order_data, payment_method)
            messages.success(request, "Order placed successfully!")
            return redirect('orders:order_success')

        except requests.exceptions.RequestException as e:
            if e.response.status_code == 400:
                try:
                    error_detail = e.response.json().get("detail", "Something went wrong.")
                    messages.error(request, error_detail)
                except ValueError:
                    messages.error(request, "Something went wrong while placing the order.")
            else:
                messages.error(request, "An unexpected error occurred. Please try again.")

    return redirect('cart:view_cart')

# View to render the order success page
@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')  # Display success template


# View to list all orders placed by the user
@login_required
def order_list(request):
    # Get user's orders, most recent first
    orders = OrderDetails.objects.filter(user=request.user).order_by('-created_at')

    # Add line_total for each order item for display
    for order in orders:
        for item in order.orderitems.all():  
            item.line_total = item.product.price * item.quantity

    # Render orders in template
    return render(request, 'orders/orders.html', {'orders': orders})