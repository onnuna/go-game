import tkinter as tk
from gui.board import GoBoard
from gui.settings import Settings
from network.client import GameClient

class GoGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Go Game")
        
        self.settings = Settings(root)
        self.board = GoBoard(root, self.settings.get_board_size())
        self.board.pack()

        # Połączenie z serwerem
        self.client = None

    def connect_to_server(self):
        """
        Nawiązuje połączenie z serwerem gry.
        """
        server_ip = self.settings.get_server_ip()
        server_port = self.settings.get_server_port()
        
        self.client = GameClient(server_ip, server_port)
        self.client.connect()
        if self.client.is_connected:
            print("Połączono z serwerem")
        else:
            print("Błąd połączenia")

if __name__ == "__main__":
    root = tk.Tk()
    app = GoGameApp(root)
    root.mainloop()
