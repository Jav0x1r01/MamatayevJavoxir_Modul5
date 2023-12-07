# celery Haqida malumot
# Celery biror bir vazifani bajarganda o'ziga yangi oqim
# ochadi va vazifani orqa fonda bajaradi va asosiy codga xalaqt bermaydi.
import smtplib
import ssl

from celery import Celery
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Celery('hello', broker='redis://localhost:6379/0')


@app.task
def send_email(emails):
    for email in emails:
        sender_email = "mamatayevjavoxir@gmail.com"
        receiver_email = email
        password = "mcijwnfpuxustoup"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Test"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"""Modul 5 imtixon
        
      """

        part1 = MIMEText(text, "plain")

        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )


