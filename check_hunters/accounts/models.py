from django.db import models
from django.urls import reverse
from address.models import AddressField
from datetime import timedelta
# from checks.models import validate_num, validate_positive


def validate_positive(num):
    return num >= 0

def validate_num(num_str):
    return num_str.isdigit()
    
LETTER_TEMPLATE = """
{recipient_name}
{st_addr}
{city}, {state} {zip}

{date}

Dear {recipient_name}:

Check {check_num} you wrote for ${check_amt}, dated {made_date}, which was made payable to {to_client} was returned by your bank, {bank_name}.
Unless full payment of the check is received by cash within {wait_period} days after the date this demand letter was mailed, together with ${late_fee} in bank fees, we will file a small claims court claim against you.
You may wish to contact a lawyer to discuss your legal rights and responsibilities.
Sincerely,
Check Hunters
"""

class Client(models.Model):
    """
    Client model. this makes the client table and represents a Client company using the Check Hunter Services
    Client model allows companies to configure their wait_period and late fee
    """
    name = models.CharField(max_length=200)
    wait_period = models.DurationField(blank=True, default=timedelta(days=10))
    late_fee = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=25)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    letter_1_template = models.CharField(max_length=5000, blank=True, default=LETTER_TEMPLATE)
    letter_2_template = models.CharField(max_length=5000, blank=True, default=LETTER_TEMPLATE)
    letter_3_template = models.CharField(max_length=5000, blank=True, default=LETTER_TEMPLATE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Bank(models.Model):
    """
    Bank model. this makes the bank table and represents the routing number of a checking account that owes a client company money.
    """
    routing_n = models.CharField(max_length=50, unique=True, validators=[validate_num])
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
    """
    Account model. this model represents a checking account of a bounced check and makes the Account table.
    """
    first_name1 = models.CharField(max_length=200)
    last_name1 = models.CharField(max_length=200, default='')
    first_name2 = models.CharField(max_length=200, blank=True, null=True)
    last_name2 = models.CharField(max_length=200, blank=True, null=True)
    
    street_addr = models.CharField(max_length=200, default='')
    city_addr = models.CharField(max_length=200, default='')
    state_addr = models.CharField(max_length=200, default='')
    zip_addr = models.CharField(max_length=200, default='')

    routing_num = models.ForeignKey(Bank, on_delete=models.SET(None), null=True)
    account_num = models.CharField(max_length=50, validators=[validate_num])
    phone_num = models.CharField(max_length=20, null=True)

    class Meta:
        unique_together = ('routing_num', 'account_num')    # can have accounts with matching bank numbers as long as the account number is diff and vice versa

    def __str__(self):
        base = ""
        if self.routing_num:
            base =  self.routing_num.routing_n
        return f"{base}:{self.account_num}"

    def __unicode__(self):
        base = ""
        if self.routing_num:
            base =  self.routing_num.routing_n
        return base + ':' + self.account_num

