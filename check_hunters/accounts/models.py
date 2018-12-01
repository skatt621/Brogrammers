import django_filters
import re
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from address.models import AddressField
import datetime

import logging

logger = logging.getLogger(__name__)

def validate_positive(num):
    if not num >= 0:
        raise ValidationError(f"value can't be negative ({num})")

def validate_num(num_str):
    if not num_str.isdigit():
        raise ValidationError(f"value must be a number ({num_str})")


LETTER_TEMPLATE = """
{date}

Dear {recipient_name}:

Check {check_num} you wrote for ${check_amt}, dated {made_date}, which was made payable to {to_client} was returned by your bank, {bank_name}.
Unless full payment of the check is received by cash within {wait_period} days after the date this demand letter was mailed, together with ${late_fee} in bank fees, we will file a small claims court claim against you.
You may wish to contact a lawyer to discuss your legal rights and responsibilities.
Sincerely,
Check Hunters
"""

VALID_TAGS = [
    'template',
    'recipient_name',
    'st_addr',
    'city',
    'state',
    'zip',
    'date',
    'to_client',
    'check_num',
    'made_date',
    'bank_name',
    'check_amt',
    'late_fee',
    'wait_period'
]

REGEX = re.compile(r'[^{]*{([^}]*)}')

def validate_template(template_str):
    keys = REGEX.findall(template_str)
    for key in keys:
        if key not in VALID_TAGS:
            raise ValidationError(f"Template tag '{key}' not a valid tag. Options are {VALID_TAGS}")

class Client(models.Model):
    """
    Client model. this makes the client table and represents a Client company using the Check Hunter Services
    Client model allows companies to configure their wait_period and late fee
    """
    name = models.CharField(max_length=200)
    wait_period = models.DurationField(blank=True, default=datetime.timedelta(days=10))
    late_fee = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=25)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    letter_1_template = models.CharField(max_length=5000, blank=True, default=LETTER_TEMPLATE, validators=[validate_template])
    letter_2_template = models.CharField(max_length=5000, blank=True, default=LETTER_TEMPLATE, validators=[validate_template])
    letter_3_template = models.CharField(max_length=5000, blank=True, default=LETTER_TEMPLATE, validators=[validate_template])

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        infoString = "{} Database Updated Client {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.name)
        logger.info(infoString)
        super(Client, self).save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        infoString = "{} Database Updated Bank".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.name)
        logger.info(infoString)
        super(Bank, self).save(*args, **kwargs)


class StringToFK(models.ForeignKey):
    # def to_python(self, value):
    #     bank = Bank.objects.get_or_create(routing_num=value)
    #     return bank

    # def validate(self, value):
    #     validate_num(value)
    #     return True

    pass


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

    def save(self, *args, **kwargs):
        infoString = "{} Database Updated Account {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.account_num)
        logger.info(infoString)
        super(Account, self).save(*args, **kwargs)
