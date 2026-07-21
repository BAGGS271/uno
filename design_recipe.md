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
    def __init__(self, name):
    #   Assigns players name
    #   self.hand = [] -> Empty player hand

    def play_card(self):
    #   Takes user input to select a card from self.hand[]
    #   Removes that card from the hand and appends it to the cards in play
    #   Checks card is playable

    def draw_card(self):
    #   Takes a card from deck class
    #   Appends that card to hand
    #   Removes card from deck

    def show_hand(self):
    #   Print hand list to terminal

class Game:
    def __init__(self):
    #   self.turn_order = [] -> cyle through list to get turns

    def setup(self):
    #   Create two decks as lists - In play + Pickup
    #   Create players and add to turn list
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

    def check_winner(self):
    #    If hand is empty list
    #    Print winner
    #   Call end_game()

    def end_game(self):
    #   Play again? user input = Y/N
    #   Y = setup
    #   N = exit()


## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
