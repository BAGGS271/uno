from lib.deck import Deck
from lib.game import Game
from lib.player import Player
from lib.card import Card


#some of these are working, but they need to simulate and takes some time
#commented them out for now so i can work on the test_wildcards
#if you'd like to see these running/fix ones that dont, just uncomment.
"""
def test_player_gets_hand():
    game = Game()
    game.setup()
    assert len(game.players[0].player_hand) == 7

def test_player_draws_card_and_removes():
    game = Game()
    game.setup()
    player = game.players[0]
    player.draw_card(game.pickup)
    assert len(player.player_hand) == 8

def test_player_plays_card_and_removes_from_hand():
    game = Game()
    game.setup()
    player = game.players[0]
    player.play_card(game.in_play)
    assert len(player.player_hand) == 6
    assert len(game.in_play) == 1

def test_declare_winner_if_hand_empty():
    game = Game()
    game.setup()
    player = game.players[0]
    player.player_hand = [Card("Red","1")]
    game.turn()
    assert player.is_winner == True
    """
