# reports urls

from django.urls import re_path
from . import views

app_name = 'reports'

# url patterns match in a procedural way, so put the most specific ones at the top
urlpatterns = [
    re_path(r'paid_check_data$', views.paid_check_data, name='paid_check_data'),
    re_path(r'num_check_data$', views.num_checks_data, name='num_checks_data'),
    re_path(r'sent_letters_data$', views.sent_letters_data, name='sent_letters_data'),
    re_path(r'$', views.general_report, name='general_report'),
]
