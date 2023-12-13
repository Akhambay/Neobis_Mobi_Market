from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "DOB",
        "profile_image",
    ]
    fieldsets = UserAdmin.fieldsets + \
        ((None, {"fields": ("DOB", "profile_image")}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ("DOB", "profile_image")}),)


admin.site.register(CustomUser, CustomUserAdmin)
