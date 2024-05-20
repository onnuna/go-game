import tkinter as tk
from logic.game_logic import GameLogic

class GoBoard(tk.Frame):
    def __init__(self, master, size):
        super().__init__(master)
        self.size = size
        self.logic = GameLogic(size)
        self.canvas = tk.Canvas(self, width=600, height=600, bg='beige')
        self.canvas.pack()
        self.create_grid()
        self.canvas.bind("<Button-1>", self.on_click)

    def create_grid(self):
        """
        Tworzy siatkę na planszy.
        """
        for i in range(self.size):
            self.canvas.create_line(20, 20 + i * 40, 20 + (self.size - 1) * 40, 20 + i * 40)
            self.canvas.create_line(20 + i * 40, 20, 20 + i * 40, 20 + (self.size - 1) * 40)

    def on_click(self, event):
        """
        Obsługuje kliknięcia na planszy.
        """
        x = (event.x - 20) // 40
        y = (event.y - 20) // 40
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.logic.make_move(x, y):
                self.draw_stone(x, y)

    def draw_stone(self, x, y):
        """
        Rysuje kamień na planszy.
        """
        color = 'black' if self.logic.current_player == 'white' else 'white'
        self.canvas.create_oval(
            20 + x * 40 - 15, 20 + y * 40 - 15,
            20 + x * 40 + 15, 20 + y * 40 + 15,
            fill=color
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Go Game")
    
    def on_size_selected(size):
        for widget in root.winfo_children():
            widget.destroy()
        board = GoBoard(root, size)
        board.pack()
    
    size_var = tk.IntVar(value=5)
    
    size_frame = tk.Frame(root)
    size_frame.pack()
    
    tk.Label(size_frame, text="Rozmiar planszy:").pack(side=tk.LEFT)
    tk.OptionMenu(size_frame, size_var, 5, 9, 13, 19).pack(side=tk.LEFT)
    tk.Button(size_frame, text="Zatwierdź", command=lambda: on_size_selected(size_var.get())).pack(side=tk.LEFT)
    
    on_size_selected(size_var.get())
    
    root.mainloop()
