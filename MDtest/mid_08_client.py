import socket

BUFF_SIZE = 4096
HOST = 'localhost'
PORT = 6789

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect((HOST, PORT))
c_sock.settimeout(5.0)

# 1. 'Hello' 전송
c_sock.send('Hello'.encode())
print("[Client] Sent 'Hello'")

# 2. 'Filename' 수신
data = c_sock.recv(BUFF_SIZE)
print(f"[Client] Received: '{data.decode()}'")

# 3. 파일 이름 입력 후 전송
filename = input("[Client] Enter filename to request: ").strip()
c_sock.send(filename.encode())
print(f"[Client] Sent filename: '{filename}'")

# 4. 파일 또는 'No File' 수신
data = c_sock.recv(BUFF_SIZE)

if data.decode(errors='ignore').strip() == 'No File':
    print("[Client] Server response: 'No File'")
else:
    save_name = 'received_' + filename
    with open(save_name, 'wb') as f:
        f.write(data)
    print(f"[Client] File received and saved as '{save_name}' ({len(data)} bytes)")

# 5. 'Bye' 전송
c_sock.send('Bye'.encode())
print("[Client] Sent 'Bye'. Session ended.")

c_sock.close()
