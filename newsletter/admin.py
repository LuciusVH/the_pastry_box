from django.contrib import admin
from .models import Subscriber, NewsletterContent
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(NewsletterContent)
