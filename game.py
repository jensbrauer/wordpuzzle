import puzzle
from english_words import english_words_set

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
    
    def is_word_correct(self):
        string_list = []
        for row in self.board[0]:
            string_list.append(''.join(row))
        for i in range(len(self.board[0])):
            col_string = []
            for row in self.board[0]:
                col_string.append(row[i])
            string_list.append(''.join(col_string))
        return string_list

    def run_game(self, word):
        for string in self.is_word_correct():
            if word in string and word in english_words_set:
                if word not in self.found_words:
                    self.found_words.append(word)
                    break
    
    def how_many_left(self):
        words_left = []
        for word in self.board[1]:
            if word not in self.found_words:
                words_left.append(word)
        return len(words_left)

#    def game_welcome():
#    def exit_game():




