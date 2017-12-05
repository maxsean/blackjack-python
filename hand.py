class Hand:

    def __init__(self):
        self.player_hand = []

    def __str__(self):
        s = ''
        for card in self.player_hand:
            s = s + str(card) + ' '
        return s

    def add_card(self, card):
        self.player_hand.append(card)
        return self.player_hand

    def get_value(self):
        value = 0
        for card in self.player_hand:
            face = card.get_face()
            value = value + FACE_VALUES[face]
        for card in self.player_hand:
            face = card.get_face()
            if face == 'A' and value <= 11:
                value += 10
        return value
