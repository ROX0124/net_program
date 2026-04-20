import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg  = input('Enter message: ')
    sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'q':
        break

    data, addr = sock.recvfrom(BUFSIZE)
    print('Server says: ', data.decode())

sock.close()