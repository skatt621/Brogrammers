from django.db import models
from checks.models import Check

LETTER_TEMPLATES = [ # TODO set to template names
    ("letter1","1st"),
    ("letter2", "2nd"),
    ("letter3", "3rd"),
    ]

# Create your models here.
class Letter(models.Model):
    sent_date = models.DateField()
    letter_template = models.CharField(choices=LETTER_TEMPLATES, max_length=100)
    check_obj = models.ForeignKey(Check, on_delete=models.CASCADE)

def print_todays_checks():
    """preps & prints all letters that need to be sent out today"""
    # TODO
    pass
