from ConnectNGame.src.board import Board
from ConnectNGame.src.players.human_player import HumanPlayer
from ConnectNGame.src.players.simple_ai import SimpleAI
from ConnectNGame.src.players.random_ai import RandomAi
from ConnectNGame.src.config import Config
from typing import List, Tuple, Union


class Game(object):
    def __init__(self, game_config: Config):
        self.players: List[Tuple[str, str, int]] = []
        self.board: Board = Board.build_board_from_config(game_config)
        self.Player_instants: List[Union[HumanPlayer, SimpleAI, RandomAi]] = []
        self.player_num = 0

    def play(self):
        while True:
            self.player_num += 1
            type_choice = input(f"Choose the type for Player {self.player_num}\rEnter Human or Random or Simple:")
            type_choices = {"Random": RandomAi, "Human": HumanPlayer,
                            "Simple": SimpleAI}
            self.Player_instants.append(type_choices[type_choice].create_player(self.player_num))
            type_choice = input(f"Choose the type for Player {self.player_num}\rEnter Human or Random or Simple:")
            self.Player_instants.append(type_choices[type_choice].create_player(self.player_num))

            print(self.board)
            while True:
                for x in self.Player_instants:
                    if type(x)==HumanPlayer:
                        play_col: int = self.play_check(x.name)  # type: ignore
                    else:
                        play_col=x.play(self.board)
                    self.board.drop_piece_into_column(play_col, x.piece)
                    print(self.board)
                    win = self.win_check(x.piece, x.name)
                    if win:
                        print(f"{x.name} won the game!")
                        quit()
                    if self.board.is_full():
                        print("Tie Game.")
                        quit()



    def win_check(self, piece, name) -> bool:
        board_list: List[List[str]] = self.board.contents
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

        for col in range(self.board.num_columns):
            for row in range(self.board.num_rows):
                if piece == self.board.contents[row][col]:
                    # print("{}", row, col)
                    up_vect: int = check_next(row, col, -1, 0)
                    # print("topright")
                    top_right_vect: int = check_next(row, col, 1, 1)
                    right_vect: int = check_next(row, col, 0, 1)
                    bottom_right_vect: int = check_next(row, col, -1, 1)
                    # print("!!!!",up_vect,top_right_vect,right_vect,bottom_right_vect)
                    longest_vect: int = max(up_vect, top_right_vect, right_vect, bottom_right_vect, longest_vect)
                    # print("?????",longest_vect)
        if longest_vect >= self.board.pieces_to_win:
            print(f"{name} won the game!")
            quit()

        return False

    def _play_check(self, player) -> Union[str]:
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
            x: List[str] = [t[pos] for t in self.board.contents]
            if self.board.blank_character not in x:
                print(f'You cannot play in {pos} because it is full.')
                continue
            break
        return pos