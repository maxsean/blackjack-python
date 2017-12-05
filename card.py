class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return self.suit + self.face

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face
    
    @property
    def value(self):
        return self.FACES.get(self.face, self.face)
