import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('google.com', 80))

sock.send(b'GET / HTTP/1.1\r\n\r\n')
data = sock.recv(10000)

print(data.decode())
sock.close()