import socket
import random

HOST = '127.0.0.1'
PORT = 9001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Device1 Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = data.strip()
    if data == 'Request':
        temp  = random.randint(0, 40)
        humid = random.randint(0, 100)
        ilum  = random.randint(70, 150)
        response = f"{temp},{humid},{ilum}"
        conn.sendall(response.encode())
        print(f"Sent: {response}")
    elif data == 'quit':
        print("Received quit. Closing.")
        break

conn.close()
server.close()
