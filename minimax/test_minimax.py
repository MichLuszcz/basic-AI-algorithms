from TicTacToe import TicTacToe
from Player import HumanPlayer
from minimax import MinimaxPlayer, minimax


def test_endgame_win_human():
    player_1 = HumanPlayer("player", "human")
    player_2 = MinimaxPlayer("minimax", "bot")
    state = [
        ["O", "X", "X"],
        ["", "O", ""],
        ["", "", ""]
    ]
    game = TicTacToe(player_1, player_2, state)
    game.current_player = player_1

    result_player_1 = minimax(game, player_1)
    result_player_2 = minimax(game, player_2)
    assert result_player_1 == 1 and result_player_2 == -1


def test_endgame_win_bot():
    player_1 = HumanPlayer("player", "human")
    player_2 = MinimaxPlayer("minimax", "bot")
    state = [
        ["O", "", ""],
        ["O", "O", "X"],
        ["", "", "X"]
    ]
    game = TicTacToe(player_1, player_2, state)
    game.current_player = player_2

    result_player_1 = minimax(game, player_1)
    result_player_2 = minimax(game, player_2)
    assert result_player_1 == -1
    assert result_player_2 == 1


def test_win_bot():
    player_1 = HumanPlayer("player", "human")
    player_2 = MinimaxPlayer("minimax", "bot")
    state = [
        ["O", "", "X"],
        ["O", "O", "X"],
        ["", "", "X"]
    ]
    game = TicTacToe(player_1, player_2, state)
    game.current_player = player_1

    result_player_1 = minimax(game, player_1)
    result_player_2 = minimax(game, player_2)
    assert result_player_1 == -1
    assert result_player_2 == 1


def test_human_win_longgame():
    player_1 = HumanPlayer("player", "human")
    player_2 = MinimaxPlayer("minimax", "bot")
    state = [
        ["", "X", ""],
        ["", "O", ""],
        ["", "", ""]
    ]
    game = TicTacToe(player_1, player_2, state)
    game.current_player = player_1

    result_player_1 = minimax(game, player_1)
    result_player_2 = minimax(game, player_2)
    assert result_player_1 == 1
    assert result_player_2 == -1


def test_human_win_longgame():
    player_1 = HumanPlayer("player", "human")
    player_2 = MinimaxPlayer("minimax", "bot")
    state = [
        ["X", "", ""],
        ["", "O", ""],
        ["", "", ""]
    ]
    game = TicTacToe(player_1, player_2, state)
    game.current_player = player_1

    result_player_1 = minimax(game, player_1)
    result_player_2 = minimax(game, player_2)
    assert result_player_1 == 0
    assert result_player_2 == 0

# | X | O | X |
# __________
# | O | O | X |
# __________
# | O |  |  |
#
# ??????????????
#
# | X | O | X |
# __________
# | O | O | X |
# __________
# | O | X |  |
