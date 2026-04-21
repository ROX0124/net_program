# from socket import *
import socket
import struct
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5052))

fmt = '!HHBBBBI'

while True:
    data, addr = sock.recvfrom(1024)

    if data.decode() == 'Hello':
        sender = random.randint(1, 50000)
        receiver = random.randint(1, 50000)
        lumi = random.randint(1, 100)
        humi = random.randint(1, 100)
        temp = random.randint(1, 100)
        air = random.randint(1, 100)
        seq = random.randint(1, 100000)

        pkt = struct.pack(fmt, sender, receiver, lumi, humi, temp, air, seq)
        sock.sendto(pkt, addr)
