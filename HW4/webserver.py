import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(10)
print("웹 서버 대기 중 (포트 80)...")

while True:
    c, addr = s.accept()
    print('Connection from', addr)

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    print(req[0])

    # 요청 라인에서 파일 이름 파싱
    # "GET /index.html HTTP/1.1" → "/index.html" → "index.html"
    try:
        filename = req[0].split(' ')[1][1:]  # "/" 제거
    except:
        c.close()
        continue

    if filename == '':
        filename = 'index.html'

    # 파일 존재 여부 확인
    if os.path.exists(filename):
        # mimeType 설정 및 파일 열기
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html; charset=utf-8'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
        else:
            f = open(filename, 'rb')
            mimeType = 'application/octet-stream'

        # HTTP 헤더 전송
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: ' + mimeType + '\r\n'
        header += '\r\n'
        c.send(header.encode())

        # HTTP 바디 전송
        data = f.read()
        if filename == 'index.html':
            c.send(data.encode())
        else:
            c.send(data)
        f.close()

    else:
        # 파일이 존재하지 않는 경우 404
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += '\r\n'
        response += '<html><head><title>Not Found</title></head><body><h1>Not Found</h1></body></html>'
        c.send(response.encode())

    c.close()
