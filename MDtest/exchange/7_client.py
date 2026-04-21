# from socket import *
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5555))

sock.send(b'Hello, IoT')
data = sock.recv(1024)
print(data.decode())

sock.close()
