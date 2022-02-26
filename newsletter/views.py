from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django_pandas.io import read_frame

from .models import Subscriber
from .forms import NewsletterSubscriptionForm, NewsletterContentForm

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
                return redirect(same_url)
    else:
        form = NewsletterSubscriptionForm()

    return render(newsletter_form(request))


@login_required
def send_newsletter(request):
    """
    A view to send newsletter to subscribers
    """

    if not request.user.is_superuser:
        messages.error(request, 'You\'re not there yet my dear, sorry 😏')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewsletterContentForm(request.POST)
        if form.is_valid():
            subscribers = Subscriber.objects.all()
            emails = read_frame(subscribers, fieldnames=['email'])
            emailing_list = emails['email'].values.tolist()
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('content')
            send_mail(
                title,
                message,
                '',
                emailing_list,
                fail_silently=False,
            )
            messages.success(request,
                             "Your dope newsletter has been sent! 🤜🏻💥")
            return redirect('send_newsletter')
    else:
        form = NewsletterContentForm()
        template = 'newsletter/send.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
