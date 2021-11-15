import random
from ConnectNGame.src.players.random_ai import RandomAi
from typing import List


class SimpleAI(RandomAi):
    #inherits the init and check piece definition from RandomAI
    @staticmethod
    def create_player(self, player_num, player_list,board) -> SimpleAI:
        name_AI="SimpleAI "+str(player_num)
        globals()[name_AI] = SimpleAI(player_num, player_list)
        return (globals()[name_AI])
    
