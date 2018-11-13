from django.test import TestCase
from accounts.models import Client
from django.test import Client as VisitorClient
from accounts.models import Bank
from accounts.models import Account
import unittest
from address.models import AddressField
from datetime import timedelta
import unicodedata

class exc:
    @staticmethod
    def zde_pass():
        return 10*(10/0)
        
    @staticmethod    
    def zde_fail():
        return 10*10

class TestAccount(unittest.TestCase):

    def test_invalid_Account_acct_num(self):
        try:
            b = Bank.objects.create(routing_n="000000010",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", street_addr = "123 Somewhere St.", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", routing_num = b,
            account_num = 123,
            phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)
    
    def test_invalid_Account_acct_neg(self):
        try:
            b = Bank.objects.create(routing_n="000000020",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", street_addr = "123 Somewhere St.", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", routing_num = b,
            account_num = -1,
            phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)
    
    def test_invalid_Account_acct_noacct(self):
        try:
            b = Bank.objects.create(routing_n="000000030",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", street_addr = "123 Somewhere St.", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", routing_num = b, phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_rout_int(self):
        try:
            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", street_addr = "123 Somewhere St.", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = 0,
            account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_rout_str(self):
        try:
            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", street_addr = "123 Somewhere St.", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = "0",
            account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)
    
    def test_invalid_Account_address_int(self):
        try:
            b = Bank.objects.create(routing_n="000000100",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = 123, city_addr = "Middle of", state_addr = "Nowhere", zip_addr = 123000, 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_address_null(self):
        try:
            b = Bank.objects.create(routing_n="000000200",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = None, city_addr = None, state_addr = None, zip_addr = None, 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_address_noaddress(self):
        try:
            b = Bank.objects.create(routing_n="000000300",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name1_firstempty(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name1_firstnull(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = None, first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name1_nofirst(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name1_lastempty(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "Charles", last_name1 = "", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name1_lastnull(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "Charles", last_name1 = None, last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name1_nolast(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "Charles", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name2_firstempty(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name2_firstnull(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = None, last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name2_nofirst(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", last_name1 = "Harding", last_name2 = "Martinet", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name2_lastempty(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name2_lastnull(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "Charles", last_name1 = "Harding", last_name2 = None, 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_name2_nolast(self):
        try:
            b = Bank.objects.create(routing_n="000001000",
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "big fun")

            a = Account.objects.create(first_name1 = "Mike", first_name2 = "Charles", last_name1 = "Harding", 
            street_addr = "123 Address", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", 
            routing_num = b, account_num = "0", phone_num = "(864) 123-4567")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_valid_Account_phone_nophone(self):
        try:
            b = Bank.objects.create(routing_n="00010000",
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
            account_num = 0)

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_invalid_Account_phone_float(self):
        try:
            b = Bank.objects.create(routing_n="00020000",
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
            account_num = 0,
            phone_num = 864.9912714)

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Account_phone_null(self):
        try:
            b = Bank.objects.create(routing_n="000000001",
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
            account_num = 0,
            phone_num = None)

            self.assertTrue(False)
        except:
            self.assertTrue(True)

class TestClient(unittest.TestCase):

    def test_valid_Client_allattrib(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            wait_period=timedelta(days=14), 
            late_fee=100.00, 
            address="123 Address", 
            phone_num="(123) 456-7890")

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_valid_Client_minattrib(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            late_fee=100.00, 
            address="123 Address")

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_invalid_Client_noattrib(self):
        try:
            c = Client.objects.create()

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_address_int(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, 
            address=123, 
            phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_address_null(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, 
            address=None, 
            phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_address_noaddress(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_valid_Client_late_zero(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), 
            late_fee=0, 
            address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_invalid_Client_late_str(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), 
            late_fee="asdfas", 
            address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_late_neg(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), 
            late_fee=-314.00, 
            address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)
    
    def test_invalid_Client_late_null(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), 
                late_fee=None, 
                address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_late_nolate(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_name_number(self):
        try:
            c = Client.objects.create(name=123, 
            wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_name_empty(self):
        try:
            c = Client.objects.create(name="", 
            wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_name_null(self):
        try:
            c = Client.objects.create(name=None, 
            wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_name_noname(self):
        try:
            c = Client.objects.create(wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_phone_int(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", 
            phone_num=1234567)

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_phone_float(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", 
            phone_num=12345.67)

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_phone_null(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, address="123 Address", 
            phone_num=None)

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_phone_nophone(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", wait_period=timedelta(days=14), late_fee=100.00, address="123 Address")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_valid_Client_wait_nowait(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_invalid_Client_wait_str(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            wait_period="wait", 
            late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_wait_negdelta(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            wait_period=timedelta(days=-14), 
            late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)
    
    def test_invalid_Client_wait_num(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            wait_period=14, 
            late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_wait_empty(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            wait_period=14, 
            late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_invalid_Client_wait_null(self):
        try:
            c = Client.objects.create(name="Sandeep's Store", 
            wait_period=None, 
            late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

            self.assertTrue(False)
        except:
            self.assertTrue(True)

class TestBank(unittest.TestCase):
    def test_valid_Bank_allattrib(self):
        try:
            b = Bank.objects.create(routing_n="100000000",
            name = "Bobby's Bank", 
            address = "someaddaress",
            phone_num = "123456789",
            contact_name = "Some guy")

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_valid_Bank_minattrib(self):
        try:
            b = Bank.objects.create(routing_n="200000000")

            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_valid_Bank_noattrib(self):
        try:
            b = Bank.objects.create()

            self.assertTrue(False)
        except:
            self.assertTrue(True)

class TestAccount_methods(unittest.TestCase):
    def test_str(self):
        b = Bank.objects.create(routing_n="00005500", address = "someaddaress", phone_num = "123456789", contact_name = "big fun")

        a = Account.objects.create(first_name1 = "Andy", first_name2 = "Charles", last_name1 = "Harding", last_name2 = "Martinet", 
        street_addr = "123 Somewhere St.", city_addr = "Middle of", state_addr = "Nowhere", zip_addr = "123000", routing_num = b, 
        account_num = "45", phone_num = "(864) 123-4567")

        retval = str(a)
        self.assertTrue(retval == "00005500:45")

class TestClient_methods(unittest.TestCase):
    def test_str(self):
        c = Client.objects.create(name="A nice store", late_fee=100.00, address="123 Address", phone_num="(123) 456-7890")

        retval = str(c)
        self.assertTrue(retval == "A nice store")

class TestBank_methods(unittest.TestCase):
    def test_str(self):
        b = Bank.objects.create(routing_n="00005700",
        name = "Bobby's Bank", 
        address = "someaddaress",
        phone_num = "123456789",
        contact_name = "Some guy")
        
        retval = str(b)
        self.assertTrue(retval == "00005700")

    def test_make_name(self):
        b = Bank.objects.create(routing_n="00005900",
        name = "Bobby's Bank", 
        address = "someaddaress",
        phone_num = "123456789",
        contact_name = "Some guy")
        
        retval = Bank.make_name(b)
        self.assertTrue(retval == "bank00005900")




if __name__ == '__main__':
    unittest.main()