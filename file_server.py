import socket
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('File server is running...')

while True:
    conn, addr = sock.accept()

    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Hello':
        print('client:',addr ,msg.decode())
        conn.close()
        continue
    else:
        print('client:',addr ,msg.decode())
    conn.send(b'Filename')
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    filename = msg.decode()
    print('client:',addr ,filename)
    try:
        filesizze = os.path.getsize(filename)
    except:
        conn.send(b'Nofile')
        conn.close()
        continue
    else:
        fs_binary = filesizze.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)
    
    f = open(filename, 'rb')
    data = f.read()
    conn.sendall(data)

    msg = conn.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print('client:',addr ,msg.decode())
    
    f.close()
    conn.close()