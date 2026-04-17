import socket
import random

port = 3333
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', port))

while True:
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
    if data.decode() == 'q':
        break

    msg = input('->  ')
    
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUF_SIZE)
        except socket.timeout:
            reTx += 1
            continue
sock.close()