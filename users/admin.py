from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Post, CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
  add_form=CustomUserCreationForm
  form=CustomUserChangeForm
  model=CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
