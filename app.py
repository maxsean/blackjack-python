from deck import Deck
from hand import Hand
from random import shuffle

message = ""
outcome = ""
score = 0
deck = []
player = []
dealer = []

SUITS = [
    "CLUB", "DIAMOND", "SPADE", "HEART"
]

FACES = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K', 'A'
]

FACE_VALUES = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10}

deck = Deck().get_deck()
shuffle(deck)
print deck
