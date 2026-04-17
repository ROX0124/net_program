import socket
import struct
import random

HOST = 'localhost'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    request = data.decode().strip()

    temp  = 0
    humid = 0
    lumi  = 0

    if request == 'a':
        temp = random.randint(1, 50)
    elif request == 'b':
        humid = random.randint(1, 100)
    elif request == 'c':
        lumi = random.randint(1, 150)

    # 항상 6바이트: 빅 엔디언 2바이트 정수 x 3
    packet = struct.pack('>HHH', temp, humid, lumi)
    sock.sendto(packet, addr)
    print(f"Request='{request}' → Temp={temp}, Humid={humid}, Lumi={lumi} | Sent: {packet.hex()}")
