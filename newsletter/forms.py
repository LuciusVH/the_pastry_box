from django import forms
from .models import NewsletterContent, Subscriber


class NewsletterSubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """

        super().__init__(*args, **kwargs)
        placeholder = 'Email'

        self.fields['email'].widget.attrs['placeholder'] = placeholder
        self.fields['email'].widget.attrs['class'] = ('form-control')
        self.fields['email'].label = False


class NewsletterContentForm(forms.ModelForm):

    class Meta:
        model = NewsletterContent
        fields = '__all__'
