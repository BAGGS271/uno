from lib.deck import Deck
from lib.player import Player

class Game:
    def __init__(self):
        player = Player("player",False)
        computer = Player("computer",True)
        player.turn = True
        self.players =[player,computer]
        self.in_play = []
        self.pickup = Deck()

    def turn(self):
        for player in self.players:
            if player.turn:
                player.play_card(self.in_play)
                player.turn = False
            else:
                player.turn = True
        self.check_winner()

    def check_winner(self):
        for player in self.players:
            if len(player.player_hand) == 0:
                player.is_winner = True
                print (f"{player.name} wins!")
        

    def setup(self):
        self.deal()

    def deal(self):
        for player in self.players:
            for i in range(7):
                player.draw_card(self.pickup)




