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
            card = self.player_hand.pop()
            deck.append(card)