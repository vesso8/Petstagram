from django.shortcuts import render, redirect
from django.views import generic as views

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import Pet_photo



class HomeView(RedirectToDashboard ,views.TemplateView):
    template_name = 'templates_main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = Pet_photo
    template_name = 'templates_main/dashboard.html'
    context_object_name = 'pet_photos'
