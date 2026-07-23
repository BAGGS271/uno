class Card:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour

    def __str__(self):
        return f"{self.colour} {self.value}"