#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    tcpClientSocket.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpClientSocket.send(f'{data}\r\n'.encode())
    data = tcpClientSocket.recv(BUFSIZ)
    if not data:
        break
    print(data.decode().strip())
    tcpClientSocket.close()