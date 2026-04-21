# from socket import *
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 7000))

while True:
    data, addr = sock.recvfrom(1024)
    if data.decode() == 'ping':
        sock.sendto(b'pong', addr)
