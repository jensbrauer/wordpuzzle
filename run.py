from game import Game


"""
Program looping until user does not want to play any more.
Game instance looping to ask for new input until user aborts gameplay.
"""


while True:
    new_game = Game()
    while True:
        new_game.display_board()
        new_game.show_game_status()
        if new_game.run_game():
            continue
        else:
            new_game.game_over()
            break
    if new_game.play_again():
        continue
    else:
        break
