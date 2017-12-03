from card import Card

class Game:
    global SUITS
    global FACE_VALUES

    SUITS = [
        "CLUB", "DIAMOND", "SPADE", "HEART"
    ]

    FACE_VALUES = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'
    ]


    def get_deck(self):

        return [Card(face, suit) for face in FACE_VALUES for suit in SUITS]
