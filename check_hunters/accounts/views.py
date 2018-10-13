from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from accounts.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountListView(LoginRequiredMixin, ListView):
    # redirect_field_name = 'accounts: list'
    model = Account
    paginate_by = 100
    fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2',  'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num', 'addr', 'render_edit_link']


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    # redirect_field_name = 'accounts:update'
    model = Account
    success_url = reverse_lazy('accounts:update')
    fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2', 'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num', 'addr']


class AccountCreateView(LoginRequiredMixin, CreateView):
    # redirect_field_name = 'accounts:create'
    model = Account
    success_url = reverse_lazy('accounts:list')
    fields = ['first_name1', 'first_name2', 'last_name1', 'last_name2', 'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'routing_num', 'account_num', 'phone_num', 'addr']

