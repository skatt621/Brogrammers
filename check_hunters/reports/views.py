from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Account, Bank, Client
from checks.models import Check
from datetime import datetime

from .forms import FilterForm

@login_required
def general_report(request):
    return render(request, 'generalreports.html')

@login_required
def paid_check_data(request):
    checks = Check.objects.all()
    return_data = []

    paid_checks = {}
    paid_checks["Name"] = "Paid Checks"
    paid_checks["Count"] = 0

    unpaid_checks = {}
    unpaid_checks["Name"] = "Unpaid Checks"
    unpaid_checks["Count"] = 0

    for check in checks:
        if (check.paid_date == None):
            unpaid_checks["Count"] += 1
        else:
            paid_checks["Count"] += 1

    return_data.append(paid_checks)
    return_data.append(unpaid_checks)

    return JsonResponse(return_data, safe=False)


@login_required
def sent_letters_data(request):
    checks = Check.objects.all()

    letter_1_sent = 0
    letter_2_sent = 0
    letter_3_sent = 0
    letter_1_notsent = 0
    letter_2_notsent = 0
    letter_3_notsent = 0

    today = datetime.today().strftime('%Y-%m-%d')

    for check in checks:
        print(type(check.letter_1_send_date))
        if (str(check.letter_1_send_date) == today and check.letter_1_sent == 1):
            letter_1_sent += 1
        elif (str(check.letter_2_send_date) == today and check.letter_2_sent == 1):
            letter_2_sent += 1
        elif (str(check.letter_3_send_date) == today and check.letter_3_sent == 1):
            letter_3_sent += 1
        elif (str(check.letter_1_send_date) == today and check.letter_1_sent == 0):
            letter_1_notsent += 1
        elif (str(check.letter_2_send_date) == today and check.letter_2_sent == 0):
            letter_2_notsent += 1
        elif (str(check.letter_3_send_date) == today and check.letter_3_sent == 0):
            letter_3_notsent += 1
        else:
            continue

    return_data = [{"lettertype": "letter 1's sent", "letterssent": letter_1_sent},
     {"lettertype": "letter 2's sent", "letterssent": letter_2_sent},
     {"lettertype": "letter 3's sent", "letterssent": letter_3_sent},
     {"lettertype": "letter 1's not sent", "letterssent": letter_1_notsent},
     {"lettertype": "letter 2's not sent", "letterssent": letter_2_notsent},
     {"lettertype": "letter 3's not sent", "letterssent": letter_3_notsent}]
    return JsonResponse(return_data, safe=False)
