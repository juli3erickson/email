# #PyZTM221
# import smtplib
# from email.message import EmailMessage
#
# email = EmailMessage()
#
# email['from'] = 'a'
# email['to'] = 'a'
# #email['to'] = 'b'
# email['subject'] = 'You won 1,000,000 dollars!'
#
# email.set_content('I am a Python Master!')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('b', 'b_pass')
#     smtp.send_message(email)
#     print('all good boss!')

#PyZTM222
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'A'
email['to'] = 'a'
#email['to'] = 'b'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name='TinTin'))
email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('b', 'p_pass')
    smtp.send_message(email)
    print('all good boss!')