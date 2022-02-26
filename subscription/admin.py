from django.contrib import admin
from subscription.models import StripeCustomer, StripePlan

# Register your models here.

admin.site.register(StripeCustomer)
admin.site.register(StripePlan)
