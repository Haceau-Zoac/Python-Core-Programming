#!/usr/bin/env python

from socket import *
from sys import argv

主机 = '127.0.0.1'
端口 = 21567
if len(argv) > 1:
    主机 = argv[1]
if len(argv) > 2:
    端口 = int(argv[2])
缓冲区大小 = 1024
地址 = (主机, 端口)

with socket(AF_INET, SOCK_STREAM) as tcp客户端:
    tcp客户端.connect(地址)

    while True:
        数据 = input('> ')
        if not 数据:
            break
        tcp客户端.send(数据.encode())
        数据 = tcp客户端.recv(缓冲区大小)
        if not 数据:
            break
        print(数据.decode('utf-8'))