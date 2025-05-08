import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from store.models import Product
from users.models import UserAddress, UserSecondaryAddress
from cart.models import ShoppingSession, CartItem
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

FAST_API_URL = settings.FAST_API_URL
# print(FAST_API_URL)

# ——————————————————————————————————————————
# View to add a product to the user's shopping cart
@login_required
def add_to_cart(request, product_id):
    # still check product exists in Django for 404
    get_object_or_404(Product, pk=product_id)

    # Get token from session
    access_token = request.session.get('access_token')
    # print(access_token)
    if not access_token:
        return HttpResponse("Unauthorized: No token found", status=401)

    # call FastAPI with Bearer token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # resp = requests.post(f"{FAST_API_URL}/cart/add/{product_id}")
    resp = requests.post(f"{FAST_API_URL}/cart/add/{product_id}", headers=headers)

    if resp.status_code != 200:
        return HttpResponse("Error adding to cart", status=resp.status_code)
    else:
        data = resp.json()
        product_name = data.get("product_name")

    # if AJAX, return just a message
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return HttpResponse(resp.json().get("detail", f'"{product_name}" Added To Your Cart'))

    # otherwise redirect to our cart page
    return redirect('cart:view_cart')


# ——————————————————————————————————————————
# View to display the current user's cart
@login_required
def view_cart(request):

    # Get token from session
    access_token = request.session.get("access_token")
    if not access_token:
        return HttpResponse("Unauthorized: No token found", status=401)
    
    # Include token in request
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # fetch cart from FastAPI
    resp = requests.get(f"{FAST_API_URL}/cart/view", headers=headers)
    if resp.status_code != 200:
        # treat no session as empty cart
        cart_items = []
        cart_total = 0
    else:
        data = resp.json()
        cart_items = data.get("cart_items", [])
        cart_total = data.get("total", 0)
        
        for item in cart_items:
            product_id = item.get("product_id")
            if product_id:
                product_image_url = item.get("image", "")
                item["image_url"] = product_image_url 
                # print(product_image_url) # For Debugging

    # Django addresses logic unchanged
    user_addresses = UserAddress.objects.filter(user=request.user)
    user_secondary_addresses = UserSecondaryAddress.objects.filter(user=request.user)
    address_count = user_addresses.count()
    secondary_address_count = user_secondary_addresses.count()
    show_add_address_button = address_count > 0 and secondary_address_count == 0

    data = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'user_addresses': user_addresses,
        'user_secondary_addresses': user_secondary_addresses,
        'address_count': address_count,
        'secondary_address_count': secondary_address_count,
        'show_add_address_button': show_add_address_button,
    }

    return render(request, 'cart/view_cart.html', data)


# ——————————————————————————————————————————
# View to update the quantity of a cart item
@require_POST
@login_required
def update_cart_item(request, item_id):    
    qty = request.POST.get('quantity')
    
    try:
        qty = int(qty)
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity.")
        return redirect('cart:view_cart')
    
    # Get token from session
    access_token = request.session.get("access_token")
    if not access_token:
        messages.error(request, "Unauthorized: No token found.")
        return redirect('cart:view_cart')

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    }

    # Call FastAPI to update the item with the token in the header
    resp = requests.post(
        f"{FAST_API_URL}/cart/update/{item_id}",
        json={"quantity": qty},
        headers=headers,
    )

    # Debugging the response
    # print(f"FastAPI response status code: {resp.status_code}")
    # print(f"FastAPI response body: {resp.text}")
    
    if resp.status_code != 200:
        messages.error(request, "Could not update cart item.")
    return redirect('cart:view_cart')


# ——————————————————————————————————————————
# View to remove a cart item
@require_POST
@login_required
def remove_cart_item(request, item_id):

    # Get token from session
    access_token = request.session.get("access_token")
    if not access_token:
        messages.error(request, "Unauthorized: No token found.")
        return redirect('cart:view_cart')
    
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    # call FastAPI remove with the token in the header
    requests.post(f"{FAST_API_URL}/cart/remove/{item_id}", headers=headers)

    return redirect('cart:view_cart')