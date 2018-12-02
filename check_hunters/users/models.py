from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from accounts.models import Client

import logging

logger = logging.getLogger(__name__)

class User(AbstractUser):
    """User model. To be able to associate users with clients"""
    client = models.ForeignKey('accounts.Client', on_delete=models.SET_NULL, null=True, blank=True)

    def can_access_admin(self):
        is_admin = self.groups.filter(name='Admin').exists()
        is_supervisor = self.groups.filter(name='Supervisor').exists()
        return is_admin or is_supervisor or self.is_superuser

    def save(self, *args, **kwargs):
        infoString = "{} Updating User Settings, Old Values".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.__dict__)
        logger.info(infoString)
        super(User, self).save(*args, **kwargs)
        infoString = "{} Updated User Settings, New Values".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.__dict__)
        logger.info(infoString)
