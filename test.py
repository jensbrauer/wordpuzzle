from game import Game

while True:
    new_game = Game()
    while True:
        new_game.display_board()
        new_game.run_game(input('tjena'))