#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 1145
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(5)
    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(BUFSIZ).decode()
            print(data)
            data = input('> ').encode()
            conn.send(data)