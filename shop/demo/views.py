from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
