# from socket import *
import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 5052)

sock.sendto(b'Hello', addr)
data, _ = sock.recvfrom(1024)

fmt = '!HHBBBBI'
sender, receiver, lumi, humi, temp, air, seq = struct.unpack(fmt, data)

print(f'Sender:{sender}, Receiver:{receiver}, Lumi:{lumi}, Humi:{humi}, Temp:{temp}, Air:{air}, Seq:{seq}')
