from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class StripePlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stripe_price_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def displayed_price(self):
        return "{0:.2f}".format(self.price / 1000)
