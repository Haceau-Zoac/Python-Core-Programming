#!/usr/bin/env python

# 参考 https://github.com/schedutron/CPAP/blob/master/Chap2/sleep_clnt.py

from socket import *
from time import sleep

HOST = input('Enter host: ')
if not HOST:
    HOST = 'localhost'

PORT = input('Enter port: ')
if not PORT:
    PORT = 1145
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(ADDR)
    print('连接已建立。请输入睡眠秒数作为您的消息。它可以很小。')
    while True:
        msg = input("睡眠秒数：")
        if not msg: break
        s.send(msg.encode())
        command = s.recv(BUFSIZ)
        if not command: break
        print(f'睡眠了 {msg} 秒。')
        exec(command.decode())