# from socket import *
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 6789))
sock.listen(1)

while True:
    c, addr = sock.accept()

    data = c.recv(1024)
    if data.decode() != 'Hello':
        c.close()
        continue

    c.send(b'Filename')
    filename = c.recv(1024).decode()

    if not os.path.exists(filename):
        c.send(b'No File')
        c.close()
        continue

    size = os.path.getsize(filename)
    c.send(size.to_bytes(4, 'big'))

    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            c.sendall(chunk)

    bye = c.recv(1024)
    if bye.decode() == 'Bye':
        pass

    c.close()
