from TicTacToe import TicTacToe, Move
from Player import Player
import random as rand


class MinimaxPlayer(Player):
    def get_move(self, possible_moves: list[Move], game):
        good_move_found = False
        possible_good_moves = []

        for valid_move in possible_moves:
            next_state = game.simulate_move(valid_move)
            if self.minimax(next_state) == 1:
                possible_good_moves.append(valid_move)
        if possible_good_moves:
            return rand.choice(possible_good_moves)
        return rand.choice(possible_moves)

    def minimax(self, game: TicTacToe, depth=1000):
        best_result = 0
        if depth == 0 or game.winner is not None:
            return game.get_heuristic()
        if game.current_player is game.player_1:
            best_result = float('-inf')
            moves = game.get_possible_moves()
            for move in moves:
                next_game_state = game.simulate_move(move)
                best_result = max(best_result, self.minimax(next_game_state, depth - 1))
        else:
            best_result = float('inf')
            moves = game.get_possible_moves()
            for move in moves:
                next_game_state = game.simulate_move(move)
                best_result = min(best_result, self.minimax(next_game_state, depth - 1))
        return best_result
