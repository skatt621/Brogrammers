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
    model = Check
    success_url = reverse_lazy('checks:list')
    form_class = CheckCreateForm

    def form_valid(self, form):
        """override form_valid to associate it with the current user that created it"""
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PrintLettersView(LoginRequiredMixin, FormView):
    template_name = "checks/print_letters.html"
    form_class = PrintLettersForm
    success_url = reverse_lazy('checks:print_letters')

    def post(self, request, *args, **kwargs):
        # get all the data needed to make the letters
        letters_data = GetLettersData(request.user)
        # get summary data to give the user an idea of what output to exepect (and for debugging)
        letter_count = len(letters_data['first_letters']) + len(letters_data['second_letters']) + len(letters_data['third_letters'])
        messages.success(request, 'Would have printed ' + str(letter_count) + ' letters')
        
        if(letters_data != 0):
            # make and print the letters
            success_printing_letters, response = PopulateTemplate(letters_data)

            # indicate if they were successfully printed or not
            form = self.form_class(request.POST)
            form.is_valid()
            if not success_printing_letters:
                form.errors['printing'] = "failed to print letters"
            # return super(PrintLettersView, self).post(request, *args, **kwargs)
            return response
        else:
            return super(PrintLettersView, self).post(request, *args, **kwargs)