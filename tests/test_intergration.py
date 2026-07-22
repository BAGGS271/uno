from lib.deck import Deck
from lib.game import Game
from lib.player import Player

def test_player_gets_hand():
    deck = Deck()
    deck.fill_deck()
    player = Player("Player_one")
    game = Game(player)
    game.setup()
    game.deal()
    assert len(player.player_hand) == 7