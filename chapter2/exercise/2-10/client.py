#!/usr/bin/env python

from socket import *
from msgsendrecv import *

HOST = 'localhost'
PORT = 11451
BUFSIZ = 1024
ADDR = (HOST, PORT)
NAME = input('NAME > ')
ROOM = input('ROOM > ')

s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)
s.send(f"{NAME} {ROOM}".encode())

recv = RecvThread(s, BUFSIZ)
send = SendThread(s)

send.start()
recv.start()