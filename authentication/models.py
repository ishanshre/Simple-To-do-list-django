from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class User(AbstractUser):
    profile_photo = models.ImageField()
    phone_number = models.IntegerField(validators=[MinValueValidator(9000000000),MaxValueValidator(9999999999)], null=True, blank=True)
    

