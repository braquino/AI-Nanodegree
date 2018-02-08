from isolation import Board
from game_agent import *
from sample_players import HumanPlayer
import timeit

player1 = MinimaxPlayer(score_fn=custom_score)
player2 = AlphaBetaPlayer(score_fn=custom_score)

board = Board(player1, player2)
board._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 57]
print(board.play(250000))

print(board.to_string())
print(board.get_legal_moves(player1))
print(board.get_legal_moves(player2))


'''
opening_book_p2 = {(0, 0): (5, 2), (1, 0): (6, 5), (2, 0): (6, 5), (3, 0): (6, 5), \
                       (0, 1): (6, 5), (1, 1): (6, 5), (2, 1): (6, 5), (3, 1): (6, 5), \
                       (0, 2): (6, 5), (1, 2): (6, 5), (2, 2): (6, 5), (3, 2): (6, 5), \
                       (0, 3): (6, 5), (1, 3): (6, 5), (2, 3): (6, 5), (3, 3): (6, 5)}
                       
for box in opening_book_p2.keys():

    new_board = board.forecast_move(box)
    move_history = []

    time_millis = lambda: 1000 * timeit.default_timer()

    legal_player_moves = new_board.get_legal_moves()
    game_copy = new_board.copy()

    move_start = time_millis()
    time_left = lambda: 50000 - (time_millis() - move_start)
    curr_move = new_board._active_player.get_move(game_copy, time_left)
    opening_book_p2[box] = curr_move

print(opening_book_p2)
'''

