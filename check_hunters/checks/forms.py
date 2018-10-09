# check forms

from django import forms
from django.forms import ModelForm, widgets
from django.urls import reverse
from django.utils.safestring import mark_safe
from searchableselect.widgets import SearchableSelect

from accounts.models import Account
from .models import Check
from core import settings

class RelatedFieldWidgetCanAdd(widgets.Select):   # TODO SearchableSelect

    def __init__(self, related_model, related_url=None, *args, **kw):

        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        #self.render = kwargs.pop('render')
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        img = '<img src="{0}img/add_icon.png" class="icon" id="add_icon" width="10" height="10" alt="{1}"/></a>'.format(settings.STATIC_URL, "Add Another")
        link = '<a href="{0}" class="add-another" id="add_id_{1}" onclick="return showAddAnotherPopup(this);">'.format(self.related_url, name)
        output.append(link)
        output.append(img)                                                                                                                               
        return mark_safe(u''.join(output))


class CheckCreateForm(ModelForm):

    class Meta:
        model = Check
        fields = ('to_client', 'from_account', 'amount', 'made_date', 'check_num')
        widgets = {
            'from_account': RelatedFieldWidgetCanAdd(Account, related_url="accounts:create"), # , search_field='name', model="accounts.Account"),
            'made_date':forms.SelectDateWidget(),
        }


class CheckMarkPaidForm(ModelForm):
    class Meta:
        model = Check
        fields = ('paid_date',)
        widgets = {
            'paid_date':forms.SelectDateWidget(),
        }
        