from django.test import TestCase
from letters.models import Letter
from django.test import Client as VisitorClient
import unittest
from accounts.models import Client
from accounts.models import Bank
from accounts.models import Account
from checks.models import Check

class exc:
    @staticmethod
    def zde_pass():
        return 10*(10/0)
        
    @staticmethod    
    def zde_fail():
        return 10*10

class TestLetters(unittest.TestCase):

    def test_valid_Letter_allattrib(self):
        try:
            cl = Client.objects.create(name="Sandeep's Store", 
            late_fee=100.00, 
            address="123 Address")

            b = Bank.objects.create(routing_n="010000000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy",
            first_name2 = "Charles",
            last_name1 = "Harding",
            last_name2 = "Martinet",
            street_addr = "123 Somewhere St.",
            city_addr = "Middle of",
            state_addr = "Nowhere",
            zip_addr = "123000",
            routing_num = b,
            account_num = "0",
            phone_num = "(864) 123-4567")

            c = Check.objects.create(
            to_client = cl,
            from_account = a,
            amount = 300.00,
            made_date = '2010-10-25',
            check_num = 123,

            created_date = '2011-01-25',

            amount_paid = 300.00,
            paid_date = '2011-02-16',

            letter_1_send_date = '2011-02-01',
            letter_2_send_date = '2011-02-15',
            letter_3_send_date = '2011-02-21')

            l = Letter.object.create(
            sent_date='2018-05-18',
            letter_template='letter1',
            check_obj=c)

            self.assertRaises(ZeroDivisionError, exc.zde_pass)
        except:
            self.assertRaises(ZeroDivisionError, exc.zde_fail)