from django.urls import path

from . import views

urlpatterns = [
    path('', views.random, name='random'),
    path('list/', views.list, name='list'),
]

