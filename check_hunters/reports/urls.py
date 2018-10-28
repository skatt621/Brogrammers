# reports urls

from django.urls import re_path
from . import views

app_name = 'reports'

# url patterns match in a procedural way, so put the most specific ones at the top
urlpatterns = [
    re_path(r'report_data$', views.report_data, name='report_data'),
    re_path(r'$', views.general_report, name='general_report'),
]
