from game import Game

while True:
    """
    Program looping until user does not want to play any more.
    """
    new_game = Game()
    while True:
        """
        Game instance looping to ask for new input until
        user aborts gameplay.
        """
        new_game.display_board()
        new_game.show_game_status()
        if new_game.run_game(input('Enter word(or "I am done" to quit): \n')):
            continue
        else:
            new_game.game_over()
            break
    if new_game.play_again():
        continue
    else:
        print('\nThanks for playing!')
        break
