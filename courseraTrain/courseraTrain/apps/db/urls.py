from django.contrib import admin
from django.urls import path
from db import views

urlpatterns = [
    path('check/', views.check),
]
