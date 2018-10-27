from django.core.management.base import BaseCommand
from accounts.models import Client, Account, Bank
from checks.models import Check
from letters.models import Letter
from datetime import timedelta, date
import time

class Command(BaseCommand):
    #TODO: fill these out for future reference
    args = ''
    help = ''

    client = None

    def _create_clients(self):
        client1 = Client(name='Sherlock Holmes', wait_period=timedelta(days=10), late_fee=50, address='221B Baker Street, London, UK', phone_num='call Watson instead')
        client1.save()
        client = client1

        client2 = Client(name='Freddy Krueger', wait_period=timedelta(days=10), late_fee=20, address='145 Elm Street, Austin, Texas, US', phone_num='919-555-9798')
        client2.save()

        client3 = Client(name='Schmidt and Jenko', wait_period=timedelta(days=10), late_fee=40, address='21 Jump Street, New York, New York, US', phone_num='214-555-2150')
        client3.save()

    def _create_accounts(self):
        account1 = Account(first_name1="Obi Wan", last_name1="Kenobi", street_addr="The High Ground", account_num="12345678", phone_num="it's a secret")
        account1.save()

        account2 = Account(first_name1="Sheev", last_name1="Palpatine", street_addr="100 Senate way", account_num="Order 66", phone_num="1-800-THE-SENATE")
        account2.save()

        # TODO: why can't we use name here?
    def _create_banks(self):
        bank1 = Bank(routing_n="9234024", address="1900 Main Ave, Raleigh, NC", phone_num="1-800-PNC-BANK", contact_name="Penn the Teller")
        bank1.save()

        bank2 = Bank(routing_n="0123912", address="200 Hickory Street, Nashville, TN", phone_num="877-CASH-NOW", contact_name="JG Wentworth-less")
        bank2.save()

    #def _create_checks(self):
        #check1 = Check(to_client=self.client,amount=100.00, made_date=date(date.today().year, date.today().month, 23), check_num=101, created_date=date.today())
        #check1.save()

        #check2 = Check(to_client=self.client, amount=205.00, made_date=date(date.today().year, date.today().month, 25), check_num=1005, created_date=date.today())
        # check2.save()
        #
        # check3 = Check(to_client=self.client, amount=100.00, made_date=date(date.today().year, 9, 26), check_num=92, created_date=date.today())
        # check3.save()

    # def _create_letters(self):
    #     letter1 = Letter(sent_date=date(date.today().year, date.today().month, 26), letter_template="1st")
    #     letter1.save()
    #
    #     letter2 = Letter(sent_date=date(date.today().year, date.today().month, 25), letter_template="2nd")
    #     letter2.save()
    #
    #     letter3 = Letter(sent_date=date(date.today().year, date.today().month, 18), letter_template="3rd")
    #     letter3.save()

    def handle(self, *args, **options):
        self._create_clients()
        self._create_accounts()
        self._create_banks()
        # self._create_letters()
        print("Database succesfully updated")
