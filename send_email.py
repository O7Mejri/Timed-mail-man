# Default sender
# uses SSL encryption

import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import schedule
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

# get the vars
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PW = os.environ.get("PW")
SMTP_SERVER = "smtp.gmail.com"
PORT = 465

# define the function
def sendMail():
    context = ssl.create_default_context()

    rec = "oussama326mejri@gmail.com"
    sbj = "YOU BEING STUPID"
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"I will later provide my resons \n\n Current Date and Time: {current_datetime}"

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = rec
    msg["Subject"] = sbj

    msg.attach(MIMEText(body, "plain"))

    text = msg.as_string()

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(EMAIL, PW)
        server.sendmail(EMAIL, rec, text)
        print("EMAIL SENT!")




# Running

if __name__ == '__main__':
    sendMail()