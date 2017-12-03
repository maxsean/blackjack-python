class Card:

    FACES = {"A": 1, "J": 10, "Q": 10, "K": 10}

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    @property
    def value(self):
        return self.FACES.get(self.face, self.face)
