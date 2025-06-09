from django.shortcuts import render, redirect

from django.http import JsonResponse
from .models import Location

def landing(request):
    return render(request, 'core/landing.html')

def get_cities(request):
    estate = request.GET.get('estate')
    cities = Location.objects.filter(estate=estate).order_by('city')
    city_list = [{'id': loc.id, 'name': loc.city} for loc in cities]
    return JsonResponse({'cities': city_list})