from django.urls import path
from . import views

urlpatterns = [
    path('subscription/', views.newsletter_subscription,
         name='newsletter_subscription'),
    path('send/', views.send_newsletter, name='send_newsletter'),
    path('recipes/', views.display_recipes, name='recipes'),
    path('recipes/<int:post_id>/', views.recipe_detail, name='recipe_detail'),
]
