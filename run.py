import puzzle

def run_game():
    puzzle_board = puzzle.get_puzzle()
    while True:
        for row in puzzle_board[0]:
            print('  '.join(row))
        input('Enter a word from the board:')


if input('Welcome to this wordpuzzle game, press enter to start!') == '':
    run_game()
