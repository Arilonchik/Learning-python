from django.urls import path
from template import views


urlpatterns = [
    path('echo/', views.echo),
    path('tag/', views.tag_check),
    path('extend/', views.extends),
]
