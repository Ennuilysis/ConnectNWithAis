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
    
    def check_piece(self, players: int,board) -> str:
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        y = [t[1] for t in players]
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
