from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('config/', views.stripe_config),
    path('create-checkout-session/<str:price_id>/',
         views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.subscription_success),
    path('wh/', views.subscription_webhook),
]
