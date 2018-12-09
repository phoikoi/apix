from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ApixUser

class ApixUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ApixUser
        fields = ('username', 'email')

class ApixUserChangeForm(UserChangeForm):
    class Meta:
        model = ApixUser
        fields = UserChangeForm.Meta.fields

