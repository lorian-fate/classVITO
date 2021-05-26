from django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import MyUser


class User_PerfilesForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
            'name',
            'email',
            'password',
        ]