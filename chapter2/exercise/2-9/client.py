#!/usr/bin/env python

from socket import *
from msgsendrecv import *

HOST = 'localhost'
PORT = 11451
BUFSIZ = 1024
ADDR = (HOST, PORT)
NAME = input('NAME > ')

s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)
s.send(NAME.encode())

recv = RecvThread(s, BUFSIZ)
send = SendThread(s)

send.start()
recv.start()