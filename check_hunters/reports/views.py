from django.shortcuts import render
from django.http import JsonResponse

from .forms import FilterForm

# Create your views here.
def general_report(request):

    form  = FilterForm()
    return render(request, 'generalreports.html', {'form': form})

def report_data(request):
    print(request)
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
