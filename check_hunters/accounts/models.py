from django.db import models
from django.urls import reverse
from address.models import AddressField

class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=200)
    addr = AddressField(on_delete=models.CASCADE) 
    routing_num = models.CharField(max_length=50)
    account_num = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ('routing_num', 'account_num')

    def __str__(self):
        return self.routing_num + ':' + self.account_num

    def __unicode__(self):
        return self.routing_num + ':' + self.account_num


def validate_positive(num):
    return num >= 0
