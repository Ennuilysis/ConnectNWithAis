import random, abc

from ConnectNGame.src.players.random_ai import RandomAi

class SimpleAI(RandomAi):
    def __init__(self, player_number: int):
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        self.name: str = "SimpleAI "+str(player_number)
        self.piece: str = self.check_piece()
        self.player_num: str = player_number

    @abc.abstractmethod
    def create_player(self, player_num, player_list) -> SimpleAI:
        globals()[self.name] = SimpleAI(player_num, player_list)
        return (globals()[self.name])

    @abc.abstractmethod
    def check_piece(self, player_num: int) -> str:
        x = [t[0] for t in self.players]
        x = [t.lower() for t in x]
        y = [t[1] for t in self.players]
        while True:
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
            return piece
