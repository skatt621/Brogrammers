# util methods for checks
from .models import Check
from datetime import datetime
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io
from django.template.loader import render_to_string
from reportlab.platypus import PageBreak


LETTER_TEMPLATE = """
{{recipient_name}}
{{st_addr}}
{{city}}, {{state}} {{zip}}

{{date}}

Dear {{recipient_name}}:

Check {{check_num}} you wrote for ${{check_amt}}, dated {{made_date}}, which was made payable to {{to_client}} was returned by {{bank_name}}.
Unless full payment of the check is received by cash within {{wait_period}} days after the date this demand letter was mailed, together with ${{late_fee}} in bank fees, we will file a small claims court claim against you.
You may wish to contact a lawyer to discuss your legal rights and responsibilities.
Sincerely,
Check Hunters
"""

def PopulateTemplate(letters_info: dict) -> bool:
    """
    takes a dictionary and uses information to generate letters
    returns bool of success of printing those letters
    """
    # create a file-like bugger to receive PDF data
    buffer = io.BytesIO()
    # create a PDF object using the buffer as its "file"
    p = canvas.Canvas(buffer)
    # 'draw' letters on the pdf. the PDF generation
    for key, letters in letters_info.items():
        for letter_data in letters:
            rendered = render_to_string(LETTER_TEMPLATE, letter_data)
            p.drawString(100, 100, rendered)
            # p.append(PageBreak())
    # close the PDF object cleanly
    p.showPage()
    p.save()
    return True, FileResponse(buffer, as_attachment=True, filename='LettersToPrint.pdf')

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
        'recipient_name': check.name, # TODO make name function
        'st_addr': check.from_account.street_addr,
        'city': check.from_account.city_addr,
        'state': check.from_account.state_addr,
        'zip': check.from_account.zip_addr,
        'date': datetime.today().strftime("%m/%d/%Y"),
        'to_client': check.to_client.name,
        'check_num': check.check_num,
        'made_Date': check.made_date,
        'bank_name': str(check.from_account.routing_num),
        'check_amt': check.amount,
        'late_fee': check.to_client.late_fee,
        'wait_period': check.to_client.wait_period,
    }