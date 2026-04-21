import socket
import random

port = 3333
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print("UDP Loss Chat Server 시작")

while True:
    # -----------------------------
    # 수신 처리 (50% 확률로 손실)
    # -----------------------------
    sock.settimeout(None)

    while True:
        data, addr = sock.recvfrom(BUF_SIZE)

        # 50% 확률로 ACK 안 보냄 (손실)
        if random.random() <= 0.2:
            print("!! 패킷 손실 (ACK 안보냄)")
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break

    if data.decode() == 'q':
        break

    # -----------------------------
    # 송신 처리 (재전송 포함)
    # -----------------------------
    msg = input('-> ')

    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)

        sock.settimeout(2)  # 2초 타임아웃

        try:
            ack, _ = sock.recvfrom(BUF_SIZE)

            if ack == b'ack':
                print("ACK 수신 성공")
                break

        except socket.timeout:
            print(f"재전송 {reTx+1}회")
            reTx += 1

    if msg == 'q':
        break

sock.close()