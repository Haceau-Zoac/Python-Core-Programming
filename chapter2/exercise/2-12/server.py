#!/usr/bin/env python

# 参考 https://github.com/schedutron/CPAP/blob/master/Chap2/sleep_serv.py

from socket import *

HOST = ''
PORT = 1145
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(5)
    clnt, addr = s.accept()
    print(f'连接到 {addr}。')

    with clnt:
        while True:
            msg = clnt.recv(BUFSIZ)
            if not msg: break
            sec = msg.decode()
            msg = f"sleep({sec})"
            tup = addr + (sec, )
            print(f"%s:%s 请求睡眠 %s 秒。" % tup)
            clnt.send(msg.encode())

    print(f"{addr} 断开。")
