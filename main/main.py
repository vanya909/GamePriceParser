import parser


def main():
    game_title = input("Type the game's name: ")
    parser.parse(game_title=game_title)


if __name__ == '__main__':
    main()
