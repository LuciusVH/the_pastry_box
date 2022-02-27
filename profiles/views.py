from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings

from datetime import datetime

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from subscription.models import StripeCustomer

import stripe

# Create your views here.


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated 👍🏻')
        else:
            messages.error(request, 'Update failed. \
                Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripe_subscription_id)
        plan = stripe.Product.retrieve(subscription.plan.product)
        plan_subscription = datetime.fromtimestamp(plan.created)

        pagination = Paginator(orders, 5)
        page = request.GET.get('page')
        orders_list = pagination.get_page(page)

        template = 'profiles/profile.html'
        context = {
            'form': form,
            'orders': orders_list,
            'on_profile_page': True,
            'subscription': subscription,
            'plan': plan,
            'plan_subscription': plan_subscription,
        }

        return render(request, template, context)

    except StripeCustomer.DoesNotExist:
        template = 'profiles/profile.html'
        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

        return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def stripe_customer_portal(request):
    stripe_customer = get_object_or_404(StripeCustomer, user=request.user)

    stripe_customer_id = stripe_customer.stripe_customer_id

    session = stripe.billing_portal.Session.create(
        customer=stripe_customer_id,
        return_url='https://thepastrybox.herokuapp.com/profile/',
    )

    return redirect(session.url)
