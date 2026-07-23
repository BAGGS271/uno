from deck import Deck
from player import Player
import random
import time
import os
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


class Game:

    def __init__(self):
        self.players = []
        self.pickup = Deck()
        self.in_play = [self.pickup.draw()]

    # for tests to work, it was asking for name first when running the game
    # so seperated this to put it before the name request
    def show_logo(self):
        console.print("""
                [bold red]██╗   ██╗███╗   ██╗ ██████╗[/]
                [bold yellow]██║   ██║████╗  ██║██╔═══██╗[/]
                [bold green]██║   ██║██╔██╗ ██║██║   ██║[/]
                [bold blue]██║   ██║██║╚██╗██║██║   ██║[/]
                [bold red]╚██████╔╝██║ ╚████║╚██████╔╝[/]
                [bold yellow]╚═════╝ ╚═╝  ╚═══╝ ╚═════╝[/]
                """)

        time.sleep(1.5)

    def turn(self):
        self.render()

        if self.pickup == []:
            self.pickup = self.in_play
            console.print("Deck Flipped!")
            time.sleep(1.5)

        for i, player in enumerate(self.players):

            if not player.turn:
                continue

            if player.is_computer:
                console.print("\nComputer is thinking...", style="italic yellow")
                time.sleep(1)

                # store card by comp
                played_card = player.computer_play_card(self.in_play, self.pickup)

            else:
                # store card played by human
                played_card = player.no_playable_card(self.in_play, self.pickup)

            next_player = self.players[(i + 1) % len(self.players)]

            # check if card played was a draw 2
            if played_card is not None and played_card.value == "Draw Two":

                # make player pick up 2 cards
                next_player.draw_card(self.pickup)
                next_player.draw_card(self.pickup)

                console.print(
                    f"{next_player.name} picks up two cards and misses their turn!",
                    style="bold yellow",
                )
                time.sleep(1.5)
                player.turn = True
                next_player.turn = False
            else:
                player.turn = False
                next_player.turn = True

            if len(player.player_hand) == 1:
                console.print("UNO!")
                time.sleep(1.5)

            self.render()

            break

    def check_winner(self):
        for player in self.players:
            if len(player.player_hand) == 0:
                player.is_winner = True
                return True

        return False

    def setup(self, player_name="Joe"):
        # using the name passed into setup() instead of terminal
        # allows you to be able to test setting up a game without waiting for someone to type.
        self.players.append(Player(player_name, False))
        self.players.append(Player("Computer", True))
        print("Player 2 name: Computer \n")

        time.sleep(1.5)

        self.choose_first()

        self.deal()

    def play(self):
        while not self.check_winner():
            self.turn()

        self.render()

        winner = next(player for player in self.players if player.is_winner)

        console.print(f"\n🏆 {winner.name} wins!", style="bold green")

        while True:
            play_again = console.input("Play Again? Y/N: ").upper()

            if play_again == "Y":
                # Create a fresh game while keeping the same player's name.
                game = Game()
                game.setup(self.players[0].name)
                game.play()
                return

            elif play_again == "N":
                return

            else:
                continue

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
                console.print(
                    f"[bold green][ {player1.name.upper()} ][/]        "
                    + f"[bold red][ {player2.name} ][/]"
                )
            else:
                console.print(
                    f"[bold green][ {player1.name} ][/]        "
                    + f"[bold red][ {player2.name.upper()} ][/]"
                )

            time.sleep(0.4)
            os.system("clear")

        winner = random.choice(self.players)

        os.system("clear")

        print("Choosing who goes first...\n")

        if winner == player1:
            console.print(
                f"[bold green][ {player1.name.upper()} ][/]        "
                + f"[bold red][ {player2.name} ][/]"
            )
        else:
            console.print(
                f"[bold red][ {player1.name} ][/]        "
                + f"[bold green][ {player2.name.upper()} ][/]"
            )

        console.print(f"\n[bold green]{winner.name} goes first![/]")

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

        hidden_cards = [self.hidden_card() for _ in self.players[1].player_hand]

        row = []

        for card in hidden_cards:
            row.append(card)

            if len(row) == 6:
                computer_table.add_row(*row)
                row = []

        if row:
            computer_table.add_row(*row)

        board = Group(
            Panel(computer_table, title="Computer Hand", border_style="red"),
            self.center_area(),
            Panel(
                self.draw_hand(self.players[0].player_hand),
                title="Your Hand",
                border_style="green",
            ),
        )

        return board

    def card_panel(self, card):

        color_styles = {
            "Red": "red",
            "Blue": "blue",
            "Green": "green",
            "Yellow": "yellow",
        }

        color = str(card.colour)
        value = str(card.value)

        # display draw 2 cards as +2 as the text will be too long
        if card.value == "Draw Two":
            value = "+2"

        style = color_styles.get(color, "white")

        card_text = Text(f"\n{value}\n", justify="center", style=f"bold {style}")

        return Panel(card_text, width=8, height=5, border_style=style)

    def hidden_card(self):

        return Panel(
            Text("\n🂠\n", justify="center"), width=8, height=5, border_style="white"
        )

    def draw_hand(self, cards):

        table = Table.grid()

        row = []

        for card_number, card in enumerate(cards, start=1):

            labelled_card = Group(
                self.card_panel(card),
                Text(f"Card {card_number}", justify="center", style="bold white"),
            )

            row.append(labelled_card)

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
            f"{amount} pick up cards\nremaining", justify="left", style="bold white"
        )

        return Group(pile, count)

    def center_area(self):
        table = Table.grid(expand=True)

        pickup = self.pickup_pile()

        amount_in_play = self.in_play.__len__()

        discard = Group(
            self.card_panel(self.in_play[-1]),
            Text(
                f"There are {amount_in_play}\ncards in play",
                justify="left",
                style="bold white",
            ),
        )

        table.add_row(pickup, discard)

        return Panel(table, title="Table", border_style="cyan")

        console.clear()

        computer_table = Table.grid()

        hidden_cards = [self.hidden_card() for _ in self.players[1].player_hand]

        row = []

        for card in hidden_cards:

            row.append(card)

            if len(row) == 6:
                computer_table.add_row(*row)
                row = []

        if row:
            computer_table.add_row(*row)

        console.print(Panel(computer_table, title="Computer Hand", border_style="red"))

        console.print(self.center_area())

        console.print(
            Panel(
                self.draw_hand(self.players[0].player_hand),
                title="Your Hand",
                border_style="green",
            )
        )
