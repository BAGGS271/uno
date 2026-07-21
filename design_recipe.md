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
│ - title                 │
│ - start()               │
│ - setup()               │
│ - next turn()           │
└─────────────────────────┘

_Also design the interface of each class in more detail._

```python
class MusicLibrary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet


class Track:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

```

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
