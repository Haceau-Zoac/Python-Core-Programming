#!/usr/bin/env python

from socket import *
from msgsendrecv import *

HOST = ''
PORT = 11451
BUFSIZ = 1024
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
s.bind(ADDR)
s.listen(1)

print('Waiting...')
ws, addr = s.accept()

recv = RecvThread(ws, BUFSIZ)
send = SendThread(ws)

send.start()
recv.start()