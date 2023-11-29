from Player import RandomPlayer
from minimax import MinimaxPlayer
from TicTacToe import TicTacToe


def simulate_game(player_1, player_2):
    game = TicTacToe(player_1, player_2)
    while not game.game_over:
        game.make_move(game.get_player_move())

    if game.winner is not None:
        print("Winner:" + game.winner.name)
    else:
        print("Draw!")
    return game.winner


def main():
    minimax_player_1 = MinimaxPlayer("minimax1", "bot")
    minimax_player_2 = MinimaxPlayer("minimax2", "bot")
    random_player_1 = RandomPlayer("random1", "bot")
    random_player_2 = RandomPlayer("random2", "bot")
    optimal_v_optimal_winners = simulate_n_games(minimax_player_1, minimax_player_2, 50)
    minimax_vs_rand_winners = simulate_n_games(minimax_player_1, random_player_1, 200)
    rand_vs_minimax_winners = simulate_n_games(random_player_1, minimax_player_1, 500)
    rand_vs_rand_winners = simulate_n_games(random_player_1, random_player_2, 500)

    print_win_ratio(optimal_v_optimal_winners, minimax_player_1, minimax_player_2)
    print_win_ratio(minimax_vs_rand_winners, minimax_player_1, random_player_1)
    print_win_ratio(rand_vs_minimax_winners, random_player_1, minimax_player_1)
    print_win_ratio(rand_vs_rand_winners, random_player_1, random_player_2)


def count_wins(winners_list, player1, player2):
    wins1 = 0
    wins2 = 0
    for winner in winners_list:
        if winner is not None:
            if winner == player1:
                wins1 += 1
            elif winner == player2:
                wins2 += 1
    return wins1, wins2


def print_win_ratio(winners, player1, player2):
    total_games = len(winners)
    print(f"{player1} vs {player2} win ratio in {total_games} games :")
    wins = count_wins(winners, player1, player2)
    print(f"p1: {wins[0]} ({wins[0] * 100 / total_games}%) / p2: {wins[1]} ({wins[1] * 100 / total_games}%). ")


def simulate_n_games(minimax_player_1, minimax_player_2, n=10):
    optimal_v_optimal_winners = []
    for i in range(n):
        # print(i)
        winner = simulate_game(minimax_player_1, minimax_player_2)
        optimal_v_optimal_winners.append(winner)
    return optimal_v_optimal_winners


if __name__ == "__main__":
    main()
