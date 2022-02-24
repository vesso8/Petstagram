from django.shortcuts import render, redirect

from petstagram.main.forms import CreatePetPhotoForm, EditPetPhotoForm
from petstagram.main.models import Pet_photo, Pet
from petstagram.main.helpers import get_profile


def show_photo_details(request, pk):
    pet_photo = Pet_photo.objects\
        .prefetch_related('tagged_pets')\
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)

# def error(request):
#     return render(request, '401_error.html')

def like_pet_photo(request, pk):
    pet_photo = Pet_photo.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)

def photo_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'photo': instance,
    }
    return render(request, template_name, context)

def create_photo(request):
    return photo_action(request, CreatePetPhotoForm, 'dashboard', Pet_photo(), 'photo_create.html')


# def edit_photo(request, pk):
#     return photo_action(request, EditPetPhotoForm, 'dashboard' , Pet_photo.objects.get(pk=pk), 'photo_edit.html')

def delete_photo(request, pk):
    photo = Pet_photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')


def edit_photo(request, pk):
    photo = Pet_photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('pet photo details', pk)
    else:
        form = EditPetPhotoForm(instance=photo)
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photo_edit.html', context)