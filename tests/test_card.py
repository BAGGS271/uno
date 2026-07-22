from lib.card import Card

def test_card_creates_card():
    card = Card("1", "Red")
    assert card.value == "1"
    assert card.colour == "Red"