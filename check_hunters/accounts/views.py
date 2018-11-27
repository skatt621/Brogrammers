from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django_filters.views import FilterView
from accounts.models import Account, Client
from accounts.filters import AccountFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.models import modelform_factory
from django.core.exceptions import PermissionDenied


class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)

class AccountListView(LoginRequiredMixin, ListView):
    """view for having a list of accounts"""
    model = Account
    # filterset_class = AccountFilter
    paginate_by = 100
    fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2',  'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num', 'render_edit_link']
    # template_name = "accounts/account_list.html"


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """view for updating an account's information"""
    model = Account
    success_url = reverse_lazy('accounts:update')
    fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2', 'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num']


class AccountCreateView(LoginRequiredMixin, CreateView):
    """view for creating an account"""
    model = Account
    success_url = reverse_lazy('accounts:list')
    fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2', 'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num']


def validate_company_employee(request, client_pk):
    # checks if user can view page. raises a permission error if not
    client = request.user.client
    if client and client.pk != client_pk:
        raise PermissionDenied()



class ClientUpdateView(LoginRequiredMixin, ModelFormWidgetMixin, UpdateView):
    """view where a client user can change a client company's configurations"""
    model = Client
    success_url = reverse_lazy('home')
    fields = ['name', 'wait_period', 'late_fee', 'address', 'phone_num', 'letter_1_template', 'letter_2_template', 'letter_3_template']
    widgets = {
        'letter_1_template': forms.Textarea(),
        'letter_2_template': forms.Textarea(),
        'letter_3_template': forms.Textarea(),
    }

    def get(self, request, *args, **kwargs):
        validate_company_employee(request, int(kwargs['pk']))
        return super(ClientUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        validate_company_employee(request, int(kwargs['pk']))
        return super(ClientUpdateView, self).post(request, *args, **kwargs)
