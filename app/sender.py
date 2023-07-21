import os
import smtplib
import ssl

from dotenv import load_dotenv

load_dotenv()


def send_emails(message):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv('GMAIL_SMTP_PASSWORD')
    username = os.getenv('GMAIL')
    receiver = username

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

