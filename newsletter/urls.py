from django.urls import path
from . import views

urlpatterns = [
    path('subscription/', views.newsletter_subscription,
         name='newsletter_subscription'),
    path('send/', views.send_newsletter,
         name='send_newsletter'),
]
