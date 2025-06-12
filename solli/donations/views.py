from django.conf import settings
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Image
from .forms import DonationForm
from core.forms import LocationForm, ImageForm, BaseEntryCategoryForm
from django.contrib.contenttypes.models import ContentType
from core.utils import process_image
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Donation


def list_donations(request):
    donations = Donation.objects.all().order_by('-created_at')
    donation_type = ContentType.objects.get_for_model(Donation)

    donations_with_images = []
    for donation in donations:
        first_image = Image.objects.filter(
            content_type=donation_type,
            object_id=donation.id
        ).first()
        donations_with_images.append({
            'donation': donation,
            'image_url': first_image.image.url if first_image else None,
        })
    print(donations_with_images)
    context = {
        'donations_with_images': donations_with_images,
    }
    return render(request, 'donations/list.html', context)

@login_required
def create_donation(request):
    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        location_form = LocationForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if donation_form.is_valid() and location_form.is_valid() and image_form.is_valid():
            try:
                with transaction.atomic():
                    # Salva localização e doação
                    location = location_form.save()
                    donation = donation_form.save(commit=False)
                    donation.user = request.user
                    donation.location = location
                    donation.save()

                    # Processa o crop da imagem (se dados existirem)
                    image = image_form.save(commit=False)
                    try:
                        x = int(request.POST.get('x', 0))
                        y = int(request.POST.get('y', 0))
                        width = int(request.POST.get('width', 0))
                        height = int(request.POST.get('height', 0))
                        if width == 0 or height == 0:
                            x = y = width = height = None
                    except (ValueError, TypeError):
                        x = y = width = height = None

                    file_name, jpeg_file = process_image(
                        image.image,
                        x=x, y=y, width=width, height=height
                    )
                    image.image.save(file_name, jpeg_file, save=False)

                    # Vincula a imagem à doação
                    image.content_type = ContentType.objects.get_for_model(donation)
                    image.object_id = donation.id
                    image.save()

                    messages.success(request, "Criado com sucesso!")
                return redirect('core:landing')

            except Exception as e:
                # Log de erro (opcional)
                print(f"Erro durante a transação: {e}")
                # Os forms já terão os erros adicionados

        else:
            print("Formulários inválidos:", donation_form.errors, location_form.errors, image_form.errors)
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

def donation_detail(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation_type = ContentType.objects.get_for_model(Donation)
    image = Image.objects.filter(
        content_type=donation_type,
        object_id=donation.id
    ).first()

    return render(request, 'donations/detail.html', {
        'donation': donation,
        'donation_image': image.image.url if image else None,
    })

from django.shortcuts import get_object_or_404

@login_required
def edit_donation(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)  # Garante que o usuário edita só as suas doações
    location = donation.location
    # Pegamos a imagem vinculada (assumindo que só tem uma)
    image = donation.images.first() if donation.images.exists() else None

    if request.method == 'POST':
        donation_form = DonationForm(request.POST, instance=donation)
        location_form = LocationForm(request.POST, instance=location)
        image_form = ImageForm(request.POST, request.FILES, instance=image)

        if donation_form.is_valid() and location_form.is_valid() and image_form.is_valid():
            try:
                with transaction.atomic():
                    location = location_form.save()
                    donation = donation_form.save(commit=False)
                    donation.location = location
                    donation.save()

                    image = image_form.save(commit=False)

                    try:
                        x = int(request.POST.get('x', 0))
                        y = int(request.POST.get('y', 0))
                        width = int(request.POST.get('width', 0))
                        height = int(request.POST.get('height', 0))
                        if width == 0 or height == 0:
                            x = y = width = height = None
                    except (ValueError, TypeError):
                        x = y = width = height = None

                    if image.image:
                        file_name, jpeg_file = process_image(
                            image.image,
                            x=x, y=y, width=width, height=height
                        )
                        image.image.save(file_name, jpeg_file, save=False)

                    image.content_type = ContentType.objects.get_for_model(donation)
                    image.object_id = donation.id
                    image.save()

                    messages.success(request, "Editado com sucesso!")
                return redirect('core:landing')

            except Exception as e:
                print(f"Erro na edição: {e}")

    else:
        donation_form = DonationForm(instance=donation)
        location_form = LocationForm(instance=location)
        image_form = ImageForm(instance=image)

    context = {
        'donation_form': donation_form,
        'location_form': location_form,
        'image_form': image_form,
        'donation': donation,  # instancia de donation para identificar se é create ou delete
    }
    return render(request, 'donations/create.html', context)


