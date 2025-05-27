from django.contrib import admin

# Register your models here.



# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Fields", {"fields": ("profile_picture_url",)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
