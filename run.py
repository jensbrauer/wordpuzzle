import puzzle

from english_words import english_words_set


def make_strings(rows):
    string_list = []
    for row in rows:
        string_list.append(''.join(row))
    for i in range(len(rows[0])):
        col_string = []
        for row in rows:
            col_string.append(row[i])
        string_list.append(''.join(col_string))
    return string_list

def check_guess(word, board, scored_guesses):
    for string in board:
        if word in string and word in english_words_set:
            if word not in scored_guesses:
                return True
    return False

def run_game():
    puzzle_board = puzzle.get_puzzle()
    stringed_rows_and_cols = make_strings(puzzle_board[0])
    guess = ''
    score = 0
    scored_guesses = ['hej']

    while True:
        print('\n')
        for row in puzzle_board[0]:
            print('  '.join(row))
        print('\n')

        if guess == scored_guesses[-1]:
            print(f'"{guess}" scored you a point!')
        else:
            print(f'No points for "{guess}"! Go again!')
        print(f'Current score: {score}')
        guess = input('Enter a word (Q/q to quit):').lower()
        if check_guess(guess, stringed_rows_and_cols, scored_guesses):
            score += 1
            scored_guesses.append(guess)



if input('Welcome to this wordpuzzle game, press enter to start!') == '':
    run_game()
