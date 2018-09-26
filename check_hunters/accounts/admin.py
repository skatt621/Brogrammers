from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['routing_num', 'account_num', 'name', 'addr']
    
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['routing_n', 'name']