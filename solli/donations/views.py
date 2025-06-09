from django.db import transaction
from django.shortcuts import render, redirect

from .forms import DonationForm
from core.forms import LocationForm, ImageForm, BaseEntryCategoryForm
from django.contrib.contenttypes.models import ContentType

from .models import Donation


# Create your views here.


def list_donations(request):
    donations = Donation.objects.all().order_by('-created_at')  #ordenação por data
    return render(request, 'donations/list.html', {'donations': donations})

def create_donation(request):
    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        location_form = LocationForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if donation_form.is_valid() and location_form.is_valid() and image_form.is_valid():
            #o transaction atomic tem que ser usado para garantir o correto salvamento dos dados
            #ele garante que salva tudo ou nada
            print('entrou')
            with transaction.atomic():
                location = location_form.save()
                #category = category_form.save()

                # salvar doação, mas ainda sem commit para setar local
                donation = donation_form.save(commit=False)
                #setou
                donation.location = location
                #salvar
                print(donation.location)
                donation.save()

                # salvar imagem vinculando à doação
                image = image_form.save(commit=False)
                image.content_type = ContentType.objects.get_for_model(donation)
                image.object_id = donation.id
                image.save()

            return redirect('core:landing')
        else:
            print("Donation form is valid:", donation_form.is_valid())
            print("Location form is valid:", location_form.is_valid())
            print("Image form is valid:", image_form.is_valid())

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
