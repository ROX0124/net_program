import socket

BUFF_SIZE = 1024
port = 5555

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect(('localhost', port))
c_sock.settimeout(1.0)   # 1초 고정 타임아웃

for i in range(10):
    data = 'Hello, IoT'
    max_retrans = 2       # 최대 재전송 횟수
    attempts = 0          # 시도 횟수

    while attempts <= max_retrans:   # 최초 1회 + 재전송 2회 = 최대 3회
        c_sock.send(data.encode())
        print('Packet sent({}): attempt {}, Waiting up to 1 sec for ack'.format(i, attempts + 1))

        try:
            response = c_sock.recv(BUFF_SIZE)
        except socket.timeout:
            attempts += 1
            if attempts <= max_retrans:
                print('Timeout! Retransmitting... ({}/{})'.format(attempts, max_retrans))
            else:
                print('Packet {} failed after 3 attempts. Giving up.'.format(i))
        else:
            print('Response:', response.decode())
            break

c_sock.close()
