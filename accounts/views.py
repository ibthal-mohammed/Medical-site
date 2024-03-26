from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin 
)

from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import NewSignUp


class SignUpView(CreateView):
    form_class = NewSignUp
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'