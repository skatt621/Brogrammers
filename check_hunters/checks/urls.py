# check urls

from django.urls import re_path
from .views import *

app_name = 'checks'

urlpatterns = [
    re_path(r'update/(?P<pk>\d+)/$', CheckUpdateView.as_view(), name='update'),
    re_path(r'add$', CheckCreateView.as_view(), name='create'),
    re_path(r'print_letters$', PrintLettersView.as_view(), name='print_letters'),
    re_path(r'$', CheckListView.as_view(), name='list'),
]