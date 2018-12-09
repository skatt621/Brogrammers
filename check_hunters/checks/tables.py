import django_tables2 as tables
from django_tables2.utils import A
from .models import Check

class ChecksTable(tables.Table):
    check_num = tables.LinkColumn('checks:update', args=[A('pk')])
    paid = tables.BooleanColumn()
    current_fee = tables.TemplateColumn("{{ record.current_fee }}")
    total = tables.TemplateColumn("{{ record.total }}")
    letters_sent = tables.TemplateColumn("{{ record.sent_letters_count }}")

    class Meta:
        model = Check
        fields = ('check_num', 'from_account', 'to_client', 'amount', 'current_fee', 'total', 'made_date', 'paid', 'letters_sent', 'outstanding')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "No Checks matching the search criteria"
