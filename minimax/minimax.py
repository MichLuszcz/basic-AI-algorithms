from TicTacToe import TicTacToe, Move
from Player import Player
import random as rand


def minimax(game: TicTacToe, max_player, depth=1000):
    # best_result = 0
    if depth == 0 or game.game_over:
        if game.winner is None:
            return 0
        if game.winner == max_player:
            return 1
        return -1

    if game.current_player == max_player:
        best_result = float('-inf')
        moves = game.get_possible_moves()
        for move in moves:
            next_game_state = game.simulate_move(move)
            best_result = max(best_result, minimax(next_game_state, max_player, depth - 1))
        return best_result
    else:
        best_result = float('inf')
        moves = game.get_possible_moves()
        for move in moves:
            next_game_state = game.simulate_move(move)
            best_result = min(best_result, minimax(next_game_state, max_player, depth - 1))
        return best_result


class MinimaxPlayer(Player):
    def get_move(self, possible_moves: list[Move], game):
        good_move_found = False
        possible_winning_moves = []
        possible_draw_moves = []
        for valid_move in possible_moves:
            next_state = game.simulate_move(valid_move)
            best_case = minimax(next_state, self)
            if best_case == 1:
                possible_winning_moves.append(valid_move)
            if best_case == 0:
                possible_draw_moves.append(valid_move)
        if possible_winning_moves:
            return rand.choice(possible_winning_moves)
        if possible_draw_moves:
            return rand.choice(possible_draw_moves)
        return rand.choice(possible_moves)
