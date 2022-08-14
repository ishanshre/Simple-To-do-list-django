from django.urls import path
from .views import UserRegister, UserLoginView
from django.contrib.auth.views import LogoutView
app_name = 'authentication'
urlpatterns = [
    path('SignUp/', UserRegister.as_view(),name='signup'),
    path('Login/',UserLoginView.as_view(),name='login'),
    path('Logout', LogoutView.as_view(next_page='authentication:login'),name='logout'),
]