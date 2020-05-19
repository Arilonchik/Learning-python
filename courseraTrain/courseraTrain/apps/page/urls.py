from django.contrib import admin
from django.urls import path
from page import views
urlpatterns = [
    path('main/', views.main_page),
    path('logreg/', views.logreg, name='logreg'),
    path('user_det/<int:id>', views.userdetail, name='us_det'),
    path('tag/<str:tag>', views.tag_news, name='tag_news'),
]

