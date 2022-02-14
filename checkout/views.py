from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shopping_cart.contexts import cart_contents

import stripe
from django.conf import settings

# Create your views here.


def checkout(request):
    """
    Handle checkout
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_cart = request.session.get('shopping_cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country']
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in shopping_cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't \
                        found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_shopping_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
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

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkout
    """
    # save_info = request.session.get('save_info')
    request.session.get('save_info')
    # newline = '\n'
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \n \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'shopping_cart' in request.session:
        del request.session['shopping_cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
