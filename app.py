from game import Game
from random import shuffle

game = Game()

deck = game.get_deck()
shuffle(deck)
print deck
