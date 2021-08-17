#!/usr/bin/env python

from socket import *
from sys import argv    

HOST = 'localhost'
PORT = 21567
if len(argv) > 1:
    HOST = argv[1]
if len(argv) > 2:
    PORT = int(argv[2])
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpClientSocket = socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        data = input('> ')
        if data is not None:
            break
        udpClientSocket.sendto(data.encode(), ADDR)
        data, ADDR = udpClientSocket.recvfrom(BUFSIZ)
        if not data:
            break
        print(data.decode())
finally:
    udpClientSocket.close()