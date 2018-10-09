from django.conf import settings
from django.db import models
from django.urls import reverse
from address.models import AddressField

class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Bank(models.Model):
    routing_n = models.CharField(max_length=50, unique=True)
    # contact_name
    # contact_phone_num

    def __str__(self):
        return self.routing_n

    def __unicode__(self):
        return self.routing_n
    def name(self):
        return "bank" +  self.routing_n
    def routing_num_is_valid(self):
        """checks if routing_num is correct"""
        # TODO 
        return True


class Account(models.Model):
    name = models.CharField(max_length=200)
    addr = AddressField(on_delete=models.CASCADE) 
    routing_num = models.ForeignKey(Bank, on_delete=models.SET(None), null=True)
    account_num = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ('routing_num', 'account_num')

    def __str__(self):
        base = ""
        if self.routing_num:
            base =  self.routing_num.routing_n
        return base + ':' + self.account_num

    def __unicode__(self):
        base = ""
        if self.routing_num:
            base =  self.routing_num.routing_n
        return base + ':' + self.account_num

def validate_positive(num):
    return num >= 0
