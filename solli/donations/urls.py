from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('create', views.create_donation, name='create_donation'),
]