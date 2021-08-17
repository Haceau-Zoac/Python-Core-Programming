#!/usr/bin/env python

from socketserver import (TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...连接到：', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),
            self.rfile.readline().decode())).encode())

tcpServ = TCP(ADDR, MyRequestHandler)
print('等待连接...')
tcpServ.serve_forever()