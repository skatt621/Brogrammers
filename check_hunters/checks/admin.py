from django.contrib import admin
from .models import *

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['from_account', 'check_num', 'paid', 'to_client', 'made_date']

