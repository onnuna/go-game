import socket
import threading
from game_logic import GameLogic
from move_validator import MoveValidator

class GoServer:
    def __init__(self, host, port, board_size=5):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.game_logic = GameLogic(board_size)
        self.move_validator = MoveValidator(board_size)

    def start(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            print(f"Server started, listening on {self.host}:{self.port}")
            self.accept_clients()
        except Exception as e:
            print(f"Error starting server: {e}")

    def accept_clients(self):
        while True:
            try:
                client_socket, client_address = self.socket.accept()
                print(f"New connection from {client_address}")
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_handler.start()
                self.clients.append((client_socket, client_handler))
            except Exception as e:
                print(f"Error accepting client connection: {e}")

    def handle_client(self, client_socket):
        try:
            client_socket.sendall("Welcome to Go Game Server!\n".encode())
            while True:
                data = client_socket.recv(1024)
                if data:
                    message = data.decode().strip()
                    print(f"Received message from client: {message}")
                    if message.lower() == "exit":
                        break
                    elif message.startswith("move"):
                        parts = message.split()
                        if len(parts) == 3:
                            x, y = int(parts[1]), int(parts[2])
                            if self.game_logic.make_move(x, y):
                                self.broadcast(f"move {x} {y}\n")
                                winner = self.game_logic.check_winner()
                                if winner:
                                    self.broadcast(f"winner {winner}\n")
                                    break
                            else:
                                client_socket.sendall("invalid_move\n".encode())
                        else:
                            client_socket.sendall("invalid_command\n".encode())
                    else:
                        client_socket.sendall("invalid_command\n".encode())
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def broadcast(self, message):
        for client, _ in self.clients:
            try:
                client.sendall(message.encode())
            except Exception as e:
                print(f"Error sending message to client: {e}")
                # Jeśli wysłanie wiadomości do klienta się nie powiedzie, usuwamy go z listy klientów
                self.clients.remove((client, _))
                client.close()

if __name__ == "__main__":
    server = GoServer("localhost", 9999, board_size=5)
    server.start()
