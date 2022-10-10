# mime = multipurpose internet mail extension 


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import name
import smtplib



template = Template(Path(r"/home/pyrex/Desktop/Email Sender/template.html").read_text())


message = MIMEMultipart()
message["from"] = "Peter Griffin"
message["to"] = name.reciver_email_id
message["subject"] = "Test Alert !!"
body = template.substitute({"name":"john"})
message.attach(MIMEText(body,"html"))
message.attach(MIMEImage(Path(r"//home/pyrex/Desktop/Email Sender/Sorry.webp").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(name.sender_email_id, name.sender_email_pass)
    smtp.send_message(message)
    print("Sent..")