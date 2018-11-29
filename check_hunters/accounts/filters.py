from django_filters import FilterSet, CharFilter
from.models import Account

class AccountFilter(FilterSet):
    """class to filter accounts"""
    primary_first_name = CharFilter(label='Primary First Name', field_name='first_name1__icontains')
    primary_last_name = CharFilter(label='Primary Last Name', field_name='flast_name1__icontains')
    secondary_first_name = CharFilter(label='Secondary First Name', field_name='first_name2__icontains')
    secondary_last_name = CharFilter(label='Secondary Last Name', field_name='last_name2__icontains')
    
    class Meta:
        model = Account
        fields = [ 
            'routing_num', 'account_num', 'phone_num'
            ]
