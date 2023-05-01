import smtplib
from email.message import EmailMessage
import ssl

sender = 'megh.shah2003@gmail.com'
password = '' 
# Use your password through google apppasswords
receiver = input()

subject = 'Test email'
body = """
Hey! I'm learning to send emails using python.
"""

test = EmailMessage()
test['From'] = sender
test['To'] = receiver
test['Subject'] = subject
test.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, test.as_string())
