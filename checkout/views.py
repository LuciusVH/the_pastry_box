from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def checkout(request):
    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(
            request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': '',
    }

    print(shopping_cart)

    return render(request, template, context)
