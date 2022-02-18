from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_cart, name='view_shopping_cart'),
    path('add/<product_id>/', views.add_to_shopping_cart,
         name='add_to_shopping_cart'),
    path('buy/<product_id>/', views.buy_now, name='buy_now'),
    path('adjust/<product_id>/', views.adjust_shopping_cart,
         name='adjust_shopping_cart'),
    path('remove/<product_id>/', views.remove_from_shopping_cart,
         name='remove_from_shopping_cart'),
]
