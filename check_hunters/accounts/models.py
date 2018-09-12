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


class Check(models.Model):
    # info on check
    to_client = models.ForeignKey('Client', on_delete=models.CASCADE)
    from_account = models.ForeignKey('Account', on_delete=models.CASCADE, help_text="routing#:account#")
    amount = models.DecimalField(max_digits=18, decimal_places=2, validators=[validate_positive])
    made_date = models.DateField()
    check_num = models.PositiveIntegerField()

    # info about when check was entered into the system
    created_date = models.DateField(blank=True, auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    # info about payment being made
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.from_account) + '\t' + str(self.check_num)

    def __unicode__(self):
        return str(self.from_account) + '\t' + str(self.check_num)