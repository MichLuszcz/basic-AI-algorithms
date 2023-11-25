from Move import Move


class Player:
    def __init__(self, name, type):
        # TODO: remove type
        self.name = name
        self.type = type

    def get_move(self, possible_moves, game):
        pass


class HumanPlayer(Player):
    def get_move(self, possible_moves: list[Move], game):
        good_move_found = False
        while not good_move_found:
            picked_row = (int(input("Enter row (0, 1, 2 from the top): ")))
            print()
            picked_column = (int(input("Enter column (0, 1, 2 from the left): ")))
            for valid_move in possible_moves:
                if valid_move.row == picked_row and valid_move.column == picked_column:
                    return valid_move
            print("Please select a valid move")
