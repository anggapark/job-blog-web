from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "fullname",
            "username",
            "email",
            "phone",
        )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
