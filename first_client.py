import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = '김창현'
sock.send(name.encode())

data = sock.recv(4)
big = int.from_bytes(data, byteorder='big')
little = int.from_bytes(data, byteorder='little')
print(f"{big}")
sock.close