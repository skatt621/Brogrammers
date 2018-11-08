from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Client

class User(AbstractUser):
    """User model. To be able to associate users with clients"""
    client = models.ForeignKey('accounts.Client', on_delete=models.SET_NULL, null=True, blank=True)
    

