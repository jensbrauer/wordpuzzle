from game import Game

while True:
    new_game = Game()
    while True:
        new_game.display_board()
        print(f'\nYour current score is {len(new_game.found_words)}')
        print(f'At least {new_game.how_many_left()} left to find!')
        if new_game.run_game(input('Enter a word: \n')):
            continue
        else:
            break
    if new_game.play_again():
            continue
    else:
        print('\nThanks for playing!')
        break