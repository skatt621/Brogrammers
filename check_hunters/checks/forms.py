# check forms

from django.forms import ModelForm, widgets, Form
from django.urls import reverse
from django.utils.safestring import mark_safe
from searchableselect.widgets import SearchableSelect

from accounts.models import Account
from .models import Check
from core import settings

class RelatedFieldWidgetCanAdd(widgets.Select):   # TODO SearchableSelect

    def __init__(self, related_model, related_url=None, *args, **kw):
        """overriding init to add create new FK object link"""
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        """overriding to add create new button"""
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        img = '<img src="{0}img/add_icon.png" class="icon" id="add_icon" width="10" height="10" alt="{1}"/></a>'.format(settings.STATIC_URL, "Add Another")
        link = '<a href="{0}" target="_blank" class="add-another" id="add_id_{1}" onclick="return showAddAnotherPopup(this);">'.format(self.related_url, name)
        output.append(link)
        output.append(img)                                                                                                                               
        return mark_safe(u''.join(output))


class CheckCreateForm(ModelForm):
    """Overriding create form to have option to create a new account directly"""
    class Meta:
        model = Check
        fields = ('to_client', 'from_account', 'amount', 'made_date', 'check_num')
        widgets = {
            'from_account': RelatedFieldWidgetCanAdd(Account, related_url="accounts:create"), # , search_field='name', model="accounts.Account"),
            'made_date':widgets.SelectDateWidget(),
        }


class CheckMarkPaidForm(ModelForm):
    """Overriding update form so only editable fields are amount and date paid"""
    class Meta:
        model = Check
        fields = ('amount_paid', 'paid_date')
        widgets = {
            'paid_date':widgets.SelectDateWidget(),
        }

        def is_valid(self):
            valid = super(CheckMarkPaidForm, self).is_valid()
            # we're done now if not valid
            if not valid:
                return valid
            # TODO if amountpaid != amount, make sure user is supervisor or admin
            return valid
        
class PrintLettersForm(Form):
    """form that starts batch print process when posted to"""
    pass