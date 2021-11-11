import abc
from ConnectNGame.src.player import Player
class HumanPlayer(Player):
    #creates human player instances

    @abc.abstractmethod
    def create_player(self, player_num, player_list) -> Player:
        globals()[self.name] = Player(player_num, player_list)
        return (globals()[self.name])

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int, player_list) -> tuple[str, str]:
        x = [t[0] for t in player_list]
        x = [t.lower() for t in x]
        y = [t[1] for t in player_list]
        while True:
            player_name = input(f"Player {player_num} enter your name: ")
            player_name_lower = player_name.lower()
            if len(player_name) == 0 or player_name == "_":
                print("Your name cannot be the empty string or whitespace")
                continue
            elif len(player_name.replace(" ", "")) == 0:
                print("Your name cannot be the empty string or whitespace")
                continue
            elif player_name_lower in x:
                print(f'You cannot use {player_name} for your name as someone else is already using it.')
                continue
            piece = input(f"Player {self.player_num} enter your piece: ")
            if len(piece.replace(" ", "")) == 0:
                print("Your piece cannot be the empty string or whitespace")
                continue
            elif len(piece) > 1:
                print(f'{piece} is not a single character. Your piece can only be a single character.')
                continue
            elif piece == self.board.blank_character:
                print('Your piece cannot be the same as the blank character.')
                continue
            elif piece in y:
                pos = y.index(piece)
                print(f'You cannot use {piece} for your piece as {self.players[pos][0]} is already using it.')
            self.name = player_name
            self.piece = piece
