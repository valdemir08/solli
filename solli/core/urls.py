from django.urls import path
from . import views
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('get_cities/', views.get_cities, name='get_cities'),
]