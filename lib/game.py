from deck import Deck
from player import Player
import random
import time
import os


class Game:
    def __init__(self):
        self.players = []
        self.pickup = Deck()
        self.in_play = [self.pickup.draw()]

    def turn(self):
        self.show_top_card()

        for player in self.players:
            if player.turn:
                if player.is_computer is False:
                    self.show_hand(player)
                player.play_card(self.in_play)
                player.turn = False
            else:
                player.turn = True

        self.check_winner()

    def check_winner(self):
        for player in self.players:
            if len(player.player_hand) == 0:
                player.is_winner = True
                print (f"{player.name} wins!")

    def setup(self):

        print("""
            ██╗   ██╗███╗   ██╗ ██████╗
            ██║   ██║████╗  ██║██╔═══██╗
            ██║   ██║██╔██╗ ██║██║   ██║
            ██║   ██║██║╚██╗██║██║   ██║
            ╚██████╔╝██║ ╚████║╚██████╔╝
            ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝
        """)

        time.sleep(2)

        self.players.append(Player(input("Player 1 name: "),False))
        self.players.append(Player("Computer",True))
        print("Player 2 name: Computer \n")
        print("[ Corban ] VS [ Computer ]")

        time.sleep(2)

        self.choose_first()

        self.deal()

        self.turn()

    def deal(self):
        for player in self.players:
            for i in range(7):
                player.draw_card(self.pickup)

#VISUALS
    def choose_first(self):
        player1 = self.players[0]
        player2 = self.players[1]

        for i in range(8):

            print("Choosing who goes first...\n")

            if i % 2 == 0:
                print(f"[ {player1.name.upper()} ]      [ {player2.name} ]")
            else:
                print(f"[ {player1.name} ]      [ {player2.name.upper()} ]")

            time.sleep(0.4)
            os.system("clear")

        winner = random.choice(self.players)

        os.system("clear")

        print("Choosing who goes first...\n")

        if winner == player1:
            print(f"[ {player1.name.upper()} ]      [ {player2.name} ]")
        else:
            print(f"[ {player1.name} ]      [ {player2.name.upper()} ]")

        print(f"\n{winner.name} goes first!")

        time.sleep(2.5)

        os.system("clear")

        winner.turn = True
        return winner

    def show_hand(self, player):

        cards = []

        for card in player.player_hand:
            cards.append([
                "+---------+",
                f"| {card.colour:<7} |",
                "|         |",
                f"| {card.value:^7} |",
                "|         |",
                f"| {card.colour:<7} |",
                "+---------+"
            ])

        print("\nYour cards:\n")

        for row in range(7):
            for card in cards:
                print(card[row], end="  ")
            print()

        for i in range(len(cards)):
            print(f"    {i+1}       ", end="")
        print()

    def show_top_card(self):
        card = self.in_play[-1]

        print("Top card:\n")

        print("+---------+")
        print(f"| {card.colour:<7} |")
        print("|         |")
        print(f"| {card.value:^7} |")
        print("|         |")
        print(f"| {card.colour:<7} |")
        print("+---------+")

