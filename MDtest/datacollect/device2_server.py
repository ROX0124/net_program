import socket
import random

HOST = '127.0.0.1'
PORT = 9002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Device2 Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = data.strip()
    if data == 'Request':
        heartbeat = random.randint(40, 140)
        steps     = random.randint(2000, 6000)
        calories  = random.randint(1000, 4000)
        response  = f"{heartbeat},{steps},{calories}"
        conn.sendall(response.encode())
        print(f"Sent: {response}")
    elif data == 'quit':
        print("Received quit. Closing.")
        break

conn.close()
server.close()
