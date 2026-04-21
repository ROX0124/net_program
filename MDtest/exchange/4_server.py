# from socket import *
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9999))
sock.listen(1)

while True:
    c, addr = sock.accept()
    data = c.recv(1024).decode()

    temp = 0
    humid = 0
    lumi = 0

    if data == '1':
        temp = random.randint(1, 50)
    elif data == '2':
        humid = random.randint(1, 100)
    elif data == '3':
        lumi = random.randint(1, 150)

    msg = temp.to_bytes(2, 'big') + humid.to_bytes(2, 'big') + lumi.to_bytes(2, 'big')
    c.send(msg)
    c.close()
