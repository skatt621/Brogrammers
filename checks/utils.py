# util methods for checks
from .models import Check
from datetime import datetime
def PopulateTemplate(letters_info: dict) -> bool:
    """
    takes a dictionary and uses information to generate letters
    returns bool of success of printing those letters
    """
    pass    # TODO
    return False

def GetLettersData(user) -> dict:
    """
    takes a user and 
    returns dictionary of letter info for checks user has access to
    """
    # TODO after authorization is implemented
    # if (user.client):
    #     checks = Check.objects.filter(to_client=user.client)
    # else:
    checks = Check.objects.all()
    letter_info = {
        'first_letters': [],
        'second_letters': [],
        'third_letters': [],
        }
    today = datetime.today()

    # generate 1st letter info
    for check in checks.filter(letter_1_send_date=today, paid_date__isnull=True):
        letter_info['first_letters'].append(ExtractCheckInfo(check))
    # generate 2nd letter info
    for check in checks.filter(letter_2_send_date=today, paid_date__isnull=True):
        letter_info['second_letters'].append(ExtractCheckInfo(check))
    # generate 3rd letter info
    for check in checks.filter(letter_3_send_date=today, paid_date__isnull=True):
        letter_info['third_letters'].append(ExtractCheckInfo(check))

    return letter_info

def ExtractCheckInfo(check) -> dict:
    """
    takes a check, 
    returns the dictionary of information for printing out its letter
    """
    return {
        'CheckDate': check.made_date,

        'Street': check.from_account.street_addr,
        'City': check.from_account.city_addr,
        'State': check.from_account.state_addr,
        'ZipCode': check.from_account.zip_addr,

        # 'toClient':,
        'Recipient': check.to_client.name,
        'CheckNo': check.check_num,
        'Bank': str(check.from_account.routing_num),
        'CheckAmount': check.amount,
        'LateFee': check.to_client.late_fee,
    }