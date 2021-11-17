import random, abc
from abc import ABC

from ConnectNGame.src.players import player
from ConnectNGame.src.players.random_ai import RandomAi
from ConnectNGame.src.board import Board
from ConnectNGame.src.game import Game
from typing import Tuple, List
import random


class SimpleAI(RandomAi):
    # inherits the init and check piece definition from RandomAI
    @staticmethod
    def create_player(player_number: int, players, board: Board, piece: str) -> RandomAi:
        name = "SimpleAI " + str(player_number)
        globals()[name] = SimpleAI(player_number, players, board)
        # noinspection PyRedundantParentheses
        return (globals()[name])
#Where is the list of all players updated?

    # def my_fun(self):
    #     self.check_piece(...)
# chooses the piece the same way as Random Ai

    def win_check(self, piece, board) -> bool:
        board_list: List[List[str]] = board.contents
        longest_vect = 0

        def check_next(row: int, col: int, row_chng: int, col_chng: int) -> int:
            if row == -1 or col == -1:
                return 0
            try:
                next_chr: str = board_list[row][col]
            except IndexError:
                # print("problem")
                return 0
            if next_chr == piece:
                # print("{}", row, col, next_chr)
                return 1 + check_next(row + row_chng, col + col_chng, row_chng, col_chng)
            else:
                return 0

        for col in range(board.num_columns):
            for row in range(board.num_rows):
                if piece == board.contents[row][col]:
                    # print("{}", row, col)
                    up_vect: int = check_next(row, col, -1, 0)
                    # print("topright")
                    top_right_vect: int = check_next(row, col, 1, 1)
                    right_vect: int = check_next(row, col, 0, 1)
                    bottom_right_vect: int = check_next(row, col, -1, 1)
                    # print("!!!!",up_vect,top_right_vect,right_vect,bottom_right_vect)
                    longest_vect: int = max(up_vect, top_right_vect, right_vect, bottom_right_vect,
                                            longest_vect)
                    # print("?????",longest_vect)
        if longest_vect >= board.pieces_to_win:
            return True

    # chooses the piece the same way as Random Ai
    def play(self, opponent: player, board):
        col = board.num_columns
        for column in range(col):
            board.drop_piece_into_column(column, self.piece)
            win = self.win_check(self.piece, board)
            board.take_out_piece(column)
            # take piece back out
            if win:
                return column
        for column in range(board.num_columns):
            board.drop_piece_into_column(column, opponent.piece)
            win = opponent.win_check(opponent.piece, board)
            board.take_out_piece(column)
            if win:
                return column
        while True:
            pos = random.choice(range(col))
            x: List[str] = [t[pos] for t in board.contents]
            if pos > col - 1 or pos < 0:
                continue
            if board.blank_character not in x:
                continue
            break
        return pos










`







        # We want to iterate through the columns in contents
        # if there is a spot to win the simple ai will play there.
        # board.contents

        # otherwise if there is a spot to block the opponent from winning the ai will play there


        # if the top two conditions aren't met then the AI will play at the spot the same way that random AI does





#bob = SimpleAI()
#bob.check_piece()

# if there is a spot to win the simple ai will play there.
# otherwise if there is a spot to block the opponent from winning the ai will play there
# if the top two conditions aren't met then the AI will play at the spot the same way that random AI does
#



