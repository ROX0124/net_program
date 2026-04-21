# from socket import *
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 80))

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode()

    if msg.startswith('/exam?q='):
        q = msg.split('=', 1)[1]
        resp = f'Hello, {q}'
    else:
        resp = 'Not Found'

    sock.sendto(resp.encode(), addr)
