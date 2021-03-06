from django.core.management.base import BaseCommand, CommandError
from accounts.models import *
from checks.models import *
from users.models import User
from datetime import timedelta

# DATA FOR POPULATING THE DATABASE

CLIENT_DETS = [
    {
        'name': "Papa John's Pizza", 
    },
    {
        'name': "Walmart", 
        'wait_period': timedelta(days=20),
    },
    {
        'name': "Spinx", 
        'address': '3100 SC-14, Greenville, SC 29615'
    },
    {
        'name': "Waldo's World", 
        'phone_num': '(864) 642-3123'
    },
    {
        'name': "Junk Shop", 
        'wait_period': timedelta(days=5),
    },
]

BANK_DETS = [
    {
        'routing_n': '12214',
        'name': 'First Bank of America',
        'contact_name': 'Joe Schmoe'
    }, {
        'routing_n': '12814',
        'name': 'South State Bank',
        'address': ' 79 S Main St, Inman, SC 29349',
    },
    {
        'routing_n': '16214',
        'name': 'Capitol One',
        'phone_num': '(231) 212-8328',
    },
    {
        'routing_n': '10214',
        'name': 'Wells Fargo',
    },
    {
        'routing_n': '12274',
    }
]

ACCOUNT_DETS = [
    {
        'first_name1': 'Jill',
        'last_name1': 'Jones',
        'street_addr': '2132 Orchard Ct.',
        'city_addr': 'Anderson',
        'state_addr': 'SC',
        'zip_addr': '12321',
        'routing_num': None,
        'account_num': '23423212332',
        'phone_num': '(827) 213 - 2123'
    }, 
    {
        'first_name1': 'Jim',
        'last_name1': 'Bob',
        'street_addr': '21 Boiling Brook Dr.',
        'city_addr': 'Simpsonville',
        'state_addr': 'SC',
        'zip_addr': '12241',
        'routing_num': None,
        'account_num': '23423212332',
    }, 
    {
        'first_name1': 'Donald',
        'last_name1': 'Macy',
        'first_name2': 'Holly',
        'last_name2': 'Macy',
        'street_addr': '21 Boiling Brook Dr.',
        'city_addr': 'Simpsonville',
        'state_addr': 'SC',
        'zip_addr': '12241',
        'routing_num': None,
        'account_num': '23423212332',
    }, 
    {
        'first_name1': 'Joy',
        'last_name1': 'Smith',
        'street_addr': '7321 Jones St.',
        'city_addr': 'Greenville',
        'state_addr': 'NC',
        'zip_addr': '72841',
        'routing_num': None,
        'account_num': '23423212332',
    }, 
    {
        'first_name1': 'Mary',
        'last_name1': 'Jane',
        'street_addr': '91 Shoe St.',
        'city_addr': 'Greer',
        'state_addr': 'SC',
        'zip_addr': '72881',
        'routing_num': None,
        'account_num': '23423212332',
    }
]

class Command(BaseCommand):
    """
    This command populates the data base with at least 20 accounts and at least 30 checks
    """
    help = 'Populates the DB with checks'

    def handle(self, *args, **options):
        # make 5 clients, that all have 5 accounts that have written them 2 bad checks
        # each client has a user associated with them
        # each account has a different bank because that's easiest
        # each client has a user that is associated with them
        # this creates users, but you have to set the passwords in admin, can't script it
        
        for i in range(0,5):
            # make checkhunter employee
            if not User.objects.filter(username=f"Employee{i}User").exists():
                check_hunter_employee = User.objects.update_or_create(username=f"Employee{i}User")
            # make client
            client, new = Client.objects.update_or_create(**CLIENT_DETS[i])
            # make 
            if not User.objects.filter(username=f"Client{i}User").exists():
                client_user, new = User.objects.update_or_create(username=f"Client{i}User", client=client)
                
            bank, new = Bank.objects.update_or_create(**BANK_DETS[i])
            account_dets = ACCOUNT_DETS[i]
            account_dets['routing_num'] = bank

            check_dets = {
                'to_client': client,
                'from_account': None,
                'amount': 23.90,
                'made_date': None,
                'check_num': None,
            }
            # add 2 checks for each person
            for x in range(0,4):
                account_dets['account_num'] = (x * 4) + i
                account, new = Account.objects.update_or_create(**account_dets)
                check_dets['from_account'] = account
                check_dets['made_date'] = datetime.today() - timedelta(days =  x * 5)
                check_dets['check_num'] = (x * 4) + i
                check1, new = Check.objects.update_or_create(**check_dets)
                
                check_dets['made_date'] = datetime.today() - timedelta(days =  x * 10)
                check_dets['check_num'] = ((x * 4) + i) * 2
                check2, new = Check.objects.update_or_create(**check_dets)

        self.stdout.write(f"Now {Account.objects.count()} Accounts in DB")
        self.stdout.write(f"Now {Check.objects.count()} Checks in DB")