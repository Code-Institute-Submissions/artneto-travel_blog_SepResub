from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from world.models import Profile

#Function to edit Profile page

class EditPageProfile(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_page_profile.html'
    success_url = reverse_lazy('index')
    fields = ['bio', 'profile_picture', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']
    

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile_user.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        user_page = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["user_page"] = user_page
        return context

#Function to change Password
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_changed')

def password_changed(request):
    return render(request, 'registration/password_changed.html', {})


#Create the Registration form using to sign up
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

#Edit/update Profile Page
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

#function to display user who is updating his details. 
    def get_object(self):
        return self.request.user