from django.db import models
from django.conf import settings
from accounts.models import Account, Client
from datetime import datetime
from django.core.exceptions import ValidationError

import logging

logger = logging.getLogger(__name__)

def validate_positive(num):
    if not num >= 0:
        raise ValidationError(f"value can't be negative ({num})")

def validate_num(num_str):
    if not num_str.isdigit():
        raise ValidationError(f"value must be a number ({num_str})")


class Check(models.Model):
    # info on check
    to_client = models.ForeignKey('accounts.Client', on_delete=models.CASCADE)
    from_account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, help_text="routing#:account#")
    amount = models.DecimalField(max_digits=18, decimal_places=2, validators=[validate_positive])
    made_date = models.DateField()
    check_num = models.PositiveIntegerField()

    # info about when check was entered into the system
    created_date = models.DateField(blank=True, auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)   #  TODO doesn't work

    # info about payment being made
    amount_paid = models.DecimalField(max_digits=18, decimal_places=2, default=0, validators=[validate_positive])
    paid_date = models.DateField(null=True, blank=True)

    # letter dates
    letter_1_send_date = models.DateField(null=True, blank=True)
    letter_2_send_date = models.DateField(null=True, blank=True)
    letter_3_send_date = models.DateField(null=True, blank=True)
    letter_1_sent = models.BooleanField(null=True, blank=True, default=False)
    letter_2_sent = models.BooleanField(null=True, blank=True, default=False)
    letter_3_sent = models.BooleanField(null=True, blank=True, default=False)

    def name(self):
        account = self.from_account
        name_str = f"{account.first_name1} {account.last_name1}"
        if account.last_name2 and account.first_name2:
            name_str += f" and {account.first_name2} {account.last_name2}"
        return name_str

    def current_fee(self):
        client_fee = self.to_client.late_fee
        if not self.letter_1_sent:
            return client_fee
        else:
            return 2 * client_fee

    def total(self):
        return self.amount + self.current_fee()

    def sent_letters_count(self):
        if self.letter_3_sent:
            return 3
        elif self.letter_2_sent:
            return 2
        elif self.letter_1_sent:
            return 1
        else:
            return 0

    def save(self, *args, **kwargs):
        """overriding save to set date values"""
        if not self.created_date:
            self.created_date = datetime.today()
        if not (self.letter_1_send_date and self.letter_2_send_date and self.letter_3_send_date):
            self.letter_1_send_date = self.created_date
            self.letter_2_send_date = self.created_date + self.to_client.wait_period
            self.letter_3_send_date = self.created_date + 2 * self.to_client.wait_period
        infoString = "{} Updating Check {} to {} from Account {}, Old Values: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.check_num, self.to_client, self.from_account, self.__dict__)
        logger.info(infoString)
        super(Check, self).save(*args, **kwargs)
        infoString = "{} Updated Check {} to {} from Account {}, New Values: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.check_num, self.to_client, self.from_account, self.__dict__)
        logger.info(infoString)

    def __str__(self):
        return str(self.from_account) + '\t' + str(self.check_num)

    def __unicode__(self):
        return str(self.from_account) + '\t' + str(self.check_num)

    def paid(self):
        return self.paid_date != None

    def outstanding(self):
        if self.letter_3_sent == 1:
            return "yes"
        else:
            return "no"
