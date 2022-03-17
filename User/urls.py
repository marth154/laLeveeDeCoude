from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginCredentials, name="login"),
    path('register/', views.registerCredentials, name="register")
]
