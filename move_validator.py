class MoveValidator:
    def __init__(self, size):
        self.size = size

    def is_valid_move(self, board, x, y, player):
        """
        Sprawdza, czy ruch jest dozwolony.
        - board: aktualna plansza gry
        - x, y: współrzędne ruchu
        - player: aktualny gracz ('black' lub 'white')
        """
        if not (0 <= x < self.size and 0 <= y < self.size):
            return False  # Ruch poza planszą
        if board[x][y] is not None:
            return False  # Pole już zajęte

        # Wstawienie ruchu na planszy tymczasowo do sprawdzenia
        board[x][y] = player
        if not self.has_liberties(board, x, y):
            board[x][y] = None
            return False  # Ruch powoduje samobójstwo
        board[x][y] = None

        return True

    def has_liberties(self, board, x, y):
        """
        Sprawdza, czy grupa kamieni zawiera wolne pola (liberties).
        - board: aktualna plansza gry
        - x, y: współrzędne ruchu
        """
        visited = set()
        return self._explore(board, x, y, board[x][y], visited)

    def _explore(self, board, x, y, player, visited):
        if (x, y) in visited:
            return False
        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if board[nx][ny] is None:
                    return True
                if board[nx][ny] == player:
                    if self._explore(board, nx, ny, player, visited):
                        return True
        return False

    def remove_captured_stones(self, board, x, y, opponent):
        """
        Usuwa kamienie przeciwnika, które zostały otoczone.
        - board: aktualna plansza gry
        - x, y: współrzędne ruchu
        - opponent: przeciwnik ('black' lub 'white')
        """
        visited = set()
        captured_groups = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if board[nx][ny] == opponent:
                    group = []
                    if not self.has_liberties(board, nx, ny, group, visited):
                        captured_groups.append(group)

        for group in captured_groups:
            for gx, gy in group:
                board[gx][gy] = None

    def has_liberties(self, board, x, y, group, visited):
        """
        Sprawdza, czy dana grupa kamieni ma wolne pola (liberties).
        - board: aktualna plansza gry
        - x, y: współrzędne ruchu
        - group: lista kamieni w grupie
        - visited: zbiór odwiedzonych współrzędnych
        """
        if (x, y) in visited:
            return False
        visited.add((x, y))
        group.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if board[nx][ny] is None:
                    return True
                if board[nx][ny] == board[x][y]:
                    if self.has_liberties(board, nx, ny, group, visited):
                        return True
        return False
