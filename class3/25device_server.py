# server.py
import socket
import threading
import random
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000


def now_str():
    return datetime.now().strftime("%a %b %d %H:%M:%S %Y")


def make_device1_data():
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    illum = random.randint(70, 150)
    msg = f"{now_str()}: Device1: Temp={temp}, Humid={humid}, Ilum={illum}"
    return msg


def make_device2_data():
    heart = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    msg = f"{now_str()}: Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}"
    return msg


def handle_client(conn, addr):
    print(f"[CONNECT] {addr} connected")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            cmd = data.decode().strip().lower()
            print(f"[RECV] {addr}: {cmd}")

            if cmd == "1":
                response = make_device1_data()
            elif cmd == "2":
                response = make_device2_data()
            elif cmd == "quit":
                response = "Server closing connection..."
                conn.sendall(response.encode())
                break
            else:
                response = "Invalid command. Use 1, 2, or quit."

            conn.sendall(response.encode())

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")
    finally:
        conn.close()
        print(f"[DISCONNECT] {addr} disconnected")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[START] TCP server running on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("\n[STOP] Server shutting down...")
    finally:
        server.close()


if __name__ == "__main__":
    main()
