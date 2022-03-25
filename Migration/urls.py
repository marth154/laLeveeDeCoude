from django.urls import path
from . import views

urlpatterns = [
    path('migration/', views.import_data, name="import_data"),
]
