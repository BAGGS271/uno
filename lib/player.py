from rich.prompt import IntPrompt
from rich.console import Console
import time

console = Console()


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

        while True:
            choice = IntPrompt.ask("Choose card number: ")
            if choice == 0:
                raise SystemExit
            if choice < 1 or choice > len(self.player_hand):
                console.print("That card does not exist!", style="bold red")
                continue

            card = self.player_hand[choice - 1]

            if card in self.playable_cards(deck):
                self.player_hand.pop(choice - 1)
                deck.append(card)
                # return the card so the game detects the draw two
                return card
            else:
                console.print("You cannot play that card!", style="bold red")

    def no_playable_card(self, in_play_deck, pickup_deck):
        playable = self.playable_cards(in_play_deck)
        if playable == []:
            console.print(
                "You have no playable cards, one has been drawn!", style="bold green"
            )
            time.sleep(1.5)
            self.draw_card(pickup_deck)

            # no card played
            return None
        else:
            # pass selected card back to Game.turn()
            return self.play_card(in_play_deck)

    def computer_play_card(self, in_play_deck, pickup_deck):
        if len(self.playable_cards(in_play_deck)) == 0:
            console.print("Computer has no playable cards, one has been drawn!",
                style="bold green",
            )
            time.sleep(1.5)
            self.draw_card(pickup_deck)
            return None
        else:
            card = self.playable_cards(in_play_deck)[0]
            self.player_hand.remove(card)
            in_play_deck.append(card)
            # same as playcard, return the card so the game detects draw 2
            return card

    def playable_cards(self, deck):
        top_card = deck[-1]
        playable = []

        for card in self.player_hand:
            if card.colour == top_card.colour or card.value == top_card.value:
                playable.append(card)
            if card.value == "Draw Four":
                playable.append(card)
            if top_card.value == "Draw Four":
                playable.append(card)
        return playable
