from django_filters import FilterSet, DateFilter, CharFilter, ChoiceFilter, BooleanFilter
from django.forms import SelectDateWidget
from .models import Check

PAID_CHOICES = {
    ('3', 'No'),
    ('2', 'Yes'),
    ('1', 'Any'),
}


class CheckFilter(FilterSet):
    """class to filter checks for reports / list views"""
    from_account__first_name1 = CharFilter(label="Primary First Name", lookup_expr='icontains')
    from_account__last_name1 = CharFilter(label="Primary Last Name", lookup_expr='icontains')
    from_account__first_name2 = CharFilter(label="Secondary First Name", lookup_expr='icontains')
    from_account__last_name2 = CharFilter(label="Secondary Last Name", lookup_expr='icontains')
    paid = ChoiceFilter(choices=PAID_CHOICES, label='Paid', field_name="paid_date", lookup_expr='isnull')
    made_date_start = DateFilter(label='Written After', field_name='made_date', lookup_expr='gte', widget=SelectDateWidget)
    made_date_end = DateFilter(label='Written Before', field_name='made_date', lookup_expr='lte', widget=SelectDateWidget)
    
    paid_date_start = DateFilter(label='Paid After',field_name='paid_date', lookup_expr='gte', widget=SelectDateWidget)
    paid_date_end = DateFilter(label='Paid Before', field_name='paid_date', lookup_expr='lte', widget=SelectDateWidget)
    

    from_account__phone_num = CharFilter(label="Phone #")
    check_num = CharFilter(label="Check #")
    
    class Meta:
        model = Check
        fields = [
            'from_account__first_name1', 'from_account__last_name1', 'from_account__first_name2', 'from_account__last_name2', 
            'from_account__phone_num', 'check_num', 'to_client','paid','paid_date_start', 'paid_date_end', 'made_date_start', 'made_date_end', 'letter_1_sent', 'letter_2_sent', 'letter_3_sent'

        ]
