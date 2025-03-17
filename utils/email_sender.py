import os
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import EmailStr

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = 587
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

async def sendMail(email: EmailStr, subject: str, body: str):
  message = MIMEMultipart()
  message['From'] = SMTP_USER
  message['To'] = email
  message['Subject'] = subject
  message.attach(MIMEText(body, 'html'))

  async with aiosmtplib.SMTP(hostname=SMTP_HOST, port=SMTP_PORT, use_tls=True) as smtp:
    await smtp.login(SMTP_USER, SMTP_PASSWORD)
    await smtp.send_message(message)

