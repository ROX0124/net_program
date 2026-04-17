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

    try:
        path = req[0].split(' ')[1]   # /exam?q=xxx 또는 /index.html
        filename = path[1:].split('?')[0]  # exam 또는 index.html
    except:
        c.close()
        continue

    # ✅ 추가된 부분 (3번 문제 핵심)
    if filename == 'exam':
        try:
            query = path.split('q=')[1]
        except:
            query = ''

        body = f"Hello, {query}"

        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type: text/plain\r\n'
        response += '\r\n'
        response += body

        c.send(response.encode())
        c.close()
        continue

    # 기존 기능 유지
    if filename == '':
        filename = 'index.html'

    if os.path.exists(filename):
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

        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: ' + mimeType + '\r\n'
        header += '\r\n'
        c.send(header.encode())

        data = f.read()
        if filename == 'index.html':
            c.send(data.encode())
        else:
            c.send(data)
        f.close()

    else:
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += '\r\n'
        response += '<html><body><h1>Not Found</h1></body></html>'
        c.send(response.encode())

    c.close()
