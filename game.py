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
        print('\nIf you spot a word, type it up and press enter.')
        print('For every word you find and enter, you score a point.')
        print('\nTo end game and see a list of the words you missed,')
        print('type "I am done" in the command line and hit enter.')
        input('\nPress enter to start!\n')
        self.board = puzzle.get_puzzle()
        self.found_words = []
        self.rounds_played = 0
        self.point_scored = False

    def display_board(self):
        print("\n\n")
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
        self.rounds_played += 1
        if word.lower() == 'i am done':
            return False
        else:
            for string in self.is_word_correct():
                if word in string and word in english_words_set:
                    if word not in self.found_words:
                        self.found_words.append(word)
                        self.point_scored = True
                        return True
            self.point_scored = False
            return True

    def how_many_left(self):
        words_left = []
        for word in self.board[1]:
            if word not in self.found_words:
                words_left.append(word)
        return len(words_left)

    def play_again(self):
        while True:
            command = input('\n\nPlay again? (type Yes or No):\n')
            if command == 'yes':
                return True
            elif command == 'no':
                return False
            else:
                print('\n\nOnly "Yes" or "No" are valid inputs.')
                continue

    def show_game_status(self):
        if self.rounds_played == 0:
            print(f'\nYour current score is {len(self.found_words)}')
            print(f'At least {self.how_many_left()} words left to find!')
        else:
            if self.point_scored:
                print('\nNice Going! You found a word!')
            else:
                print('\nSorry, no points for that one!')
            print(f'\nYour current score is {len(self.found_words)}.')
            if self.how_many_left() == 1:
                print(f'At least {self.how_many_left()} word left to find!')
            elif self.how_many_left() == 0:
                print("We don't know if there are any words left to find?")
            else:
                print(f'At least {self.how_many_left()} words left to find!')

    def game_over(self):
        print('\n\n\n\n ----------------------------GAME OVER')
        print('\nNice work!')
        not_found = [x for x in self.board[1] if x not in self.found_words]
        if len(self.found_words) == 1:
            print(f'You found {len(self.found_words)} word!:')
            print(''.join(self.found_words))
            print(f'Sorry to say, you missed {len(not_found)}:')
            print(', '.join(not_found))
        elif len(self.found_words) == 0:
            print("Even though you didn't find a single word!")
            print(f'Sorry to say, you missed {len(not_found)}:')
            print(', '.join(not_found))
        else:
            if len(not_found) == 0:
                print(f'You found {len(self.found_words)} words!')
                print(', '.join(self.found_words))
                print('We do not know of any word you missed!')
            else:
                print(f'You found {len(self.found_words)} words!:')
                print(', '.join(self.found_words))
                print(f'Sorry to say, you missed {len(not_found)}:')
                print(', '.join(not_found))
