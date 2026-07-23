from deck import Deck
from player import Player
import random
import time
import os
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live

console = Console()

class Game:
    
    def __init__(self):
        self.players = []
        self.pickup = Deck()
        self.in_play = [self.pickup.draw()]

    def turn(self):
        self.render()

        for i, player in enumerate(self.players):

            if not player.turn:
                continue

            if player.is_computer:
                console.print("\nComputer is thinking...", style="italic yellow")
                time.sleep(1)

                player.computer_play_card(self.in_play, self.pickup)
                self.render()

            else:
                player.play_card(self.in_play)
                self.render()

            player.turn = False
            self.players[(i + 1) % len(self.players)].turn = True

            break

    def check_winner(self):
        for player in self.players:
            if len(player.player_hand) == 0:
                player.is_winner = True
                return True

        return False

    def setup(self):

        print("""
            ██╗   ██╗███╗   ██╗ ██████╗
            ██║   ██║████╗  ██║██╔═══██╗
            ██║   ██║██╔██╗ ██║██║   ██║
            ██║   ██║██║╚██╗██║██║   ██║
            ╚██████╔╝██║ ╚████║╚██████╔╝
            ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝
        """)

        time.sleep(1.5)

        self.players.append(Player(input("Player 1 name: "),False))
        self.players.append(Player("Computer",True))
        print("Player 2 name: Computer \n")

        time.sleep(1.5)

        self.choose_first()

        self.deal()

        while not self.check_winner():
            self.turn()

        self.render()

        winner = next(player for player in self.players if player.is_winner)
        console.print(f"\n🏆 {winner.name} wins!", style="bold green")

    def deal(self):
        for player in self.players:
            for i in range(7):
                player.draw_card(self.pickup)

#######VISUALS#######

    def render(self):
        console.clear()
        console.print(self.render_game())

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

        winner = player2

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
    


        card = self.in_play[-1]

        print("Top card:\n")

        print("+---------+")
        print(f"| {card.colour:<7} |")
        print("|         |")
        print(f"| {card.value:^7} |")
        print("|         |")
        print(f"| {card.colour:<7} |")
        print("+---------+")

    def render_game(self):

        computer_table = Table.grid()

        hidden_cards = [
            self.hidden_card()
            for _ in self.players[1].player_hand
        ]

        row = []

        for card in hidden_cards:
            row.append(card)

            if len(row) == 6:
                computer_table.add_row(*row)
                row = []

        if row:
            computer_table.add_row(*row)


        board = Group(
            Panel(
                computer_table,
                title="Computer Hand",
                border_style="red"
            ),

            self.center_area(),

            Panel(
                self.draw_hand(
                    self.players[0].player_hand
                ),
                title="Your Hand",
                border_style="green"
            )
        )


        return board

    def card_panel(self, card):

        color_styles = {
            "Red": "red",
            "Blue": "blue",
            "Green": "green",
            "Yellow": "yellow"
        }

        color = str(card.colour)
        value = str(card.value)

        style = color_styles.get(color, "white")

        card_text = Text(
            f"\n{value}\n",
            justify="center",
            style=f"bold {style}"
        )

        return Panel(
            card_text,
            width=8,
            height=5,
            border_style=style
        )

    def hidden_card(self):

        return Panel(
            Text(
                "\n🂠\n",
                justify="center"
            ),
            width=8,
            height=5,
            border_style="white"
        )

    def draw_hand(self, cards):

        table = Table.grid()

        row = []

        for card in cards:

            row.append(
                self.card_panel(card)
            )
            if len(row) == 6:
                table.add_row(*row)
                row = []


        if row:
            table.add_row(*row)


        return table

    def pickup_pile(self):

        pile = self.hidden_card()

        amount = self.pickup.__len__()

        count = Text(
            f"\n{amount} cards\nremaining",
            justify="center",
            style="bold white"
        )

        return Group(
            pile,
            count
        )

    def center_area(self):
        table = Table.grid(
            expand=True
        )

        pickup = self.pickup_pile()

        discard = Group(
            self.card_panel(
                self.in_play[-1]
            ),
            Text(
                "\nDiscard",
                justify="center",
                style="bold yellow"
            )
        )

        table.add_row(
            pickup,
            discard
        )

        return Panel(
            table,
            title="Table",
            border_style="cyan"
        )

  
        console.clear()

        computer_table = Table.grid()


        hidden_cards = [
            self.hidden_card()
            for _ in self.players[1].player_hand
        ]


        row = []


        for card in hidden_cards:

            row.append(card)

            if len(row) == 6:
                computer_table.add_row(*row)
                row = []


        if row:
            computer_table.add_row(*row)



        console.print(
            Panel(
                computer_table,
                title="Computer Hand",
                border_style="red"
            )
        )

        console.print(
            self.center_area()
        )

        console.print(
            Panel(
                self.draw_hand(
                    self.players[0].player_hand
                ),
                title="Your Hand",
                border_style="green"
            )
        )