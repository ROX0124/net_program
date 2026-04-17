import socket
import struct
import random

HOST = 'localhost'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

data = conn.recv(1024).decode().strip()
if data == 'Hello':
    sender   = random.randint(1, 50000)
    receiver = random.randint(1, 50000)
    lumi     = random.randint(1, 100)
    humi     = random.randint(1, 100)
    temp     = random.randint(1, 100)
    air      = random.randint(1, 100)
    seq      = random.randint(1, 100000)

    # 빅 엔디언: H=2바이트, B=1바이트, I=4바이트
    packet = struct.pack('>HHBBBBI', sender, receiver, lumi, humi, temp, air, seq)
    conn.sendall(packet)
    print(f"Sent: Sender={sender}, Receiver={receiver}, Lumi={lumi}, "
          f"Humi={humi}, Temp={temp}, Air={air}, Seq={seq}")

conn.close()
server.close()
