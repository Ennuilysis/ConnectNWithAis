from ConnectNGame.src.players.random_ai import RandomAi
from ConnectNGame.src.board import Board
from typing import Tuple, List
import random


class SimpleAI(RandomAi):
    # inherits the init and check piece definition from RandomAI
    @staticmethod
    def create_player(player_num: int, players: List[Tuple[str, str, int]], board: Board) -> RandomAi:
        name_AI = "SimpleAI " + str(player_num)
        globals()[name_AI] = SimpleAI(player_num, players, board)
        # noinspection PyRedundantParentheses
        return (globals()[name_AI])
