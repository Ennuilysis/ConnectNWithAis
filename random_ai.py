from ConnectNGame.src.players.human_player import HumanPlayer

class RandomAi(HumanPlayer):
    VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
    def __init__(self, player_number: int):
        self.name: str = "RandomAI "+str(player_number)
        self.piece: str = piece
        self.player_num: str = player_number

    def create_player(self, player_num) -> Player:
        self.check_name_and_piece_human(player_num)
        self.players.append((player_name, player_piece, player_num))
        globals()[player_name] = HumanPlayer(player_name, player_piece, player_num)
        self.Player_instants.append(globals()[player_name])

    @abc.abstractmethod
    def check_name_and_piece_human(self, player_num: int) -> tuple[str, str]:
        x = [t[0] for t in self.players]
        x = [t.lower() for t in x]
        y = [t[1] for t in self.players]
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