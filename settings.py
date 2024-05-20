import tkinter as tk

class Settings(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ustawienia Gry")
        self.board_size = tk.IntVar(value=5)
        tk.Label(self, text="Wybierz rozmiar planszy:").pack()
        tk.Radiobutton(self, text="5x5", variable=self.board_size, value=5).pack()
        tk.Radiobutton(self, text="9x9", variable=self.board_size, value=9).pack()
        tk.Radiobutton(self, text="13x13", variable=self.board_size, value=13).pack()
        tk.Radiobutton(self, text="19x19", variable=self.board_size, value=19).pack()
        tk.Button(self, text="Zastosuj", command=self.apply_settings).pack()

    def apply_settings(self):
        """
        Zastosowuje wybrane ustawienia i zamyka okno dialogowe.
        """
        self.master.board.size = self.board_size.get()
        self.master.board.create_grid()
        self.destroy()

    def get_board_size(self):
        """
        Zwraca wybrany rozmiar planszy.
        """
        return self.board_size.get()

if __name__ == "__main__":
    root = tk.Tk()
    settings = Settings(root)
    settings.mainloop()
