from django.contrib import admin
from django.urls import path
from routing import views

urlpatterns = [
    path('simple_route/', views.simple_route),
    path('slug_route/<slug:slug>/', views.slug_route),
    path('sum_route/<str:first>/<str:second>/', views.sum_route),
    path('sum_get_method/', views.sum_get_method),
    path('sum_post_method/', views.sum_post_method)
]
