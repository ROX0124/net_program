import socket
import time

D1_HOST, D1_PORT = '127.0.0.1', 9001
D2_HOST, D2_PORT = '127.0.0.1', 9002
FILE_NAME = 'data.txt'

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect((D1_HOST, D1_PORT))
print("Device1 connected.")

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((D2_HOST, D2_PORT))
print("Device2 connected.")

with open(FILE_NAME, 'a') as f:
    while True:
        user_input = input("입력 (1 / 2 / q): ").strip()

        if user_input == '1':
            sock1.sendall('Request'.encode())
            data = sock1.recv(1024).decode().strip()
            temp, humid, ilum = data.split(',')
            timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
            line = f"{timestamp}: Device1: Temp={temp}, Humid={humid}, Ilum={ilum}\n"
            f.write(line)
            f.flush()
            print(line.strip())

        elif user_input == '2':
            sock2.sendall('Request'.encode())
            data = sock2.recv(1024).decode().strip()
            heartbeat, steps, calories = data.split(',')
            timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
            line = f"{timestamp}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={calories}\n"
            f.write(line)
            f.flush()
            print(line.strip())

        elif user_input == 'q':
            sock1.sendall('quit'.encode())
            sock2.sendall('quit'.encode())
            print("quit 전송 완료. 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 1, 2, quit 중 하나를 입력하세요.")

sock1.close()
sock2.close()
