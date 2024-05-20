from logic.move_validator import MoveValidator

class GameLogic:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.current_player = "black"
        self.validator = MoveValidator(size)

    def make_move(self, x, y):
        """
        Próbuje wykonać ruch dla aktualnego gracza na danej pozycji (x, y).
        Zwraca True, jeśli ruch jest możliwy, False w przeciwnym razie.
        """
        if self.validator.is_valid_move(self.board, x, y, self.current_player):
            self.board[x][y] = self.current_player
            self.validator.remove_captured_stones(self.board, x, y, self.get_opponent())
            self.switch_player()
            return True
        return False

    def switch_player(self):
        """
        Zmienia aktualnego gracza na przeciwnika.
        """
        self.current_player = "white" if self.current_player == "black" else "black"

    def get_opponent(self):
        """
        Zwraca przeciwnika aktualnego gracza.
        """
        return "white" if self.current_player == "black" else "black"

    def check_winner(self):
        """
        Sprawdza, czy jest zwycięzca gry.
        Zwraca kolor zwycięzcy ('black', 'white') lub None, jeśli nie ma zwycięzcy.
        """
        # Sprawdzanie poziomych linii
        for row in self.board:
            if all(cell == 'black' for cell in row):
                return 'black'
            elif all(cell == 'white' for cell in row):
                return 'white'

        # Sprawdzanie pionowych linii
        for col in range(self.size):
            if all(self.board[row][col] == 'black' for row in range(self.size)):
                return 'black'
            elif all(self.board[row][col] == 'white' for row in range(self.size)):
                return 'white'

        # Sprawdzanie przekątnych linii
        if all(self.board[i][i] == 'black' for i in range(self.size)):
            return 'black'
        elif all(self.board[i][i] == 'white' for i in range(self.size)):
            return 'white'

        if all(self.board[i][self.size - 1 - i] == 'black' for i in range(self.size)):
            return 'black'
        elif all(self.board[i][self.size - 1 - i] == 'white' for i in range(self.size)):
            return 'white'

        return None
