import django_tables2 as tables
from django_tables2.utils import A
from .models import Check

class ChecksTable(tables.Table):
    paid = tables.LinkColumn('checks:update', args=[A('pk')])
    
    class Meta:
        model = Check
        fields = ('to_client', 'from_account', 'amount', 'made_date', 'check_num', 'paid')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "No Checks matching the search criteria"