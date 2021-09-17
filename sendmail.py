import smtplib
import os
SUBJECT="contact to solve your issue"
s = smtplib.SMTP('smtp.gmail.com',587)
def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("heartdiseaseprediction2021@gmail.com", "heartdiseaseprediction")
    Message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("heartdiseaseprediction2021@gmail.com", email, Message)
    s.quit()
