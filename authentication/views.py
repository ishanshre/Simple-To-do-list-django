from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

class UserRegister(CreateView):
    form_class = SignUpForm
    #fields = ['first_name','last_name','username','email','password']
    template_name = 'authentication/sign_up.html'
    success_url = reverse_lazy('todoapp:tasklist')
    