#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = "778411597@qq.com"
# need to update this password or auth key
my_pass = ""
my_user = "778411597@qq.com"

mail_host = "smtp.qq.com"
mail_port = 465


def mail():
    ret = True
    try:
        msg = MIMEText('fill in email content', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])
        msg['To'] = formataddr(["FK", my_user])
        msg['Subject'] = "Runoob send email test"

        server = smtplib.SMTP_SSL(mail_host, mail_port)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user,], msg.as_string())
        server.quit()
    except Exception, e:
        print e.message
        ret = False
    return ret

ret = mail()
if ret:
    print("send email successful")
else:
    print("send email failed")
