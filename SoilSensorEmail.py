import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

channel=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

from_email_addr="3783205452@qq.com"
from_email_pass="unaaeikgaowecbib"
to_email_addr="3159897866@qq.com"

smtp_server="smtp.qq.com"
smtp_port=587
def send_email(subject,body):
	msg=EmailMessage()
	msg.set_content(body)
	msg['From']=from_email_addr
	msg['To']=to_email_addr
	msg['Subject']=subject
	server=smtplib.SMTP(smtp_server,smtp_port)
	server.starttls()
	server.login(from_email_addr,from_email_pass)
	server.send_message(msg)
	print("Email sent:"+subject)
	server.quit()
print("Soil moisture check start...")
if GPIO.input(channel):
		print("Water NOT detected!Soil is dry.")
		send_email("Plant needs watering!","Your plant soil is dry.Please water it.")
else:
		print("Water detected!Soil moisture is OK.")
		send_email("Plant status OK","Soil moisture is sufficient.No action needed.")
GPIO.cleanup()
print("Check completed.")
