from django.shortcuts import render, redirect
from .models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
#from django.contrib.auth import logout
from django.views import View
# Create your views here.

class UserRegister(SuccessMessageMixin,CreateView):
    form_class = SignUpForm
    #fields = ['first_name','last_name','username','email','password']
    template_name = 'authentication/sign_up.html'
    success_url = reverse_lazy('todoapp:tasklist')

    def get_success_message(self,cleaned_data):
        print(cleaned_data)
        return "Account Successfully Created"

class UserLoginView(SuccessMessageMixin,LoginView):
    template_name = 'authentication/login.html'

    def get_success_message(self,cleaned_data):
        print(cleaned_data)
        return "Logged In Success"
    
# class UserLogoutView(SuccessMessageMixin,View):
#     def get(self, request):
#         logout(request)
#         return redirect('todoapp:tasklist')
    
#     def get_success_message(self,cleaned_data):
#         print(cleaned_data)
#         return "Logout Success"