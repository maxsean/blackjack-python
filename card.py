class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return self.suit + self.face

    @property
    def value(self):
        return self.FACES.get(self.face, self.face)
