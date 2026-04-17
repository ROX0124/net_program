import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))
    
    print("UDP 서버 시작 - 포트 12345에서 대기 중...")
    
    clients = {}
    
    while True:
        message, client_address = server_socket.recvfrom(1024)
        message = message.decode('utf-8')
        
        print(f"[{client_address}] 수신: {message}")
        
        if message.startswith("send "):
            parts = message.split(" ", 2)
            if len(parts) == 3:
                mbox_id = parts[1]
                msg_content = parts[2]
                
                clients[client_address] = mbox_id
                
                response = "OK"
                server_socket.sendto(response.encode('utf-8'), client_address)
                print(f"[{client_address}] 송신: {response}")
        
        elif message.startswith("receive "):
            mbox_id = message.split(" ")[1]
            
            found = False
            for addr, stored_id in clients.items():
                if stored_id == mbox_id and addr != client_address:
                    response = f"receive [{mbox_id}]"
                    found = True
                    break
            
            if not found:
                response = "No messages"
            
            server_socket.sendto(response.encode('utf-8'), client_address)
            print(f"[{client_address}] 송신: {response}")
        
        elif message == "quit":
            print(f"[{client_address}] 클라이언트 종료")
            if client_address in clients:
                del clients[client_address]

if __name__ == "__main__":
    udp_server()
