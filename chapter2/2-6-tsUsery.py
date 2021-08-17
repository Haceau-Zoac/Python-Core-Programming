#!/usr/bin/env python

from socket import *
from time import ctime

常_主机 = ''
常_端口 = 21567
常_缓冲区大小 = 1024
常_地址 = (常_主机, 常_端口)

udp服务器 = socket(AF_INET, SOCK_DGRAM)
udp服务器.bind(常_地址)

try:
    while True:
        print('等待消息...')
        数据, 地址 = udp服务器.recvfrom(常_缓冲区大小)
        udp服务器.sendto(('[%s] %s' % (bytes(ctime(), 'utf-8'), 数据)).encode())
        print('...信息获取和返回到了', 地址)
finally:
    print('over.')
    udp服务器.close()