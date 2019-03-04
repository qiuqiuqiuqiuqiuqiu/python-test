#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['ethan.qiu@oracle.com']

message = MIMEText('Python email test...', 'plain', 'utf-8')
message['From'] = Header("runoob", 'utf-8')
message['To'] = Header('test', 'utf-8')

subject = 'Python SMTP email test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "email send successful"
except smtplib.SMTPException:
    print "Error: send fail"