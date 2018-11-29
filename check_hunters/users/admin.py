# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
"""import logging

logger = logging.getLogger(__name__)

logs = LogEntry.objects.all()
for l in logs:
    logOutput = "{} {} {}".format(str(l.action_time), str(l.user), str(l))
    logger.info(logOutput)
"""

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'client']

admin.site.register(User, CustomUserAdmin)
