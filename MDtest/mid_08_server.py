import socket
import os
import time

BUFF_SIZE = 4096
HOST = 'localhost'
PORT = 6789

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind((HOST, PORT))
#s_sock.settimeout(3.0)
print(f"UDP File Server listening on {HOST}:{PORT}")

while True:
    # 1. 'Hello' 수신
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    if data.decode().strip() != 'Hello':
        continue
    print(f"[Server] Received 'Hello' from {addr}")

    # 2. 'Filename' 전송
    s_sock.sendto('Filename'.encode(), addr)
    print("[Server] Sent 'Filename'")

    # 3. 파일 이름 수신
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    filename = data.decode().strip()
    print(f"[Server] Received filename: '{filename}'")

    # 4. 파일 존재 여부 확인
    if not os.path.exists(filename):
        s_sock.sendto('No File'.encode(), addr)
        print(f"[Server] File '{filename}' not found. Sent 'No File'")
    else:
        with open(filename, 'rb') as f:
            file_data = f.read()

        # 최대 3회 전송 (최초 1회 + 재전송 2회), 2초 간격
        for attempt in range(1, 4):
            s_sock.sendto(file_data, addr)
            print(f"[Server] File sent (attempt {attempt}/3). Waiting for 'Bye'...")

            try:
                ack, _ = s_sock.recvfrom(BUFF_SIZE)
                if ack.decode().strip() == 'Bye':
                    print("[Server] Received 'Bye'. Transfer complete.")
                    break
            except socket.timeout:
                if attempt < 3:
                    print(f"[Server] Timeout! Retransmitting after 2 secs...")
                    time.sleep(2)
                else:
                    print("[Server] Max retransmissions reached. Giving up.")

    # 5. 'Bye' 수신 (No File의 경우)
    try:
        bye, _ = s_sock.recvfrom(BUFF_SIZE)
        if bye.decode().strip() == 'Bye':
            print("[Server] Received 'Bye'. Session ended.")
    except socket.timeout:
        pass
