from django.shortcuts import render

# Create your views here.
def general_report(request):
    return render(request, 'generalreports.html', context)
