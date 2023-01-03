from game import Game

while True:
    new_game = Game()
    while True:
        new_game.display_board()
        new_game.show_game_status()
        if new_game.run_game(input('Enter a word: \n')):
            continue
        else:
            new_game.game_over()
            break
    if new_game.play_again():
            continue
    else:
        print('\nThanks for playing!')
        break