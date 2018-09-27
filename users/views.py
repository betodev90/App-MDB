from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from .forms import CustomUserCreateForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'