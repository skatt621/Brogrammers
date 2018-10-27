from django.conf import settings
from django.db import models
from django.urls import reverse
from address.models import AddressField
from datetime import timedelta

class Client(models.Model):
    name = models.CharField(max_length=200)
    wait_period = models.DurationField(blank=True, default=timedelta(days=10))
    late_fee = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=25)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Bank(models.Model):
    routing_n = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=500, default="bank")
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    contact_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.routing_n

    def __unicode__(self):
        return self.routing_n

    def make_name(self):
        return "bank" +  self.routing_n
        
    def routing_num_is_valid(self):
        """checks if routing_num is correct"""
        # TODO 
        return True


class Account(models.Model):
    first_name1 = models.CharField(max_length=200)
    last_name1 = models.CharField(max_length=200, default='')
    first_name2 = models.CharField(max_length=200, blank=True, null=True)
    last_name2 = models.CharField(max_length=200, blank=True, null=True)
    
    # addr = AddressField(on_delete=models.CASCADE) 
    street_addr = models.CharField(max_length=200, default='')
    city_addr = models.CharField(max_length=200, default='')
    state_addr = models.CharField(max_length=200, default='')
    zip_addr = models.CharField(max_length=200, default='')

    routing_num = models.ForeignKey(Bank, on_delete=models.SET(None), null=True)
    account_num = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20, null=True)
    
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
