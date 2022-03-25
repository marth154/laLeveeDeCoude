from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginCredentials, name="login"),
    path('register/', views.registerCredentials, name="register"),
    path('bar/', views.bar, name="bar"),
    path('bar/drinks_user/', views.drinks_user, name="drinks_user"),
    path('bar/favorites_user/', views.favorites_user, name="favorites_user"),
]
