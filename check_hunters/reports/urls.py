# reports urls

from django.urls import re_path
from . import views

app_name = 'reports'
urlpatterns = [
    re_path(r'general/', views.general_report, name='general_report'),
]
