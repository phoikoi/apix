from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ApixUserCreationForm, ApixUserChangeForm
from .models import ApixUser

class ApixUserAdmin(UserAdmin):
    model = ApixUser
    add_form = ApixUserCreationForm
    form = ApixUserChangeForm

admin.site.register(ApixUser, ApixUserAdmin)

