from django.db import models
from django.conf import settings
from django import forms
import django_filters
from accounts.models import Account, Client
from django.forms import SelectDateWidget
from datetime import datetime

def validate_positive(num):
    return num >= 0


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
    # paid = models.BooleanField(default=False)
    amount_paid = models.DecimalField(max_digits=18, decimal_places=2, default=0, validators=[validate_positive])
    paid_date = models.DateField(null=True, blank=True)

    # letter dates
    letter_1_send_date = models.DateField(null=True, blank=True)
    letter_2_send_date = models.DateField(null=True, blank=True)
    letter_3_send_date = models.DateField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = datetime.today()
        if not (self.letter_1_send_date and self.letter_2_send_date and self.letter_3_send_date):
            self.letter_1_send_date = self.created_date + self.to_client.wait_period
            self.letter_2_send_date = self.created_date + 2 * self.to_client.wait_period
            self.letter_3_send_date = self.created_date + 3 * self.to_client.wait_period
        super(Check, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.from_account) + '\t' + str(self.check_num)

    def __unicode__(self):
        return str(self.from_account) + '\t' + str(self.check_num)

    def paid(self):
        return self.paid_date != None


class CheckFilter(django_filters.FilterSet):
    """class to filter checks for reports"""
    made_date_start = django_filters.DateFilter(label='Made Out Start Date', field_name='made_date', lookup_expr='gte', widget=SelectDateWidget)
    made_date_end = django_filters.DateFilter(label='Made Out End Date', field_name='made_date', lookup_expr='lte', widget=SelectDateWidget)
    
    paid_date_start = django_filters.DateFilter(label='Paid Start Date',field_name='paid_date', lookup_expr='gte', widget=SelectDateWidget)
    paid_date_end = django_filters.DateFilter(label='Paid End Date', field_name='paid_date', lookup_expr='lte', widget=SelectDateWidget)

    class Meta:
        model = Check
        fields = []