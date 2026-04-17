import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 12345)
    
    print("UDP 클라이언트 시작")
    print("명령어: send [mboxID] message / receive [mboxID] / quit")
    
    while True:
        message = input("\n입력: ")
        
        if not message:
            continue
        
        client_socket.sendto(message.encode('utf-8'), server_address)
        print(f"서버로 전송: {message}")
        
        if message == "quit":
            print("프로그램 종료")
            break
        
        response, _ = client_socket.recvfrom(1024)
        response = response.decode('utf-8')
        print(f"서버 응답: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    udp_client()
