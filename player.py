
import abc

class Player(object):
    @abc.abstractmethod
    def __init__(self, player_number: int,players):
        self.name=None
        self.piece=None
        self.player_num=player_number
        self.check_name_and_piece(player_number, players)

    @abc.abstractmethod
    def create_player(self,player_num,player_list) -> Player:
        globals()[self.name]=Player(player_num,player_list)
        return (globals()[self.name])

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int,player_list) -> tuple[str, str]:
        ...
    @abc.abstractmethod
    def play (self,board):
        ...
