from TicTacToe import TicTacToe
from Player import HumanPlayer
from minimax import MinimaxPlayer


def main():
    player_1 = HumanPlayer("player", "human")
    player_2 = MinimaxPlayer("minimax", "bot")
    game = TicTacToe(player_1, player_2)
    while not game.game_over:
        game.display_board()
        game.make_move(game.get_player_move())
        print("_" * 15)

    game.display_board()
    if game.winner is not None:
        print("Winner:" + game.winner.name)
    else:
        print("Draw!")


if __name__ == "__main__":
    main()
