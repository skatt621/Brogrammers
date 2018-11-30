from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Account, Bank, Client
from checks.models import Check
import logging

logger = logging.getLogger(__name__)

from .forms import FilterForm

@login_required
def general_report(request):

    form  = FilterForm()
    return render(request, 'generalreports.html', {'form': form})

@login_required
def report_data(request):
    accounts = Account.objects.all()
    checks = Check.objects.all()
    return_data = []
    for account in accounts:
        new_account = {}
        new_account["Name"] = account.first_name1 + " " + account.last_name1
        new_account["id"] = account.id
        new_account["Count"] = 0
        return_data.append(new_account)

    for check in checks:
        for item in return_data:
            if item["id"] == int(check.from_account_id):
                item["Count"] += 1

    return JsonResponse(return_data, safe=False)
