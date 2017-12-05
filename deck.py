from card import Card
from random import shuffle

class Deck:

    def __init__(self):
        popped = []
        self.cards = [Card(face, suit) for face in FACES for suit in SUITS]
        self.shuffle()

    def __str__(self):
        s = ''
        for c in self.cards:
            s = s + str(c) + ' '
        return s

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        popped = self.cards.pop(0)
        return popped
