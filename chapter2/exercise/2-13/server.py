#!/usr/bin/env python

# 参考 https://github.com/schedutron/CPAP/blob/master/Chap2/name_serv.py

from os import read
from socket import *
from select import select

HOST = ''
PORT = 1145
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as serv:
    serv.bind(ADDR)
    serv.listen(10)

    inputs = [serv]
    outputs = []
    exceptional = []

    services = {}

    print('等待连接...')
    while True:
        readable, writeable, exceptional = select(inputs, outputs, inputs)

        for s in readable:
            if s is serv:
                user, user_addr = s.accept()
                inputs.append(user)
                msg = "如果你想添加一个服务器，只要输入 {<主机名> <端口号>}，你的服务器就会在这个名称服务器里注册名称。\n"
                msg += "这样可以让客户端更容易地找到你的服务器。\n\n"
                msg += "如果你是一个客户，你可以简单地输入一个服务器名来获取它的地址，或者用 {show} 查看所有存在的服务器。\n\n"
                user.send(msg.encode())
                print(f'{user_addr} 已连接。')
            else:
                msg = s.recv(BUFSIZ).decode()
                if not msg:
                    s.close()
                    inputs.remove(s)
                elif msg == "{show}":
                    if services == {}:
                        s.send("无可用服务器 :(".encode())
                    else:
                        resp = '\n'
                        for service in services:
                            resp += f"{service} - {services[service]}\n"
                        s.send(resp.encode())
                elif msg[0] == '{':
                    comp = msg[1:-1].split()
                    addr = comp[1]
                    name = comp[0]
                    if name in services:
                        s.send(f"服务器 {name} 已存在。".encode())
                    else:
                        services[name] = addr
                        s.send(f"服务器 {name} 已添加！".encode())
                else:
                    if msg in services:
                        s.send(f"{msg} - {services[msg]}".encode())
                    else:
                        s.send("这样的服务器不存在。".encode())
        
        for s in exceptional:
            s.close()
            inputs.remove(s)
            print(f"{s.getpeername()} 已断开连接。")

                
