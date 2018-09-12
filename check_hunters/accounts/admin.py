from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['routing_num', 'account_num', 'name', 'addr']

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['from_account', 'check_num', 'paid', 'to_client', 'made_date']
