from lib.deck import Deck

def test_deck_creates_deck():
    deck = Deck()
    assert len(deck.deck) == 76