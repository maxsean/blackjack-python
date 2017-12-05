from card import Card

class Deck:

    def get_deck(self):

        return [Card(face, suit) for face in FACES for suit in SUITS]
