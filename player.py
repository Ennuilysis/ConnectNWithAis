import abc
from typing import List, Tuple
from ConnectNGame.src.board import Board


class Player(object):
    @abc.abstractmethod
    def __init__(self, player_number: int, players: List[Tuple[str, str, int]], board: Board, Test=False):
        self.name = None
        self.piece = None
        self.player_num = player_number
        if Test== True:
            ...
        self.check_name_and_piece(player_number, players, board)

    @staticmethod
    def create_player(player_num: int, players: List[Tuple[str, str, int]], board: Board, Test:bool=False) -> object:
        globals()[""] = Player(player_num, players)
        return (globals()[""])

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int, players: List[Tuple[str, str, int]], board: Board,Test=False) -> Tuple[
        str, str]:
        ...

    @abc.abstractmethod
    def play(self, board, Test:bool=False):
        ...

    def __class__(self)->object:
        return self.__class__
