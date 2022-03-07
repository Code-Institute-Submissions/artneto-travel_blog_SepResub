from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView
from .import views

#This is the url for user authentication
urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_changed/', views.password_changed, name='password_changed'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='show_profile_page')
]