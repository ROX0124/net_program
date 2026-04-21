# from socket import *
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6789))

sock.send(b'Hello')
data = sock.recv(1024)

if data.decode() == 'Filename':
    filename = input()
    sock.send(filename.encode())

    data = sock.recv(1024)
    if data.decode() == 'No File':
        print('No File')
    else:
        size = int.from_bytes(data[:4], 'big')
        rx = 0

        with open(filename, 'wb') as f:
            while rx < size:
                chunk = sock.recv(1024)
                f.write(chunk)
                rx += len(chunk)

        print('Download complete')
        sock.send(b'Bye')

sock.close()
