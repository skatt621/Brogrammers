from django.test import Client as VisitorClient
from checks.models import Check
from accounts.models import Client
from accounts.models import Bank
from accounts.models import Account
import unittest
from address.models import AddressField
from datetime import timedelta
from datetime import datetime

class exc:
    @staticmethod
    def zde_pass():
        return 10*(10/0)
        
    @staticmethod    
    def zde_fail():
        return 10*10

class TestCheck(unittest.TestCase):
    def test_valid_Check_allatrib(self):
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
            account_num = "4321",
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

            self.assertTrue(True)
        except:
            self.assertTrue(False)
    
    def test_Check_edit(self):
        cl = Client.objects.create(name="Sandeep's Store", 
        late_fee=100.00, 
        address="123 Address")

        b = Bank.objects.create(routing_n="00006100",
        address = "someaddaress",
        phone_num = "123456789",
        contact_name = "big fun")

        cl2 = Client.objects.create(name="Pete's Store", 
        late_fee=100.00, 
        address="123 Address")

        b2 = Bank.objects.create(routing_n="00003600",
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
        account_num = "15",
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

        c.to_client = cl2
        c.check_num = 321
        c.amount_paid = 150.0

        retval = str(c)
        self.assertTrue(retval == "00006100:15\t321" and c.check_num == 321 and c.amount_paid == 150.0)


class TestCheck_methods(unittest.TestCase):
    def test_str(self):
        cl = Client.objects.create(name="Sandeep's Store", 
        late_fee=100.00, 
        address="123 Address")

        b = Bank.objects.create(routing_n="00006000",
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
        account_num = "12",
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

        retval = str(c)
        self.assertTrue(retval == "00006000:12\t123")

    # def test_str2(self):
    #     cl = Client.objects.create(name="Sandeep's Store", 
    #     late_fee=100.00, 
    #     address="123 Address")

    #     b = Bank.objects.create(routing_n="00006000",
    #     address = "someaddaress",
    #     phone_num = "123456789",
    #     contact_name = "big fun")

    #     a = Account.objects.create(first_name1 = "Andy",
    #     first_name2 = "Charles",
    #     last_name1 = "Harding",
    #     last_name2 = "Martinet",
    #     street_addr = "123 Somewhere St.",
    #     city_addr = "Middle of",
    #     state_addr = "Nowhere",
    #     zip_addr = "123000",
    #     routing_num = b,
    #     account_num = "12",
    #     phone_num = "(864) 123-4567")

    #     c = Check.objects.create(
    #     to_client = cl,
    #     from_account = a,
    #     amount = 300.00,
    #     made_date = '2010-10-25',
    #     check_num = 123,

    #     created_date = '2011-01-25',

    #     amount_paid = 300.00,
    #     paid_date = '2011-02-16',

    #     letter_1_send_date = '2011-02-01',
    #     letter_2_send_date = '2011-02-15',
    #     letter_3_send_date = '2011-02-21')

    #     retval = str(c)
    #     self.assertTrue(retval == "00006000:12\t123")

    # TODO CURRENTLY NOT WORKING
    #
    #
    # def test_save(self):
    #     cl = Client.objects.create(name="Sandeep's Store", 
    #     late_fee=100.00, 
    #     address="123 Address")

    #     b = Bank.objects.create(routing_n="00007700",
    #     address = "someaddaress",
    #     phone_num = "123456789",
    #     contact_name = "big fun")

    #     a = Account.objects.create(first_name1 = "Andy",
    #     first_name2 = "Charles",
    #     last_name1 = "Harding",
    #     last_name2 = "Martinet",
    #     street_addr = "123 Somewhere St.",
    #     city_addr = "Middle of",
    #     state_addr = "Nowhere",
    #     zip_addr = "123000",
    #     routing_num = b,
    #     account_num = "77",
    #     phone_num = "(864) 123-4567")

    #     c = Check.objects.create(
    #     to_client = cl,
    #     from_account = a,
    #     amount = 300.00,
    #     made_date = '2010-10-25',
    #     check_num = 123,

    #     amount_paid = 300.00,
    #     paid_date = '2011-02-16')

    #     Check.save(c)
    #     # self.assertTrue(c.created_date == datetime.today() and c.letter_1_send_date == c.created_date + c.to_client.wait_period and c.self.letter_2_send_date == c.created_date + 2 * c.to_client.wait_period)
    #     self.assertTrue(c.created_date == datetime.today())
        

    if __name__ == '__main__':
        unittest.main()