from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>/', views.order_history,
         name='order_history'),
    path('stripe_customer_portal/', views.stripe_customer_portal,
         name='stripe_customer_portal'),
]
