import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print('connected by,', remotehost, remoteport)

while True:
    try:
        data = conn.recv(BUFSIZE)
    except:
        break

    if not data:
        break

    print("Recieved message: ",data.decode())

    try:
        conn.send(data)
    except:
        break

conn.close()