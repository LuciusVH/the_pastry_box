from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Subscriber
from .forms import NewsletterSubscriptionForm

# Create your views here.


def newsletter_form(request):

    form = NewsletterSubscriptionForm(request.POST or None)
    context = {
        'form': form
    }

    return render(request, context)


def newsletter_subscription(request):
    """
    A view to manage newsletter subscription
    """

    if request.method == 'POST':
        email = request.POST.get('email', None)
        same_url = request.POST.get('same_url')

        if Subscriber.objects.filter(email__iexact=email).exists():
            messages.error(request, "Email already registered")
            return redirect(same_url)
        else:
            form = NewsletterSubscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Thank you for your subscription 📧")
                return redirect(same_url, no_cart='True')
    else:
        form = NewsletterSubscriptionForm()

    return render(newsletter_form(request))
