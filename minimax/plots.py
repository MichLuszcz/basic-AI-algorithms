from Player import HumanPlayer
from minimax import MinimaxPlayer
from TicTacToe import TicTacToe


def bot_v_bot():
    player_1 = MinimaxPlayer("minimax1", "bot")
    player_2 = MinimaxPlayer("minimax2", "bot")
    game = TicTacToe(player_1, player_2)
    while not game.game_over:
        # game.display_board()
        game.make_move(game.get_player_move())
        # print("_" * 15)

    game.display_board()
    if game.winner is not None:
        print("Winner:" + game.winner.name)
    else:
        print("Draw!")


def main():
    for i in range(10):
        bot_v_bot()


if __name__ == "__main__":
    main()
