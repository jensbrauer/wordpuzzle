from game import Game

while True:
    new_game = Game()
    while True:
        print(new_game.board[1])
        new_game.display_board()
        print(f'Your current score is {len(new_game.found_words)}')
        print(f'At least {new_game.how_many_left()} left to find!')
        new_game.run_game(input('Enter a word: '))