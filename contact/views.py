from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    """
    Contact form
    """

    if request.method == 'POST':
        contact_name = request.POST.get('contact-name')
        contact_email = request.POST.get('contact-email')
        contact_message = request.POST.get('contact-message')

        send_mail(
            f"You've got a message from {contact_name} ({contact_email})",
            contact_message,
            contact_email,
            ['thepastrybox.ms4@gmail.com', ]
        )

        messages.success(request, f'Hey {contact_name}! Your message has been \
                         sent 📧 We will get back to you shortly.')
        return render(request, 'contact/contact.html')
    else:
        return render(request, 'contact/contact.html')
