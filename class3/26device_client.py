# client.py
import socket

HOST = "127.0.0.1"
PORT = 5000


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server.")
    print("입력 가능: 1, 2, quit")

    try:
        while True:
            cmd = input(">> ").strip()
            if not cmd:
                continue

            client.sendall(cmd.encode())
            response = client.recv(1024).decode()
            print("Server:", response)

            if cmd.lower() == "quit":
                break

    except KeyboardInterrupt:
        print("\nClient stopped.")
    finally:
        client.close()


if __name__ == "__main__":
    main()
