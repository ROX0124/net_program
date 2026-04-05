import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)
print("서버 대기 중...")

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break

        expr = data.decode().strip()
        print(f"수신: {expr}")

        try:
            expr = expr.replace(' ', '')

            # 연산자 찾기 (첫 글자 이후에서 탐색, 음수 대응)
            op_pos = -1
            for i in range(1, len(expr)):
                if expr[i] in '+-*/':
                    op_pos = i
                    break

            a = int(expr[:op_pos])
            op = expr[op_pos]
            b = int(expr[op_pos+1:])

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = round(a / b, 1)

            if op == '/':
                result_str = str(result)
            else:
                result_str = str(int(result))

        except:
            result_str = "Error"

        client.send(result_str.encode())

    print(f"{addr} 연결 종료")
    client.close()
