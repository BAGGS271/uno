from lib.deck import Deck

def test_deck_creates_deck():
    deck = Deck()
    deck.fill_deck()
    assert len(deck.deck) == 76