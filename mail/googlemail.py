from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from data.config import *

def mail(message, em):
    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    password = PASSWORD_MAIL
    msg['From'] = "testiki342@gmail.com"
    msg['To'] = em
    msg['Subject'] = "Отчет"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))


if __name__ == "__main__":
    mail('тест', "testiki342@gmail.com")
