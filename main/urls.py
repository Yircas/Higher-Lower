from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("random_anime", views.random_anime, name='random_anime'),
]