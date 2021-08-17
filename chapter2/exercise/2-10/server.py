#!/usr/bin/env python

# 参考 https://zhuanlan.zhihu.com/p/149038324

from socket import *
from threading import Thread
from msgsendrecv import *

HOST = 'localhost'
PORT = 11451
BUFSIZ = 1024
ADDR = (HOST, PORT)

clients = {}

class UserThread(Thread):

    def __init__(self, conn, addr):
        super(UserThread, self).__init__()
        self.conn = conn
        self.addr = addr
    
    def run(self):
        datas = self.conn.recv(BUFSIZ).decode().split(' ')
        name = datas[0]
        if len(datas) < 2:
            self.room = 'default'
        else:
            self.room = datas[1]
        clients[self] = name
        self.brodcast(f'欢迎 {name} 加入聊天室。')
        while True:
            try:
                msg = self.conn.recv(1024).decode()
                self.brodcast(f'{name}: {msg}')
            except OSError:
                self.conn.close()
                del clients[self]
                self.brodcast(f'{name} 离开聊天室。')
    
    def brodcast(self, msg):
        for conn in filter(lambda c : c.room == self.room, clients):
            conn.conn.send(f"{msg}\n".encode())


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(10)
    print('服务器已启动。')

    while True:
        conn, address = s.accept()
        print(address, '已加入。')
        conn.send('你已加入聊天室。\n'.encode())
        ut = UserThread(conn, address)
        ut.start()
