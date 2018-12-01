import django_tables2 as tables
from django_tables2.utils import A
from .models import Account

class AccountsTable(tables.Table):
    class Meta:
        model = Account
        fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2',  'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num', 'render_edit_link']
        empty_text = "No Accounts"