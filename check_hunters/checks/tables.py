import django_tables2 as tables
from django_tables2.utils import A
from .models import Check

class ChecksTable(tables.Table):
    check_num = tables.LinkColumn('checks:update', args=[A('pk')])
    paid = tables.BooleanColumn()
    class Meta:
        model = Check
        fields = ('check_num', 'from_account', 'to_client', 'amount', 'made_date', 'paid')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "No Checks matching the search criteria"