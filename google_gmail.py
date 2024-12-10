import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

my_mail=os.getenv("username")
yourpassword=os.getenv("gmail_password")
email_receiver="alejandro.arrietanu@gmail.com"

subject="test"
body="Testo"

em=EmailMessage()
em["From"]=my_mail
em["To"]=email_receiver
em["Subject"]=subject
em.set_content(body)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as connection:
    connection.login(user=my_mail,password=yourpassword)
    connection.sendmail(from_addr=my_mail,
                        to_addrs=email_receiver,
                        msg=em.as_string())
    print('Email sent successfully.')