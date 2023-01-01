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

def run_game():
    puzzle_board = puzzle.get_puzzle()
    stringed_rows_and_cols = make_strings(puzzle_board[0])
    guess = ''

    while True:
        print('\n')
        for row in puzzle_board[0]:
            print('  '.join(row))
        print(f'{guess}')
        print('\n')
        for string in stringed_rows_and_cols:
            print(string)
        print('\n')
        guess = input('Enter a word from the board:')


if input('Welcome to this wordpuzzle game, press enter to start!') == '':
    run_game()
