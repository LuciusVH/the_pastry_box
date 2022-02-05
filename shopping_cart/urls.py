from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_cart, name='view_shopping_cart'),
    path('add/<product_sku>/', views.add_to_shopping_cart,
         name='add_to_shopping_cart'),
]
