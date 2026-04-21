# from socket import *
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 80)

msg = input()
sock.sendto(msg.encode(), addr)
data, _ = sock.recvfrom(1024)
print(data.decode())

sock.close()
