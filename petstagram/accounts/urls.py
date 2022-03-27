from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView, ChangeUserPasswordView, \
    EditProfileView, DeleteProfileView

urlpatterns = (
    path('accounts/login/', UserLoginView.as_view(), name='login user'),
    path('accounts/profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('accounts/create-profile/', UserRegisterView.as_view(), name= 'create profile'),
    path('accounts/edit-password/<int:pk>/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/' , RedirectView.as_view(url = reverse_lazy('dashboard')), name='password_change_done'),
    path('accounts/edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('accounts/delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
)
