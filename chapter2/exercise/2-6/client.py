#!/usr/bin/env python

import socket

HOST = 'localhost'
PORT = socket.getservbyname('daytime')
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello', ADDR)
    data, addr = s.recvfrom(BUFSIZ)
    print(data.decode())