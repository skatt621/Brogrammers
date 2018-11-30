# account urls

from django.urls import re_path
from .views import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'routing_num/add$', BankCreateView.as_view(), name='bank_create'),
    re_path(r'update/(?P<pk>\d+)/$', AccountUpdateView.as_view(), name='update'),
    re_path(r'add$', AccountCreateView.as_view(), name='create'),
    re_path(r'$', AccountListView.as_view(), name='list'),
]
