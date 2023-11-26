from TicTacToe import TicTacToe, Move
from Player import Player
import random as rand


def heuristic(game: TicTacToe, max_player):
    moves_done = game.moves_made
    if game.winner is None:
        return 0 + moves_done
    if game.winner == max_player:
        return 20 - moves_done
    return -20 + moves_done


def minimax(game: TicTacToe, max_player, depth=1000):
    # best_result = 0
    if depth == 0 or game.game_over:
        return heuristic(game, max_player)

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

        best_move = ""
        best_scenario = float('-inf')
        for valid_move in possible_moves:
            next_state = game.simulate_move(valid_move)
            best_case = minimax(next_state, self)
            if best_case > best_scenario:
                best_move = valid_move
                best_scenario = best_case
        if best_move:
            return best_move
        return rand.choice(possible_moves)
