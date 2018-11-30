# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

from django.utils.translation import gettext, gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'client']
    
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password', 'client')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(User, CustomUserAdmin)
