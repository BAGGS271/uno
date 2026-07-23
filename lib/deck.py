from card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.fill_deck()
        random.shuffle(self.deck)

    def fill_deck(self):
        colours = ["Red", "Yellow", "Green", "Blue"]
        for colour in colours:
            self.deck.append(Card("0", colour))
            for i in range(1, 10):
                self.deck.append(Card(i, colour))
                self.deck.append(Card(i, colour))

            for _ in range(2):
                self.deck.append(Card("Draw Two", colour))

    def draw(self):
        if self.deck:
            return self.deck.pop()
        return None

    def __len__(self):
        return len(self.deck)
