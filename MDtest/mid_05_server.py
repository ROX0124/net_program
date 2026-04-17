import socket

HOST = 'localhost'
PORT = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Ping Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = data.strip()
    if data == 'ping':
        conn.sendall('pong'.encode())
    # ping이 아니면 응답하지 않음

conn.close()
server.close()
