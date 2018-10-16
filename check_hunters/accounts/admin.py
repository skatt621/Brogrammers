from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'wait_period', 'late_fee', 'address', 'phone_num']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['routing_num', 'account_num', 'first_name1', 'first_name2', 'last_name1', 'last_name2', 'street_addr', 'city_addr', 'state_addr', 'zip_addr', 'phone_num']
    
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['routing_n', 'name', 'address', 'phone_num', 'contact_name']