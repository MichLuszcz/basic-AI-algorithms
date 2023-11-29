from Move import Move
import random as rand


class Player:
    def __init__(self, name, type):
        # TODO: remove type
        self.name = name
        self.type = type

    def get_move(self, possible_moves, game):
        pass

    def __eq__(self, other):
        if self.name == other.name and self.type == other.type:
            return True
        return False

    def __str__(self):
        return self.name


class HumanPlayer(Player):
    def get_move(self, possible_moves: list[Move], game):
        good_move_found = False
        while not good_move_found:
            picked_row = (int(input("Enter row (1, 2, 3 from the top): ")) - 1)
            picked_column = (int(input("Enter column (1, 2, 3 from the left): ")) - 1)
            for valid_move in possible_moves:
                if valid_move.row == picked_row and valid_move.column == picked_column:
                    return valid_move
            print("Please select a valid move")


class RandomPlayer(Player):
    def get_move(self, possible_moves: list[Move], game):
        return rand.choice(possible_moves)
