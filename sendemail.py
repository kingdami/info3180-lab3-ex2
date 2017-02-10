import smtplib

from_addr = ''
to_addr = 'icemandelano@hotmail.com'
from_name = "Sender"
to_name = "Receiver"
subject = "Test"
msg = " This is a test."
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if neeeded)
username = from_addr
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 

    