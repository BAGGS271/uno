from lib.card import Card

class Deck:
    def __init__(self):
        self.deck = []

    def fill_deck(self):
        colours = ["Red", "Yellow", "Green", "Blue"]
        for colour in colours:
            self.deck.append(Card("0", colour))
            for i in range(1, 10):
                self.deck.append(Card(i, colour))
                self.deck.append(Card(i, colour))