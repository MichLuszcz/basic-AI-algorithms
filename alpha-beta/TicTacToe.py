import copy as cp


class Move:

    def __init__(self, row, col, symbol: str):
        self.row = row
        self.column = col
        self.symbol = symbol


class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_move(self):
        pass


class TicTacToe:
    def __init__(self, player1=Player("player1", "human"), player2=Player("player2", "human"), state=None):
        if state is None:
            self._board = [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
        else:
            self._board = state

        self.player_1 = player1
        self.player_2 = player2
        # starting player is always Circles
        self.current_player = player1
        self.winner = None

    def get_possible_moves(self) -> list[Move]:
        symbol = ""
        if self.current_player == self.player_1:
            symbol = "O"
        else:
            symbol = "X"
        moves = []
        for line_i in range(len(self._board)):
            for space_i in range(len(self._board[line_i])):
                if self._board[line_i][space_i] == "":
                    moves.append(Move(line_i, space_i, symbol))

    def make_move(self, move: Move):
        if self._board[move.row][move.column] == "":
            self._board[move.row][move.column] = move.symbol
        else:
            raise (ValueError("Illegal move"))

    def get_board(self):
        return self._board

    def simulate_move(self, move):
        new_game = cp.deepcopy(self)
        new_game.make_move(move)
        return new_game

    def check_winner(self):
        winning_mark = ""
        # check horizontal lines
        for line in self._board:
            if line[1] == line[2] == line[0]:
                winning_mark = line[0]
        # check vertical lines
        for column_i in range(len(self._board)):
            if self._board[0][column_i] == self._board[1][column_i] == self._board[2][column_i]:
                winning_mark = self._board[0][column_i]
        # check diagonals
        if self._board[0][0] == self._board[1][1] == self._board[2][2]:
            winning_mark = self._board[0][0]
        elif self._board[0][2] == self._board[1][1] == self._board[2][0]:
            winning_mark = self._board[0][2]

        if (winning_mark == "O"):
            self.winner = self.player_1
            return
        if (winning_mark == "X"):
            self.winner = self.player_2

    def display_board(self):
        separator = "_" * 10
        print(separator)
        for line in self._board:
            print("| ", end="")
            for spot in line:
                print(spot + " | ", end="")
            print()
            print(separator)

# game = TicTacToe()
# game.display_board()
# move = Move(0, 0, "O")
# new_game = game.simulate_move(move)
# new_game.display_board()
