from newsletter.forms import NewsletterSubscriptionForm


def newsletter_form_global(request):

    return {
        'newsletter_form': NewsletterSubscriptionForm()
    }
