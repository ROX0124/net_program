import socket
import struct

HOST = 'localhost'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

requests = ['a', 'b', 'c']
idx = 0

while True:
    req = requests[idx % 3]
    idx += 1

    sock.sendto(req.encode(), (HOST, PORT))

    data, _ = sock.recvfrom(1024)

    # 6바이트 빅 엔디언 언패킹
    temp, humid, lumi = struct.unpack('>HHH', data)
    print(f"Temp={temp}, Humid={humid}, Lumi={lumi}")
