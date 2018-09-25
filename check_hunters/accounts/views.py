from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from accounts.models import Account

class AccountListView(ListView):
    model = Account
    paginate_by = 100
    fields = ['name', 'addr', 'routing_num', 'account_num', 'render_edit_link']


class AccountUpdateView(UpdateView):
    model = Account
    success_url = reverse_lazy('accounts:list')
    fields = ['name', 'addr', 'routing_num', 'account_num']


class AccountCreateView(CreateView):
    model = Account
    success_url = reverse_lazy('accounts:list')
    fields = ['name', 'addr', 'routing_num', 'account_num']

