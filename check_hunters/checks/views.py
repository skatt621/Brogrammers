from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormView
from django_tables2 import RequestConfig
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse

from .tables import ChecksTable
from .models import Check, CheckFilter
from .forms import CheckCreateForm, CheckMarkPaidForm, PrintLettersForm
from .utils import *

# check views


class CheckListView(SingleTableMixin, FilterView, LoginRequiredMixin, ListView):
    # redirect_field_name = 'checks:list'
    table_class = ChecksTable
    filterset_class = CheckFilter
    model = Check
    paginate_by = 100
    fields = ['to_client', 'from_account', 'amount', 'made_date', 'check_num', 'paid']


class CheckUpdateView(LoginRequiredMixin, UpdateView):
    # redirect_field_name = 'checks:update'
    model = Check
    form_class = CheckMarkPaidForm
    template_name = "checks/mark_paid.html"
    success_url = reverse_lazy('checks:list')


class CheckCreateView(LoginRequiredMixin, CreateView):
    # redirect_field_name = 'checks:create'
    model = Check
    success_url = reverse_lazy('checks:list')
    form_class = CheckCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PrintLettersView(LoginRequiredMixin, FormView):
    template_name = "checks/print_letters.html"
    form_class = PrintLettersForm
    success_url = reverse_lazy('checks:print_letters')

    def post(self, request, *args, **kwargs):
        letters_data = GetLettersData(request.user)
        letter_count = len(letters_data['first_letters']) + len(letters_data['second_letters']) + len(letters_data['third_letters'])
        messages.success(request, 'Would have printed ' + str(letter_count) + ' letters')
        
        success_printing_letters = PopulateTemplate(letters_data)
        form = self.form_class(request.POST)
        form.is_valid()
        if not success_printing_letters:
            form.errors['printing'] = "failed to print letters"
        return super(PrintLettersView, self).post(request, *args, **kwargs)
