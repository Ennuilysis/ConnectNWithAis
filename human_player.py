import abc
from ConnectNGame.src.player import Player
from ConnectNGame.src.board import Board

from typing import List, Union
class HumanPlayer(Player):
    #creates human player instances

    def __init__(self, player_number: int,players, board: Board):
        self.name=None
        self.piece=None
        self.player_num=player_number
        self.check_name_and_piece(player_number, players,board)

    @abc.abstractmethod
    def create_player(self, player_num, player_list,board) -> Player:
        globals()[self.name] = Player(player_num, player_list,board)
        return (globals()[self.name])

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int, player_list) -> None:
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

    def play(self, player,board) -> Union[str]:
        col = self.board.num_columns
        while True:
            try:
                pos = input(f"{player}, please enter the column you want to play in: ")
                pos = int(pos)
            except:
                print(f'{player}, column needs to be an integer. {pos} is not an integer. ')  # type: ignore
                continue
            if pos > col - 1 or pos < 0:
                print(f'Your column needs to be between 0 and {col - 1} but is actually {pos}.')  # type: ignore
                continue
            x: List[str] = [t[pos] for t in board.contents]
            if self.board.blank_character not in x:
                print(f'You cannot play in {pos} because it is full.')
                continue
            break
        return pos
