from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.list_donations, name='list_donations'),
    path('create/', views.create_donation, name='create_donation'),
    path('<int:id>/', views.donation_detail, name='donation_detail'),
    path('<int:donation_id>/edit/', views.edit_donation, name='edit_donation'),
]