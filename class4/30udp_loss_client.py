import socket

BUFF_SIZE = 1024
port = 5555

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect(('localhost', port))

for i in range(10):
    timeout = 0.1
    data = 'Hello, IoT'

    while True:
        c_sock.send(data.encode())
        print('Packet sent({}): Waiting up to {} secs for ack'.format(i, timeout))

        c_sock.settimeout(timeout)

        try:
            data = c_sock.recv(BUFF_SIZE)
        except socket.timeout:
            timeout *= 2
            if timeout > 2.0:
                print('No ack received. Give up this packet.')
                break
        else:
            print('Response', data.decode())
            break
