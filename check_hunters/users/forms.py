# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'client')

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['client'] = forms.ChoiceField()

    class Meta:
        model = User
        # fields = (
        #     'username', 'first_name', 'last_name', 'email', 'is_staff',
        #     'is_active', ''
        #     )
        fields = '__all__'