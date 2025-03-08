from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('get', views.get_data),
]