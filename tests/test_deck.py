from lib.deck import Deck


def test_deck_creates_deck():
    deck = Deck()
    assert len(deck.deck) == 84


def test_deck_contains_eight_draw_two_cards():
    deck = Deck()
    draw_two_cards = []

    for card in deck.deck:
        if card.value == "Draw Two":
            draw_two_cards.append(card)

    assert len(draw_two_cards) == 8
