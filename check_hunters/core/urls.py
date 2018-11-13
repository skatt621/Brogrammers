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
from accounts.views import ClientUpdateView
from checks.views import reset_database, current_datetime


urlpatterns = [
    re_path(r'^$', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    re_path(r'accounts/', include('django.contrib.auth.urls')),
    re_path(r'admin/', admin.site.urls),
    re_path(r'check_accounts/', include('accounts.urls')),
    re_path(r'checks/', include('checks.urls')),
    re_path(r'utests/', current_datetime),
    re_path(r'resetdb/', reset_database),
    re_path(r'reports/', include('reports.urls')),
    re_path(r'company_configurations/(?P<pk>\d+)/$', ClientUpdateView.as_view(), name='client_update'),
]
