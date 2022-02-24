
from django.urls import path

from petstagram.main.views.generic import show_home, show_dashboard
from petstagram.main.views.pets import create_pet, edit_pet, delete_pet
from petstagram.main.views.photos import show_photo_details, like_pet_photo, create_photo, edit_photo, delete_photo
from petstagram.main.views.profiles import show_profile_details, create_profile, edit_profile, delete_profile

'''
Home Page: http://127.0.0.1:8000/ 
Dashboard Page: http://127.0.0.1:8000/dashboard/ 
Profile Page: http://127.0.0.1:8000/profile/ 
Photo Details Page: http://127.0.0.1:8000/photo/details/photo_id/
'''



urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile_details, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', show_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo , name= 'like pet photo'),
    path('photo/add', create_photo, name= 'create photo'),
    path('photo/edit/<int:pk>/', edit_photo, name= 'edit photo'),
    path('photo/delete/<int:pk>/', delete_photo, name = 'delete photo'),


    path('pet/add/', create_pet, name= 'create pet'),
    path('pet/edit/<int:pk>/', edit_pet, name= 'edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

)