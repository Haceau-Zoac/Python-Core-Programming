#!/usr/bin/env python

from socket import *

HOST = input('HOST > ')
PORT = 80
BUFSIZ = 16384
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(ADDR)
    s.send(b'GET / HTTP/1.1\n')

    with open('website.txt', 'w') as file:
        while True:
            data = s.recv(BUFSIZ).decode()
            if len(data) < 1: break
            file.write(data)
    
