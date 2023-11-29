from argparse import ArgumentParser

from TicTacToe import TicTacToe
from Player import HumanPlayer
from minimax import MinimaxPlayer


def main():
    parser = ArgumentParser(description="A game of Tic Tac Toe between a player and a bot or two bots")
    parser.add_argument("-p", help="Choose which player you want to be (1 or 2)", type=int, default=1)
    parser.add_argument("--auto", action="store_true", help="Play the game automatically between two bots",
                        default=False)
    args = parser.parse_args()

    player_human = HumanPlayer("Player", "human")
    minimax_1 = MinimaxPlayer("Minimax", "bot")
    minimax_2 = MinimaxPlayer("Minimax2", "bot")
    player_1 = player_human
    player_2 = minimax_1
    auto = args.auto
    if auto:
        player_1 = minimax_2
    elif args.p == 2:
        player_1 = minimax_1
        player_2 = player_human
    game = TicTacToe(player_1, player_2)
    while not game.game_over:
        game.display_board()
        print(f"Current player: {game.current_player.name}:")
        game.make_move(game.get_player_move())
        print("_" * 15)

    game.display_board()
    if game.winner is not None:
        print("Winner:" + game.winner.name)
    else:
        print("Draw!")


if __name__ == "__main__":
    main()
