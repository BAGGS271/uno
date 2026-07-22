from lib.deck import Deck
from lib.player import Player

class Game:
    def __init__(self, player):
        self.player = player
        self.in_play = []
        self.pickup = Deck()


    def setup(self):
        pass

    def deal(self):
        for i in range(6):
            self.player.player_hand.append(i)
            self.pickup.pop(i)




