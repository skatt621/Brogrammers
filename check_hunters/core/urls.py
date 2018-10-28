"""check_hunters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import re_path, include, path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import datetime
from django.core.management import execute_from_command_line
import subprocess

def current_datetime(request):
    from django.template import Template, Context

    resultacc = subprocess.run(['python', 'manage.py', 'test', 'accounts'], stderr=subprocess.PIPE)
    stringacc = ''.join(resultacc.stderr.decode('utf-8'))
    resultchck = subprocess.run(['python', 'manage.py', 'test', 'checks'], stderr=subprocess.PIPE)
    stringchck = ''.join(resultchck.stderr.decode('utf-8'))

    # bigstringacc = "Client, Account, and Bank tests:" + stringacc
    # bigstringchck = "Check tests:\n" + stringchck
    # bigstringlett = "Letter tests:\n" + stringlett
    # string = bigstringacc + bigstringchck + bigstringlett

    page = f""""
    {{% extends "base.html" %}}
    {{% load static %}}
    {{% block stylesheets %}}
    <link rel="stylesheet" href="{{% static 'css/home.css' %}}"/>
    {{% endblock %}}
    {{% block content %}}
    <h1>Unit Test Summaries</h1>
    <ul>
    <li>Client, Account, and Bank Tests: </br> {stringacc.replace('.', '').replace('-', '')}</li>
    <li>CheckTests: </br> {stringchck.replace('.', '').replace('-', '')}</li>
    </ul>
    {{% endblock content %}}
    """
    t = Template(page)
    html = t.render(Context())
    return HttpResponse(html)

    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # html1 = "<html><h1>%s</h1><br><br><br><br><br>" % bigstringacc
    # html2 = "<h1>%s</h1><br><br><br><br><br>" % bigstringchck
    # html3 = "<h1>%s</h1></html><br><br><br><br><br>" % bigstringlett
    # html = html1 + html2 + html3
    return HttpResponse(html)

urlpatterns = [
    re_path(r'^$', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    re_path(r'accounts/', include('django.contrib.auth.urls')),
    re_path(r'admin/', admin.site.urls),
    re_path(r'check_accounts/', include('accounts.urls')),
    re_path(r'checks/', include('checks.urls')),
    re_path(r'utests', current_datetime),
    re_path(r'reports/', include('reports.urls')),
    #re_path('^searchableselect/', include('searchableselect.urls')),
]
