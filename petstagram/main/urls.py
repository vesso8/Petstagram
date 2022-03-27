
from django.urls import path

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.main.views.photos import like_pet_photo, CreatePetPhotoView, EditPetPhotoView, delete_photo, \
    PetPhotoDetailsView

'''
Home Page: http://127.0.0.1:8000/ 
Dashboard Page: http://127.0.0.1:8000/dashboard/ 
Profile Page: http://127.0.0.1:8000/profile/ 
Photo Details Page: http://127.0.0.1:8000/photo/details/photo_id/
'''



urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # path('profile/create/', create_profile, name='create profile'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo , name= 'like pet photo'),
    path('photo/add', CreatePetPhotoView.as_view(), name= 'create photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name= 'edit photo'),
    path('photo/delete/<int:pk>/', delete_photo, name = 'delete photo'),


    path('pet/add/', CreatePetView.as_view(), name= 'create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name= 'edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

)