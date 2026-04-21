# from socket import *
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 7000)

for _ in range(3):
    t1 = time.time()
    sock.sendto(b'ping', addr)
    data, _ = sock.recvfrom(1024)
    t2 = time.time()

    if data.decode() == 'pong':
        print(f'Success (RTT: {t2 - t1:.6f})')

sock.close()
