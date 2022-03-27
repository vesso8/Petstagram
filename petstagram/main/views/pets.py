from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main.models import Pet

class CreatePetView(views.CreateView):
    template_name = 'templates_main/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class EditPetView(views.UpdateView):
    model = Pet
    template_name = 'templates_main/pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('dashboard')

class DeletePetView(views.DeleteView):
    model = Pet
    template_name = 'templates_main/pet_delete.html'
    form_class = DeletePetForm
    success_url = reverse_lazy('dashboard')
