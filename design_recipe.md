# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

Win Uno by being the first to empty your hand. Deal 7 cards to each player. 
Flip the top card of the deck to start. Match the top discard card by color, number, or symbol. 
Draw a card if you cannot play. 
Yell "UNO!" with one card left.

Special Action Cards:

Skip: The next player misses their turn.
Reverse: Play changes direction (clockwise to counter-clockwise).
Draw 2: The next player draws 2 cards and skips their turn.
Wild: Choose the next color to be played.
Wild Draw 4: Choose the next color and force the next player to draw 4 cards. (You can only play this if you have no matching colored card).

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

┌────────────────────────────┐
│ Player                     │
│                            │
│ - name                     │
│ - hand []                  │
│ - draw_card()              │
│ - play_card()   
│ - show_hand()
└───────────┬────────────────┘
      
┌─────────────────────────┐
│ Card                    │
│                         │
│ - color                 │
│ - value                 │
│                         │
└─────────────────────────┘

┌─────────────────────────┐
│ Deck                    │
│                         │
│ - deck[]                │
│ - draw()                │
│ - shuffle()             │
└─────────────────────────┘

┌─────────────────────────┐
│ game                    │
│                         │
│                         │
│ - start()               │
│ - setup()               │
│ - next turn()           │
└─────────────────────────┘

_Also design the interface of each class in more detail._

class Card:
    # User-facing properties:
    #   Card colour, or wild card value
    #   Card number 1 - 9 

class Deck:
    def __init__(self):
    #   Creates a deck in the form of an empty list
    #   Creates each card and appends to list

    def shuffle(self):
    #   Puts cards in list in random order
    #   Import Random

class Player:
    def __init__(self, name, is_computer):
    #   Assigns players name
    #   self.player_hand = [] -> Empty player hand
    #   self.is_computer = is_computer

    def play_card(self, card):
    #   Takes user input to select a card from self.hand[]
    #   Removes that card from the hand and appends it to the cards in play
    #   Checks card is playable
    #
    #   if computer:
    #       Get a list of playable cards
    #       Select random playable card

    def draw_card(self, pick_up_deck):
    #   Takes a card from deck class
    #   Appends that card to hand
    #   Removes card from deck

    def show_hand(self):
    #   Print hand list to terminal

class Game:
    def __init__(self):
    #   self.turn_order = [] -> cyle through list to get turns
    #   self.in_play = []
    #   self.pickup = []
    #   self.winner = False

    def setup(self):
    #   Create two decks as lists - In play + Pickup
    #   Create players and add to turn list - 1 Player 1 Computer
    #   Deal cards to players
    #   Display top card

    def start(self):
    #   Gets first player in turn order
    #   Show player hand

    def play_round(self):
    #   Get turn player or computer
    #   Player -> Call play_card func
    #   Computer -> Get random playable card
    #   Remove the card from players hand
    #   Add card to bottom of deck
    #   Check win condition -> Empty hand []

def draw(self):
    #   if no playable cards in hand
    #   draw_card(self.pick_up)

    def check_winner(self):
    #    If hand is empty list
    #    Print winner
    #   self.winner = True
    #   Call end_game()

    def end_game(self):
    #   Play again? user input = Y/N
    #   Y = setup
    #   N = exit()


## 3. Create Examples as Integration Tests

""  When initilizing the deck
    we can return the deck and see a list of all cards""

deck = Deck()
assert len(deck.deck) == 108

"" When starting up the game
    a player gets a hand containing seven cards ""

deck = Deck()
game = Game()
game.setup()
player = Player("Player_one")
assert len(player.player_hand) == 7

"" When drawing a card
    that card is removed from the deck list
    and added to player hand ""

deck = Deck()
player = Player("Player_one")
player.draw_card()
assert player.show_hand == ["one card"]

"" When playing a card
    that card is removed from the hand list 
    and added to in_play list ""

deck = Deck()
player = Player("Player_one")
player.draw_card()
player.play_card()
assert deck.in_play == ["one card]

"" When a player reaches 0 cards in hand
    the game ends"

game = Game()
game.setup()
game.start()
player.player_hand = []
game.playround()
assert game.winner == True


## 4. Create Examples as Unit Tests

"" Creating a card ""

card = Card("1", "Red")
assert card.value == "1"
assert card.colour == "Red"


## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
