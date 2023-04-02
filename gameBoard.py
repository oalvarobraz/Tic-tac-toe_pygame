class Stats:
    EMPTY = " "
    Player_X = "X"
    Player_O = "O"


class GameBoard:

    def __init__(self, height: int = 3, width: int = 3):
        # Definindo as dimensões dos quadrados do tabuleiro
        self.square_size = 130
        self.line_width = 5
        self.height = height
        self.width = width
        self.board = []

        # Criando o tabuleiro vazio
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(Stats.EMPTY)
            self.board.append(row)

    def is_full(self):
        return all(self.board[i][j] != Stats.EMPTY for i in range(self.width) for j in range(self.height))

    def get_status(self, x: int, y: int):
        return self.board[x][y]

    def insert(self, x: int, y: int, player: Stats):
        if self.get_status(x, y) == Stats.EMPTY:
            self.board[x][y] = player
            return 1
        else:
            return -1

    def check_lines(self):
        for i in range(self.width):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        return Stats.EMPTY

    def check_coluns(self):
        for j in range(self.height):
            if self.board[0][j] == self.board[1][j] == self.board[2][j]:
                return self.board[0][j]
        return Stats.EMPTY

    def check_diagnals(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return Stats.EMPTY

    def has_winner(self):
        lines = self.check_lines()
        coluns = self.check_coluns()
        diagnals = self.check_diagnals()
        if lines != Stats.EMPTY:
            return lines
        elif coluns != Stats.EMPTY:
            return coluns
        elif diagnals != Stats.EMPTY:
            return diagnals
        return Stats.EMPTY

    def reset_board(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j] = Stats.EMPTY

    def check_tie(self):
        if self.is_full():
            return 1
        else:
            return 0
