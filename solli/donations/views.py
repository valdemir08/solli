from django.db import transaction
from django.shortcuts import render, redirect

from .forms import DonationForm
from core.forms import LocationForm, ImageForm
# Create your views here.


def list_donations(request):
    return render(request,'donations/list.html')

def create_donation(request):
    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        location_form = LocationForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if donation_form.is_valid() and location_form.is_valid() and image_form.is_valid():
            #o transaction atomic tem que ser usado para garantir o correto salvamento dos dados
            #ele garante que salva tudo ou nada

            with transaction.atomic():
                location = location_form.save()

                # salvar doação, mas ainda sem commit para setar local
                donation = donation_form.save(commit=False)
                #setou
                donation.local = location\
                #salvar
                donation.save()

                # salvar imagem vinculando à doação
                image = image_form.save(commit=False)
                image.entry = donation
                image.save()

            return redirect('core:landing')
        else:
            print("Erros donation:", donation_form.errors)
            print("Erros location:", location_form.errors)
            print("Erros image:", image_form.errors)
    else:
        donation_form = DonationForm()
        location_form = LocationForm()
        image_form = ImageForm()
    context = {
        'donation_form': donation_form,
        'location_form': location_form,
        'image_form': image_form,
    }
    return render(request, 'donations/create.html', context)
