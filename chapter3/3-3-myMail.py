#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

who = input('who > ')
pwd = input('password > ')

body = '''\
From: %(who)s
To: %(who)s
Subject: test msg

Hello World!
''' % {'who': who}

sendSvr = SMTP('smtp.qq.com')
sendSvr.login(who, pwd)
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3('pop.qq.com')
recvSvr.user(who)
recvSvr.pass_(pwd)
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index(b'')
recvBody = msg[sep+1:]
for eachLine in recvBody:
    print(eachLine.decode())