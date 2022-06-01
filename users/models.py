from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    fullname = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
