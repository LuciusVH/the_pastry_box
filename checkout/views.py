from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from shopping_cart.contexts import cart_contents

import stripe
from django.conf import settings

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY

    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(
            request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
      amount=stripe_total,
      currency=settings.STRIPE_CURRENCY,

    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    print(shopping_cart)

    return render(request, template, context)
