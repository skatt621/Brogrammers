from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry, ADDITION

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['from_account', 'check_num', 'paid', 'to_client', 'made_date']

    # TODO on create in admin add created_by user
    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)
