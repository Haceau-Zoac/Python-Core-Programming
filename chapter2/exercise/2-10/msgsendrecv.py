from socket import *
import threading

class RecvThread(threading.Thread):

    def __init__(self, s, bufsize):
        if not isinstance(s, socket):
            raise TypeError
        
        super(RecvThread, self).__init__()
        self.s = s
        self.bufsize = bufsize
    
    def run(self):
        while True:
            data = self.s.recv(self.bufsize).decode()
            if not data:
                break
            print(f'{data}', end='')

class SendThread(threading.Thread):

    def __init__(self, s):
        if not isinstance(s, socket):
            raise TypeError
        
        super(SendThread, self).__init__()
        self.s = s
    
    def run(self):
        while True:
            data = input('> ').encode()
            self.s.send(data)