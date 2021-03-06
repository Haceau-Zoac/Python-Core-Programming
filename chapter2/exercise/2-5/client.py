# Echo client program
import socket

HOST = 'localhost'      # The remote host
PORT = 50007            # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = input('> ')
    s.sendall(data.encode())
    data = s.recv(1024)
print('Received', repr(data.decode()))