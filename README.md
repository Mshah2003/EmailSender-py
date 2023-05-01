# EmailSender-py
Python email sender 
The code sends an email using the Gmail SMTP server and the Python smtplib library:

Import the necessary modules:
import smtplib
from email.message import EmailMessage
import ssl
This imports the smtplib module for sending email, the EmailMessage class for creating email messages, and the ssl module for creating a secure SSL connection with the SMTP server.

Set the sender's email address,password, and receiver's email address:

Set the email subject and body:

Create an EmailMessage object and set its properties:

Create an SSL context object:
context = ssl.create_default_context()

Create an SMTP object and establish a secure connection with the Gmail SMTP server:
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
This creates a new SMTP_SSL object with the server address 'smtp.gmail.com', the port number 465, and the SSL context object created earlier. The with statement ensures that the SMTP connection is properly closed after the email is sent.


Login to the email server:
smtp.login(sender, password)
This logs in to the Gmail SMTP server using the sender's email address and password.

Send the email:
smtp.sendmail(sender, receiver, test.as_string())
This sends the email message.
