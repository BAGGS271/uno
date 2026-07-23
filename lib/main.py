from game import Game

game = Game()

game.show_logo()

player_name = input("Player 1 name: ")

game.setup(player_name)

game.play()
