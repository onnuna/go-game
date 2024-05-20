import socket
import threading

class GoClient("192.168.0.100", 9999):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print("Connected to server.")
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except Exception as e:
            print(f"Connection failed: {e}")

    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if data:
                    print(data.decode())
            except Exception as e:
                print(f"Error receiving data: {e}")
                break

    def send_message(self, message):
        try:
            self.socket.sendall(message.encode())
        except Exception as e:
            print(f"Error sending message: {e}")

    def close(self):
        try:
            self.socket.close()
        except Exception as e:
            print(f"Error closing connection: {e}")

if __name__ == "__main__":
    client = GoClient("localhost", 9999)
    client.connect()

    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break
        client.send_message(message)

    client.close()
