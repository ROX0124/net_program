import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

while True:
    expr = input("계산식 입력 (종료: q): ")

    if expr.strip() == 'q':
        print("종료합니다.")
        break

    sock.send(expr.encode())
    result = sock.recv(1024)
    print(f"결과: {result.decode()}")

sock.close()
