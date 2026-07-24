from lib.game import Game
from lib.card import Card
from lib.player import Player

"""
set up a mini controlled game where player automatically a 2+ card then check
if other player picks up the 2 extra cards
"""


def test_draw_2_makes_comp_pick_up_2():
    game = Game()

    # creating 2players
    player = Player("Player", True)
    computer = Player("Computer", True)

    game.players = [player, computer]
    # put a red 5 on the table
    game.in_play = [Card(5, "Red")]

    # then draw a red 2 card
    player.player_hand = [Card("Draw Two", "Red")]
    player.turn = True

    # should be 0
    cards_before = len(computer.player_hand)

    game.turn()

    # checks player goes from 0 to 2 cards
    assert len(computer.player_hand) == cards_before + 2
