from deck import Deck
from hand import Hand
import builtins

def deal():
    if builtins.in_play == True:
        builtins.message = "Here is the new hand"
        builtins.score -= 1
        builtins.deck = Deck()
        builtins.player = Hand()
        builtins.dealer = Hand()
        builtins.player.add_card(builtins.deck.deal_card())
        builtins.dealer.add_card(builtins.deck.deal_card())
        builtins.player.add_card(builtins.deck.deal_card())
        builtins.dealer.add_card(builtins.deck.deal_card())
    if builtins.in_play == False:
        builtins.deck = Deck()
        builtins.player = Hand()
        builtins.dealer = Hand()
        builtins.player.add_card(builtins.deck.deal_card())
        builtins.dealer.add_card(builtins.deck.deal_card())
        builtins.player.add_card(builtins.deck.deal_card())
        builtins.dealer.add_card(builtins.deck.deal_card())
        builtins.message = "New Hand. Hit or Stand?"
    builtins.in_play = True
    builtins.outcome = "Dealer: " + str(builtins.dealer.get_value()) + "  Player: " + str(builtins.player.get_value())

def hit():
    if builtins.in_play == True:
        builtins.player.add_card(builtins.deck.deal_card())
        builtins.message = "Hit or Stand?"
        if builtins.player.get_value() > 21:
            builtins.in_play = False
            builtins.message = "Player busted! You Lose! "
            builtins.score -= 1
        builtins.outcome = "Dealer: " + str(builtins.dealer.get_value()) + "  Player: " + str(builtins.player.get_value())

def stand():
    if builtins.in_play == False:
        builtins.message = "The hand is already over. Deal again"
    else:
        while builtins.dealer.get_value() < 17:
            builtins.dealer.add_card(builtins.deck.deal_card())
        if builtins.dealer.get_value() > 21:
            builtins.message = "Dealer busted. You win! "
            builtins.score += 1
            builtins.in_play = False

        elif builtins.dealer.get_value() > builtins.player.get_value():
            builtins.message = "Dealer wins! "
            builtins.score -= 1
            builtins.in_play = False

        elif builtins.dealer.get_value() == builtins.player.get_value():
            builtins.message = "Tie! Dealer wins! "
            builtins.score -= 1
            builtins.in_play = False

        elif builtins.dealer.get_value() < builtins.player.get_value():
            builtins.message = "You win! "
            builtins.score += 1
            builtins.in_play = False

        builtins.outcome = "Dealer: " + str(builtins.dealer.get_value()) + "  Player: " + str(builtins.player.get_value())

print "Welcome to Blackjack Python"
deal()
print builtins.outcome
user_input = raw_input(builtins.message + " ")

while builtins.in_play == True:
    if user_input == "Hit":
        hit()
        print builtins.outcome
        user_input = raw_input(builtins.message + " ")
    elif user_input == "Stand":
        stand()
        print builtins.outcome
        print builtins.message
