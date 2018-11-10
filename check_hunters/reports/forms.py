from django import forms

class FilterForm(forms.Form):
    primary_field = forms.CharField(label='Primary Field', max_length=100)
    secondary_field = forms.CharField(label='Secondary Field', max_length=100)
    tertiary_field = forms.CharField(label='Tertiary Field', max_length=100)
