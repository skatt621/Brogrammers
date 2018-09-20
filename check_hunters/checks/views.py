from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime

from .models import Check
from .forms import CheckCreateForm, CheckMarkPaidForm

# check views

class CheckListView(ListView):
    model = Check
    paginate_by = 100
    fields = ['to_client', 'from_account', 'amount', 'made_date', 'check_num', 'paid']


class CheckUpdateView(UpdateView):
    model = Check
    form = CheckMarkPaidForm
    success_url = reverse_lazy('checks:list')
    fields = ['to_client', 'from_account', 'amount', 'made_date', 'check_num', 'paid']

class CheckCreateView(CreateView):
    model = Check
    success_url = reverse_lazy('checks:list')
    fields = ['to_client', 'from_account', 'amount', 'made_date', 'check_num', 'paid']
    form = CheckCreateForm

    # def get_form_kwargs(self, *args, **kwargs):
    #     form_kwargs = super(CheckCreateView, self).get_form_kwargs(*args, **kwargs)
    #     form_kwargs['created_by'] = self.request.user
    #     return form_kwargs
        
    def get_context_data(self, **kwargs):
        context = super(CheckCreateView, self).get_context_data(**kwargs)
        context['form'] = self.form(self.request)
        # This sets the initial value for the field:
        # print("fields: " + context['form'].fields.keys())
        # context['form'].fields['created_by'].initial = self.request.user 
        context['form'].fields['created_by'].initial = self.request.user.id     
        return context

