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
    iter_count = 0
    puzzle_board = puzzle.get_puzzle()
    stringed_rows_and_cols = make_strings(puzzle_board[0])
    guess = ''
    score = 0
    scored_guesses = ['notaguessIguess']
    points_were_scored = False

    while True:
        print('\n')
        for row in puzzle_board[0]:
            print('  '.join(row))
        print('\n')

        if iter_count != 0:
            if points_were_scored:
                print(f'"{guess}" scored you a point!')
            else:
                print(f'No points for "{guess}". Go again!')
        points_were_scored = False
        print(f'Current score: {score}')
        guess = input('Enter a word (Or type "I am done" to quit):').lower()
        if guess == 'i am done':
            return scored_guesses
        elif check_guess(guess, stringed_rows_and_cols, scored_guesses):
            score += 1
            scored_guesses.append(guess)
            points_were_scored = True
        iter_count += 1



if input('Welcome to this wordpuzzle game, press enter to start!') == '':
    print(run_game())
