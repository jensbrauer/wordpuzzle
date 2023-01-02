import puzzle


class Game():
    """Creates an instance of a game"""
    def __init__(self):
        self.board = puzzle.get_puzzle()

    def display_board(self):
        print(len(self.board[0]))
        for row in self.board[0]:
            print('  '.join(row))


new_game = Game()


new_game.display_board()