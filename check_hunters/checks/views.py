from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import RequestConfig
from django.urls import reverse_lazy
from datetime import datetime

from .tables import ChecksTable
from .models import Check
from .forms import CheckCreateForm, CheckMarkPaidForm

# check views

class CheckListView(ListView):
    model = Check
    paginate_by = 100
    fields = ['to_client', 'from_account', 'amount', 'made_date', 'check_num', 'paid']


    def get_context_data(self, *args, **kwargs):
        context = super(CheckListView, self).get_context_data(*args, **kwargs)
        table = ChecksTable(Check.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class CheckUpdateView(UpdateView):
    model = Check
    form_class = CheckMarkPaidForm
    template_name = "checks/mark_paid.html"
    success_url = reverse_lazy('checks:list')


class CheckCreateView(CreateView):
    model = Check
    success_url = reverse_lazy('checks:list')
    form_class = CheckCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
