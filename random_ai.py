from ConnectNGame.src.player import Player
from ConnectNGame.src.board import Board
from typing import List, Union, Tuple
import random


class RandomAi(Player):
    def __init__(self, player_number: int, player_list: Tuple(str, str, str), board):  # type: ignore
        self.name: str = "RandomAI " + str(player_number)
        self.piece: str = self.check_piece(player_list, board)
        self.player_num: int = player_number

    @staticmethod
    def create_player(player_num: int, player_list: Tuple(str, str, str), board) -> Player:  # type: ignore
        name_AI = "RandomAI " + str(player_num)
        globals()[name_AI] = RandomAi(player_num, player_list, board)
        return globals()[name_AI]

    def check_piece(self, player_list: int, board) -> str:  # type: ignore
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]  # type: ignore
        y = [t[1] for t in player_list]
        while True:
            pos_pop = VISIBLE_CHARACTERS.index(random.choice(VISIBLE_CHARACTERS))
            piece = VISIBLE_CHARACTERS.pop(pos_pop)
            if len(piece.replace(" ", "")) == 0:
                continue
            elif len(piece) > 1:
                continue
            elif piece == board.blank_character:
                continue
            elif piece in y:
                continue
            return piece
        
        
    def play(self, board: Board) -> Union[str]:
        col = board.num_columns
        while True:
            pos = random.choice(range(col))
            x: List[str] = [t[pos] for t in board.contents]
            if pos > col - 1 or pos < 0:
                continue
            if board.blank_character not in x:
                continue
            break
        return pos
