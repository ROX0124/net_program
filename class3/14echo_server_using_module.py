import class3.MyTCPServer as my

port = 2500
BUFSIZE = 1024

sock = my.TCPServer(port)
conn, addr = sock.accept()
print('Connected by', addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    
    print("Recieved message: ", data.decode())
    conn.sendall(data)
    
conn.close()
