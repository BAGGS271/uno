import random
from rich.prompt import IntPrompt

class Player:

    def __init__(self, name, is_computer):
        self.name = name
        self.is_computer = is_computer
        self.player_hand = []
        self.turn = False
        self.is_winner = False

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.player_hand.append(card)

    def play_card(self, deck):
        choice = IntPrompt.ask("Choose card number")

        card = self.player_hand[choice - 1]

        if card in self.playable_cards(deck):
            self.player_hand.pop(choice - 1)
            deck.append(card)
        else:
            print("That card can't be played.")

    def computer_play_card(self, in_play_deck, pickup_deck):
         if len(self.playable_cards(in_play_deck)) == 0:
              self.draw_card(pickup_deck)
         else:
            card = self.playable_cards(in_play_deck)[0]
            self.player_hand.remove(card)
            in_play_deck.append(card)

    def playable_cards(self, deck):
        top_card = deck[-1]
        playable = []

        for card in self.player_hand:
            if card.colour == top_card.colour or card.value == top_card.value:
                playable.append(card)
        return playable