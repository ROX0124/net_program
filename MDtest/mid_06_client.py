import socket
import struct

HOST = 'localhost'
PORT = 5050

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("Connected to server.")

sock.sendall('Hello'.encode())

packet = sock.recv(12)  # 총 12바이트 수신

sender, receiver, lumi, humi, temp, air, seq = struct.unpack('>HHBBBBI', packet)

print(f"Sender:{sender}, Receiver:{receiver}, Lumi:{lumi}, Humi:{humi}, Temp:{temp}, Air:{air}, Seq:{seq}")

sock.close()
