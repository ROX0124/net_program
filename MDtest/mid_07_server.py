import socket
import random

BUFF_SIZE = 1024
port = 5555

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind(('', port))
print('listening...')

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)

    if random.random() < 0.25:   # 25% 확률로 드롭
        print('Packet from {} lost!'.format(addr))
        continue

    print('Packet is {} from {}'.format(data.decode(), addr))
    s_sock.sendto('ack'.encode(), addr)
