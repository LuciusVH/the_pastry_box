from django.shortcuts import redirect, render, reverse
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

import stripe

from django.contrib.auth.models import User
from .models import StripePlan, StripeCustomer

# Create your views here.


def plans(request):
    """ A view to show the different plans """

    plans = StripePlan.objects.all()

    return render(request, 'subscription/plans.html', {'plans': plans})


def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config)


def create_checkout_session(request, price_id):
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=(request.user.id if request.user.is_authenticated else None),
                success_url=domain_url + 'subscription/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'subscription/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1,
                    }
                ],
            )
            return JsonResponse({'sessionId': checkout_session['id']})

        except Exception as e:
            return JsonResponse({'error': str(e)})


def subscription_success(request):
    messages.success(request, 'You have successfully subscribed to The Box!')
    return redirect(reverse('profile'))


@csrf_exempt
def subscription_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_SUBSCRIPTION_WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripe_customer_id=stripe_customer_id,
            stripe_subscription_id=stripe_subscription_id,
        )

    return HttpResponse(status=200)
