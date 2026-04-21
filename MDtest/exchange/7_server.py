# from socket import *
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5555))
sock.listen(1)

while True:
    c, addr = sock.accept()
    data = c.recv(1024)
    print(data.decode())
    c.send(b'ack')
    c.close()
