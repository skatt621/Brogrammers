# check forms

from django.forms import ModelForm, widgets
from django import forms
from .models import Check


class CheckCreateForm(ModelForm):
    class Meta:
        model = Check
        fields = (
            'to_client', 
            'from_account', 
            'amount', 
            'made_date', 
            'check_num', 
            'created_by'
            )
        # widgets = {
        #     'create_by': forms.HiddenInput()
        # }
        

    def __init__(self, requests,  *args, **kwargs):
        super(CheckCreateForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].initial =requests.user
        self.fields['created_by'].widget.attrs['readonly'] = True
        

class CheckMarkPaidForm(ModelForm):
    class Meta:
        model = Check
        fields = (
            'to_client', 
            'from_account', 
            'amount', 
            'made_date', 
            'check_num', 
            'paid', 
            'paid_date'
            )
        
    def __init__(self, *args, **kwargs):
        super(CheckMarkPaidForm, self).__init__(*args, **kwargs)
        for field in ['to_client', 'from_account', 'amount', 'made_date', 'check_num']:
            self.fields[field].widget.attrs['readonly'] = True

    def is_valid(self):
        empty = self.paid_date in [None, ''] or self.paid in [None, '']
        valid = super(CheckMarkPaidForm, self).is_valid()
        return not empty and valid