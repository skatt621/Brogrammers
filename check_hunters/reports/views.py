from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import FilterForm

@login_required
def general_report(request):

    form  = FilterForm()
    return render(request, 'generalreports.html', {'form': form})

@login_required
def report_data(request):

    data = [
      {
        "Name": "Bank A",
        "Count": .65
      },
      {
        "Name": "Bank B",
        "Count": .10
      },
      {
        "Name": "Bank C",
        "Count": .05
      },
      {
        "Name": "Bank D",
        "Count": .20
      }
    ]
    return JsonResponse(data, safe=False)
