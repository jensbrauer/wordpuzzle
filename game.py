import random
from english_words import english_words_set


class Game():
    """Creates an instance of a game"""
    def __init__(self):
        """
        Returns a msg to the terminal introducing the game.
        Initiates some variables to store gamestate.
        """
        print('\n\n\n\n\nWelcome to a game of wordpuzzle!')
        print('\nWe will show you a 15x15 letter matrix')
        print('in which we planted a set of english words.')
        print('\nWords in the matrix are written verticly from top to bottom,')
        print('or horizontaly from left to right.')
        print('\nIf you spot a word, type it up and press enter.')
        print('For every word you find and enter, you score a point.')
        print('\nTo end game and see a list of the words you missed,')
        print('type "I am done" in the command line and hit enter.')
        input('\nPress enter to start!\n')
        self.board = self.get_puzzle()
        self.found_words = []
        self.rounds_played = 0
        self.point_scored = False

    def get_puzzle(self):
        """
        Takes no parameter and returns a list.
        First list is a list of lists, each containing "rows" of the puzzle.
        Rows meaning; lists of singele letter strings.
        Second return is a list of strings with all words placed in the puzzle.
        """
        puzzle = [['-' for x in range(15)] for y in range(15)]
        words_list = []
        for word in random.sample(english_words_set, 500):
            if len(word) < 14 and word[0].islower():
                if len(word) >= 2 and "'" not in word:
                    start_pos = self.get_pos(word)
                    reference = ''
                    for i in word:
                        reference += '-'
                    check = []
                    for i in range(len(word)):
                        check.append(puzzle[start_pos[i][0]][start_pos[i][1]])
                    if ''.join(check) == reference:
                        for i in range(len(word)):
                            puzzle[start_pos[i][0]][start_pos[i][1]] = word[i]
                        words_list.append(word)
        puzzle = self.fill_blanks(puzzle)
        return puzzle, words_list

    def fill_blanks(self, list):
        """
        Takes the puzzle with planted words in as parameter.
        Returns the puzzle with blank spaces filled out with
        random letters.
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for row in range(len(list)):
            for space in range(len(list[row])):
                if list[row][space] == '-':
                    list[row][space] = random.choice(letters)
        return list

    def get_pos(self, word):
        """
        Takes string as parameter and returns a list of lists,
        each containing coordinates on the board.
        Coordinates are verticaly or horizontaly cohesive
        and represent a "space", suggested for the "word" to be placed in.
        """
        if random.choice([True, False]):
            """stacks the coordinates verticaly"""
            coord = [random.randint(0, 14 - len(word)), random.randint(0, 14)]
            coords = []
            for j in range(len(word)):
                coords.append([coord[0] + j, coord[1]])
            return coords
        else:
            """stacks the coordinates horizontaly"""
            coord = [random.randint(0, 14), random.randint(0, 14 - len(word))]
            coords = []
            for j in range(len(word)):
                coords.append([coord[0], coord[1] + j])
            return coords

    def display_board(self):
        """
        Prints a formated version of the word puzzle matrix to the terminal.
        """
        print("\n\n")
        for row in self.board[0]:
            print('  '.join(row).upper())

    def __rows_cols_str(self):
        """
        Returns a list of strings containing all rows and all columns
        of the word puzzle matrix.
        """
        string_list = []
        for row in self.board[0]:
            string_list.append(''.join(row))
        for i in range(len(self.board[0])):
            col_string = []
            for row in self.board[0]:
                col_string.append(row[i])
            string_list.append(''.join(col_string))
        return string_list

    def run_game(self):
        """
        Called every time user inputs a word into the terminal,
        taking in the string of input as parameter.
        Returns False if player wnats to exit game,
        returns true otherwise, only updating gamestate.
        """
        word = input('Enter word(or "I am done" to quit): \n')
        self.rounds_played += 1
        if word.lower() == 'i am done':
            return False
        else:
            for string in self.__rows_cols_str():
                if word in string and word in english_words_set:
                    if word not in self.found_words:
                        self.found_words.append(word)
                        self.point_scored = True
                        return True
            self.point_scored = False
            return True

    def __how_many_left(self):
        """
        Returns an integer representing how many words,
        are still to be found in the puzzle base on how many
        words were initialy planted and how many the user have found.
        """
        words_left = []
        for word in self.board[1]:
            if word not in self.found_words:
                words_left.append(word)
        return len(words_left)

    def play_again(self):
        """
        Asks the user to input 'Yes' or 'No' if wanting to play again.
        Converts the users respons to all lowercase, meaning nO yEs, yes, NO,
        are actually valid inputs. If the string is not the word yes or no
        however, the user will be prompted again until input is valid.
        Returns True or False based on input.
        """
        while True:
            command = input('\n\nPlay again? (type Yes or No):\n')
            if command.lower() == 'yes':
                return True
            elif command.lower() == 'no':
                print('\nThanks for playing!')
                return False
            else:
                print('\n\nOnly "Yes" or "No" are valid inputs.')
                continue

    def show_game_status(self):
        """
        Prints a msg to the terminal updating the user on the current
        gamestate (I e, if the last guess was awarded a point,
        hwo many words have been found, how many are left to find)
        """
        if self.rounds_played == 0:
            print(f'\nYour current score is {len(self.found_words)}')
            print(f'At least {self.__how_many_left()} words left to find!')
        else:
            if self.point_scored:
                print('\nNice Going! You found a word!')
            else:
                print('\nSorry, no points for that one!')
            print(f'\nYour current score is {len(self.found_words)}.')
            if self.__how_many_left() == 1:
                print(f'At least {self.__how_many_left()} word left to find!')
            elif self.__how_many_left() == 0:
                print("We don't know if there are any words left to find?")
            else:
                print(f'At least {self.__how_many_left()} words left to find!')

    def game_over(self):
        """
        Prints a msg to the terminal that the game is over and
        thanking the player for the game.
        Also printing the number of words the user found,
        as well as the ones that the user did'nt find.
        """
        print('\n\n\n\n ----------------------------GAME OVER')
        print('\nNice work!')
        not_found = [x for x in self.board[1] if x not in self.found_words]
        if len(self.found_words) == 1:
            print(f'You found {len(self.found_words)} word:')
            print(''.join(self.found_words))
            print(f'\nSorry to say, you missed {len(not_found)}:')
            print(', '.join(not_found))
        elif len(self.found_words) == 0:
            print("Even though you didn't find a single word.")
            print(f'\nSorry to say, you missed {len(not_found)}:')
            print(', '.join(not_found))
        else:
            if len(not_found) == 0:
                print(f'You found {len(self.found_words)} words:')
                print(', '.join(self.found_words))
                print('\nWe do not know of any word you missed!')
            else:
                print(f'You found {len(self.found_words)} words:')
                print(', '.join(self.found_words))
                print(f'\nSorry to say, you missed {len(not_found)}:')
                print(', '.join(not_found))
