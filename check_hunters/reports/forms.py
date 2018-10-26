from django import forms

class FilterForm(forms.Form):
    bank_name = forms.CharField(label='Bank Name', max_length=100)
    account_type = forms.CharField(label='Account Type', max_length=100)
    letter_num = forms.CharField(label='Letter Number', max_length=100)
    amount = forms.CharField(label='Amount', max_length=100)
