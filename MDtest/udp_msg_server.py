import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))
    
    print("UDP 서버 시작 - 포트 12345에서 대기 중...")
    
    mailboxes = {}  # {mbox_id: [messages]}
    
    while True:
        message, client_address = server_socket.recvfrom(1024)
        message = message.decode('utf-8')
        
        print(f"[{client_address}] 수신: {message}")
        
        # ------------------------
        # send
        # ------------------------
        if message.startswith("send "):
            parts = message.split(" ", 2)
            if len(parts) == 3:
                mbox_id = parts[1]
                msg_content = parts[2]
                
                # 메시지 저장
                if mbox_id not in mailboxes:
                    mailboxes[mbox_id] = []
                
                mailboxes[mbox_id].append(msg_content)
                
                response = "OK"
                server_socket.sendto(response.encode('utf-8'), client_address)
                print(f"[{client_address}] 송신: {response}")
        
        # ------------------------
        # receive
        # ------------------------
        elif message.startswith("receive "):
            parts = message.split(" ")
            if len(parts) == 2:
                mbox_id = parts[1]
                
                if mbox_id in mailboxes and mailboxes[mbox_id]:
                    msg = mailboxes[mbox_id].pop(0)
                    response = f"{msg}"
                else:
                    response = "No messages"
                
                server_socket.sendto(response.encode('utf-8'), client_address)
                print(f"[{client_address}] 송신: {response}")
        
        # ------------------------
        # quit
        # ------------------------
        elif message == "quit":
            print(f"[{client_address}] 클라이언트 종료")

if __name__ == "__main__":
    udp_server()