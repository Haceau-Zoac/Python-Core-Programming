#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 1145
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(ADDR)
    while True:
        data = input('> ').encode()
        s.send(data)
        data = s.recv(BUFSIZ).decode()
        print(data)