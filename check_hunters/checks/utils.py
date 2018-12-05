# util methods for checks
from .models import Check
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas  
from reportlab.lib.pagesizes import letter as letter_sizes
from reportlab.lib.enums import TA_JUSTIFY
from django.http import FileResponse, HttpResponse
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

MAX_CHARS_FIT = 90

LETTER_TEMPLATE = """
Dear {recipient_name}, Check {check_num} you wrote for ${check_amt}, dated {made_date}, which was made payable to {to_client} was returned by your bank, {bank_name}.
Unless full payment of the check is received by cash within {wait_period} days after the date this demand letter was mailed, together with ${late_fee} in bank fees, we will file a small claims court claim against you.
You may wish to contact a lawyer to discuss your legal rights and responsibilities.
Sincerely,
Check Hunters
"""

def setupCanvas(response):
    """
    sets up all the pdf settings
    returns the document, doc_width, and doc_height
    """
    # make PDF object using the response object as its file
    p = canvas.Canvas(response, pagesize=letter_sizes)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
    width, height = letter_sizes
    return p, width, height


def PopulateTemplate(letters_info: dict) -> bool:
    """
    takes a dictionary and uses information to generate letters
    returns bool of success of printing those letters
    """
    # make the HttpResponse obj with its PDF headers
    response = HttpResponse(content_type='application/pdf')
    date_str = datetime.today().strftime('%m-%d-%y')
    response['Content-Disposition'] = f'attachment;  filename = "{date_str}LettersToPrint.pdf"'
    p, width, height = setupCanvas(response)
        
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    
    # 'draw' letters on the pdf. the PDF generation
    for key, letters in letters_info.items():
        for letter_data in letters:
            rendered = letter_data['template'].format(**letter_data)
            line_x = width - 200
            line_y = height - (height / 3) + 50

            # draw address on pdf canvas
            for line in [letter_data['recipient_name'], letter_data['st_addr'], "{city}, {state} {zip}".format(**letter_data)]:
                p.drawString(line_x, line_y, line)
                line_y -= 20

            # draw letter on pdf canvas
            line_y = height - (height / 3) - 50
            line_x = 50
            # write date
            day = datetime.today().strftime("%m/%d/%Y")
            p.drawString(line_x, line_y, day)
            line_y -= 25
            # write letter
            
            for line in rendered.split('/n'):
                line = line.replace('.', '. ')
                # output wrapped line.
                while(len(line) > MAX_CHARS_FIT):
                    output_partial = line[0:MAX_CHARS_FIT]
                    # make sure line ends in between words
                    i = output_partial.rindex(' ')
                    output_partial = output_partial[0:i]   
                    p.drawString(line_x, line_y, output_partial)
                    # prep for next iterations
                    line = line[i:]
                    line_y -= 25
                # finish outputting wrapped line
                p.drawString(line_x, line_y, line)
                line_y -= 35
            # add page break to start next letter
            p.showPage()
    # close the PDF object cleanly
    p.save()
    # return True, FileResponse(buffer, as_attachment=True, filename=filename)
    return True, response

def GetLettersData(user: object) -> dict:
    """
    takes a user and 
    returns dictionary of letter info for checks user has access to
    """
    checks = Check.objects.filter(paid_date__isnull=True)
    letter_info = {
        'first_letters': [],
        'second_letters': [],
        'third_letters': [],
        }
    today = datetime.today().date()

    # generate 1st letter info
    for check in checks.filter(letter_1_sent=False).filter(letter_1_send_date__lte=today):
        letter_info['first_letters'].append(ExtractCheckInfo(check, 1))
    # generate 2nd letter info
    for check in checks.filter(letter_2_sent=False).filter(letter_1_sent=True).filter(letter_2_send_date__lte=today):
        letter_info['second_letters'].append(ExtractCheckInfo(check, 2))
    # generate 3rd letter info
    for check in checks.filter(letter_3_sent=False).filter(letter_2_sent=True).filter(letter_3_send_date__lte=today):
        letter_info['third_letters'].append(ExtractCheckInfo(check, 3))

    return letter_info

def ExtractCheckInfo(check: object, letter_num=1) -> dict:
    """
    takes a check, 
    returns the dictionary of information for printing out its letter
    """
    letter = LETTER_TEMPLATE
    if letter_num == 1:
        letter = check.to_client.letter_1_template
        check.letter_1_sent = True
    if letter_num == 2:
        letter = check.to_client.letter_2_template
        check.letter_2_sent = True
    if letter_num == 3:
        letter = check.to_client.letter_3_template
        check.letter_3_sent = True
    check.save()

    return {
        'template': letter,
        'recipient_name': check.name(),
        'st_addr': check.from_account.street_addr,
        'city': check.from_account.city_addr,
        'state': check.from_account.state_addr,
        'zip': check.from_account.zip_addr,
        'date': datetime.today().strftime("%m/%d/%Y"),
        'to_client': check.to_client.name,
        'check_num': check.check_num,
        'made_date': check.made_date.strftime("%m/%d/%Y"),
        'bank_name': str(check.from_account.routing_num),
        'check_amt': check.amount,
        'late_fee': check.current_fee(),
        'total': check.total(),
        'wait_period': check.to_client.wait_period.days,
    }