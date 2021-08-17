#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = getservbyname('daytime')
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind(ADDR)

    while True:
        data, addr = s.recvfrom(BUFSIZ)
        s.sendto(data, addr)