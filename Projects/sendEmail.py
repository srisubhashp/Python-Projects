import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='Sri Subhash Pathuri'
email['to']='srisubhash234@gmail.com'
email['subject']='You won 1,000,000 dollars.'

email.set_content('Hare krishna Everyone, I want to develop an innovative financial product.')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sspacademic@gmail.com','Harekpl@4')
    smtp.send_message(email)

    print('All good boss.')

