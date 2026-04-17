import socket
import time

HOST = 'localhost'
PORT = 7000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

for i in range(3):
    sock.sendall('ping'.encode())
    send_time = time.time()

    data = sock.recv(1024).decode().strip()

    recv_time = time.time()
    rtt = recv_time - send_time

    if data == 'pong':
        print(f"Success (RTT: {rtt:.6f})")

sock.close()
