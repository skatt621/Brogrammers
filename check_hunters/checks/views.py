from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormView
from django_tables2 import RequestConfig
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.template import Template, Context
import subprocess
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from checks.management.commands.populate_db import Command
from django.template import Template, Context


from accounts.models import *
from .tables import ChecksTable
from .models import Check
from .filters import CheckFilter
from .forms import CheckCreateForm, CheckMarkPaidForm, PrintLettersForm
from .utils import *
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

# CHECK VIEWS
class CheckListView(SingleTableMixin, FilterView, LoginRequiredMixin, ListView):
    table_class = ChecksTable
    filterset_class = CheckFilter
    model = Check
    paginate_by = 100
    fields = ['to_client', 'from_account', 'amount', 'current_fee', 'total', 'made_date', 'check_num', 'paid', 'outstanding']


    def get_filterset_kwargs(self, filterset_class):
        kwargs = super(CheckListView, self).get_filterset_kwargs(filterset_class)
        if kwargs["data"] is None:
            kwargs["data"] = {
                'not_paid': '1'
            }
        
        return kwargs

class CheckUpdateView(LoginRequiredMixin, UpdateView):
    model = Check
    form_class = CheckMarkPaidForm
    template_name = "checks/mark_paid.html"
    success_url = reverse_lazy('checks:list')

    def form_valid(self, form):
        infoString = "{} {} Updated Marked Check {} to {} from Account {} Paid".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.request.user, self.object.check_num, self.object.to_client, self.object.from_account)
        logger.info(infoString)
        """override form_valid to associate it with the current user that created it"""
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CheckCreateView(LoginRequiredMixin, CreateView):
    model = Check
    success_url = reverse_lazy('checks:list')
    form_class = CheckCreateForm

    def form_valid(self, form):
        infoString = "{} {} Created Check {} to {} from Account {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.request.user, form.cleaned_data['check_num'], form.cleaned_data['to_client'], form.cleaned_data['from_account'])
        logger.info(infoString)
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
        letter_1_count = len(letters_data['first_letters'])
        letter_2_count = len(letters_data['second_letters'])
        letter_3_count = len(letters_data['third_letters'])
        letter_count = letter_1_count + letter_2_count + letter_3_count

        if letter_count != 0:
            messages.success(request, f"Printing {letter_1_count} 1st letters, {letter_2_count} 2nd letters, & {letter_3_count} 3rd letters")
            # make and print the letters
            success_printing_letters, response = PopulateTemplate(letters_data)

            # indicate if they were successfully printed or not
            form = self.form_class(request.POST)
            form.is_valid()
            if not success_printing_letters:
                form.errors['printing'] = "failed to print letters"
                infoString = "{} {} Encountered Errors Printing Letters".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.request.user)
                logger.info(infoString)
            else:
                infoString = "{} {} Printed {} Letter 1's, {} Letter 2's, and {} Letter 3's".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.request.user, letter_1_count, letter_2_count, letter_3_count)
                logger.info(infoString)
            # return super(PrintLettersView, self).post(request, *args, **kwargs)
            return response
        else:
            infoString = "{} {} Attempted to Print, but All Letters were Already Printed".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.request.user)
            logger.info(infoString)
            messages.success(request, "There are no letters that need to be printed today.")
            return super(PrintLettersView, self).post(request, *args, **kwargs)

# TESTING UTILS VIEWS

def reset_database(request):
    """
    function view that deletes all clients & accounts
    and runs the populate_db script to restore the db to test state
    """
    Client.objects.all().delete()
    Account.objects.all().delete()

    # resultdbr = subprocess.run(['python', 'manage.py', 'populate_db'], stdout=subprocess.PIPE)
    # stringdbr = ''.join(resultdbr.stdout.decode('utf-8'))

    ##
    Command().handle()
    ##

    page = f""""
    {{% extends "base.html" %}}
    {{% load static %}}
    {{% block stylesheets %}}
    <link rel="stylesheet" href="{{% static 'css/home.css' %}}"/>
    {{% endblock %}}
    {{% block content %}}
    <u1>
    <li>Database reset successfully</li>
    </u1>
    {{% endblock content %}}
    """
    t = Template(page)
    html = t.render(Context())
    return HttpResponse(html)

def current_datetime(request):

    # resultacc = subprocess.run(['python', 'manage.py', 'test', 'accounts'], stderr=subprocess.PIPE)
    # stringacc = ''.join(resultacc.stderr.decode('utf-8'))
    ##
    resultacc = subprocess.run(['python', 'check_hunters\manage.py', 'test', 'accounts'], stderr=subprocess.PIPE)
    stringacc = ''.join(resultacc.stderr.decode('utf-8'))
    ##
    index = stringacc.find("Ran")
    stringacc = stringacc[index:]

    # resultchck = subprocess.run(['python', 'manage.py', 'test', 'checks'], stderr=subprocess.PIPE)
    # stringchck = ''.join(resultchck.stderr.decode('utf-8'))
    ##
    resultchck = subprocess.run(['python', 'check_hunters\manage.py', 'test', 'checks'], stderr=subprocess.PIPE)
    stringchck = ''.join(resultchck.stderr.decode('utf-8'))
    ##
    index = stringchck.find("Ran")
    stringchck = stringchck[index:]

    page = f""""
    {{% extends "base.html" %}}
    {{% load static %}}
    {{% block stylesheets %}}
    <link rel="stylesheet" href="{{% static 'css/home.css' %}}"/>
    {{% endblock %}}
    {{% block content %}}
    <h1>Unit Test Summaries</h1>
    <ul>
    <li>Client, Account, and Bank Tests: </br> {stringacc.replace('.', '').replace('-', '')}</li>
    <li>Check Tests: </br> {stringchck.replace('.', '').replace('-', '')}</li>
    </ul>
    {{% endblock content %}}
    """
    t = Template(page)
    html = t.render(Context())
    return HttpResponse(html)
