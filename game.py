import puzzle


class Game():
    """Creates an instance of a game"""
    def __init__(self):
        print('\nWelcome to a game of wordpuzzle!')
        print('\nWe will show you a 15x15 letter matrix')
        print('in which we planted a set of english words.')
        print('\nWords in the matrix are written verticly from top to bottom,')
        print('or horizontaly from left to right.')
        print('\nIf you spot a word, type it into the command line and press enter.')
        print('For every word you find and enter, you score a point.')
        print('\nTo end game and see a list of the words you missed,')
        print('type "I am done" in the command line and hit enter.')
        input('\nPress enter to start!\n')
        self.board = puzzle.get_puzzle()
        self.found_words = []

    def display_board(self):
        print(len(self.board[0]))
        for row in self.board[0]:
            print('  '.join(row))
            
    def run_game(self, word):
        self.found_words.append(word)
        return print(f'cool {len(self.found_words)}, fuck you')

#    def game_welcome():
#    def is_word_correct():
#    def exit_game():




