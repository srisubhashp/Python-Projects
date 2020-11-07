import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('sendPersEmail.html').read_text())
email=EmailMessage()

email['from']='Sri Subhash Pathuri'
email['to']='srisubhash234@gmail.com'
email['subject']='You have won a 1,000,000 dollars!'

email.set_content(html.substitute({'name':'Tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sspacademic@gmail.com','Harekpl@4')
    smtp.send_message(email)
    print('All good Boss.')


