# from socket import *
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))

while True:
    msg = input()
    sock.send(msg.encode())
    data = sock.recv(1024)

    temp = int.from_bytes(data[0:2], 'big')
    humid = int.from_bytes(data[2:4], 'big')
    lumi = int.from_bytes(data[4:6], 'big')

    print(f'Temp={temp}, Humid={humid}, Lumi={lumi}')
