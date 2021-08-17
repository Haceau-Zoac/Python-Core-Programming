#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 1145
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(ADDR)
    print(s.recv(BUFSIZ).decode())

    while True:
        data = input('> ')
        if not data: break
        s.send(data.encode())
        data = s.recv(BUFSIZ)
        if not data: break
        print(data.decode())