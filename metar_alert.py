import smtplib
import os
from email.mime.text import MIMEText

def send_email(old, new):
    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASS"]
    receiver = os.environ["EMAIL_TO"]

    msg = MIMEText(f"Temperature change: {old}°C → {new}°C")
    msg["Subject"] = "METAR Alert"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
