from ConnectNGame.src.game import Game
from ConnectNGame.src.config import Config
import sys, random


def main() -> None:
    random.seed(sys.argv[1][1])
    game_config = Config(sys.argv[1][0])
    connect_n = Game(game_config)
    Game.play(connect_n)


if __name__ == '__main__':
    main()
