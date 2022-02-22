from django.urls import path
from . import views

urlpatterns = [
    path('subscription/', views.newsletter_subscription,
         name='newsletter_subscription'),
]
