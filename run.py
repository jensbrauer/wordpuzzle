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
    scored_guesses = []
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
            return scored_guesses, puzzle_board[2]
        elif check_guess(guess, stringed_rows_and_cols, scored_guesses):
            score += 1
            scored_guesses.append(guess)
            points_were_scored = True
        iter_count += 1

def play_again():
    while True:
        command = input('Play again? (type Yes or No):')
        if command == 'yes':
            return True
        elif command == 'no':
            return False
        else:
            continue

if input('Welcome to this wordpuzzle game, press enter to start!') != 'Just about anything that can be typed, you know?':
    while True:
        game_results = run_game()
        all_found_words = game_results[0]
        planted_words = game_results[1]
        found_planted_words = [x for x in all_found_words if x in planted_words]
        missed_planted_words = [x for x in planted_words if x not in all_found_words]
        print('\n')
        print('\n')
        print('\n')
        print('\n-____________________________GAME OVER!')
        print('')
        print('\nNicely done!')
        print(f'You found a total of {len(all_found_words)} words in the puzzle:')
        print(', '.join(all_found_words))
        print(f'\nYou found {len(found_planted_words)} of the words we planted:')
        print(', '.join(found_planted_words))
        print(f'\nUnfortunatly, You missed {len(missed_planted_words)} of the words we planted:')
        print(', '.join(missed_planted_words))
        if play_again():
            continue
        else:
            break

