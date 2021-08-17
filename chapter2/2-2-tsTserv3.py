#!/usr/bin/env python

from socket import *
from time import ctime

主机 = ''
端口 = 21567
缓冲区大小 = 1024
地址 = (主机, 端口)

with socket(AF_INET, SOCK_STREAM) as tcp服务器:
    tcp服务器.bind(地址)
    tcp服务器.listen(5)

    while True:
        print('等待连接...')
        tcp客户端, 地址 = tcp服务器.accept()
        print('...连接来自：', 地址)

        with tcp客户端:
            while True:
                数据 = tcp客户端.recv(缓冲区大小)
                if not 数据:
                    break
                tcp客户端.send(('[%s] %s' % 
                    (bytes(ctime(), 'utf-8'), 数据.decode('utf-8'))).encode())