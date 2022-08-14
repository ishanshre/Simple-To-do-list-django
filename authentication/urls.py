from django.urls import path
from .views import UserRegister
app_name = 'authentication'
urlpatterns = [
    path('SignUp/', UserRegister.as_view(),name='signup'),
]