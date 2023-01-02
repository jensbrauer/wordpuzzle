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
    all_planted_words = puzzle_board[1]
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
        print(f'At least {len(all_planted_words)} words left to find.\n')
        guess = input('Enter a word (Or type "I am done" to quit):\n').lower()

        if guess == 'i am done':
            return scored_guesses, puzzle_board[1]
        elif check_guess(guess, stringed_rows_and_cols, scored_guesses):
            score += 1
            scored_guesses.append(guess)
            points_were_scored = True
            for i in range(len(all_planted_words)):
                if all_planted_words[i] == guess:
                    all_planted_words.pop(i)
                    break
        iter_count += 1


def play_again():
    while True:
        command = input('\nPlay again? (type Yes or No):\n')
        if command == 'yes':
            return True
        elif command == 'no':
            return False
        else:
            continue


print('\nWelcome to a game of wordpuzzle!')
print('\nWe will show you a 15x15 letter matrix')
print('in which we planted a set of english words.')
print('\nWords in the matrix are written verticly from top to bottom,')
print('or horizontaly from left to right.')
print('\nIf you spot a word, type it into the command line and press enter.')
print('For every word you find and enter, you score a point.')
print('\nTo end game and see a list of the words you missed,')
print('type "I am done" in the command line and hit enter.')


dumbstring = 'Astringprobablynoonewilltype'
if input('\nPress enter to start!\n') != dumbstring:
    while True:
        game_results = run_game()
        all_found_words = game_results[0]
        planted_words = game_results[1]
        missed_words = [x for x in planted_words if x not in all_found_words]
        print('\n\n\n\n____________________________GAME OVER!\n')
        print('\nNicely done!')
        print(f'You found {len(all_found_words)} words in the puzzle:')
        print(', '.join(all_found_words))
        print(f'\nUnfortunatly, you missed {len(missed_words)} words at min:')
        print(', '.join(missed_words))
        if play_again():
            continue
        else:
            print('\nThanks for playing!')
            break
