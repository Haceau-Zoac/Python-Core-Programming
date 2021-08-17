# Echo server program
import socket
from time import ctime
import os

def psend(conn, prompt, data):
    conn.sendall(('[%s] %s' %
        (prompt, data.decode())
    ).encode())

HOST = ''       # Symbolic name meaning all available interfaces
PORT = 50007    # Arbitrary non-previleged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            datas = data.decode().split(' ')
            if len(datas) > 0:
                if datas[0] == 'date':
                    psend(conn, bytes(ctime(), 'utf-8'), data)
                elif datas[0] == 'os':
                    psend(conn, os.name, data)
                elif datas[0] == 'ls':
                    if len(datas) > 1:
                        psend(conn, os.listdir(datas[1]), data)
                    else:
                        psend(conn, os.listdir(os.curdir), data)
                else:
                    conn.sendall(data)
            else:
                conn.sendall(data)