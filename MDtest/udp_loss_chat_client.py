import socket
import random

port = 3333
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP Loss Chat Client 시작")

while True:
    # -----------------------------
    # 송신
    # -----------------------------
    msg = input('-> ')
    sock.sendto(msg.encode(), ('localhost', port))

    if msg == 'q':
        break

    # -----------------------------
    # ACK 기다림 (서버 응답)
    # -----------------------------
    sock.settimeout(2)

    while True:
        try:
            data, addr = sock.recvfrom(BUF_SIZE)

            # 서버 응답 출력
            print('<-', data.decode())

            # -----------------------------
            # 50% 확률로 ACK 안 보냄 (손실)
            # -----------------------------
            if random.random() > 0.5:
                sock.sendto(b'ack', addr)
                print("ACK 전송")
            else:
                print("!! ACK 손실")

            break

        except socket.timeout:
            print("서버 응답 없음, 다시 시도")
            sock.sendto(msg.encode(), ('localhost', port))

sock.close()