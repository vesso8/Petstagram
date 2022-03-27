from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms import CreatePetPhotoForm, EditPetPhotoForm
from petstagram.main.models import Pet_photo, Pet


class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin ,views.DetailView):
    model = Pet_photo
    template_name = 'templates_main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):

        return super()\
            .get_queryset()\
            .prefetch_related('tagged_pets')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        return context


# def error(request):
#     return render(request, '401_error.html')
class CreatePetPhotoView(auth_mixins.LoginRequiredMixin ,views.CreateView):
    template_name = 'templates_main/photo_create.html'
    form_class = CreatePetPhotoForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#CreatePetPhotoView without CreatePetPhotoForm
# class CreatePetPhotoView(views.CreateView):
#       model = Pet_photo
#     template_name = 'templates_main/photo_create.html'
#     fields = ('photo', 'description', 'tagged_pets')
#     success_url = reverse_lazy('dashboard')


def like_pet_photo(request, pk):
    pet_photo = Pet_photo.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


class EditPetPhotoView(views.UpdateView):
    model = Pet_photo
    template_name = 'templates_main/photo_edit.html'
    form_class = EditPetPhotoForm
    success_url = reverse_lazy('dashboard')
    # fields = ('description', 'tagged_pets')


# def edit_photo(request, pk):
#     return photo_action(request, EditPetPhotoForm, 'dashboard' , Pet_photo.objects.get(pk=pk), 'photo_edit.html')

def delete_photo(request, pk):
    photo = Pet_photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
