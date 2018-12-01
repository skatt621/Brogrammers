# accounts/forms.py
from django.forms import ModelForm, widgets, Form, CharField
from django.urls import reverse
from django.utils.safestring import mark_safe
from searchableselect.widgets import SearchableSelect

from accounts.models import Account
from core import settings
from checks.forms import RelatedFieldWidgetCanAdd

from .models import Account, Bank
class AccountCreateForm(ModelForm):
    """overriding create form to have option to create a new account"""
    class Meta:
        model = Account
        fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2', 'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num']
        widgets = {
            'routing_num': RelatedFieldWidgetCanAdd(Bank, related_url="accounts:bank_create"),
        }
