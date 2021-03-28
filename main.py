import numpy as np
import random as r
from pprint import pprint

#board = np.zeros((7, 14))

deck = []






class card:
    colorDef = ["Spader", "Klöver", "Hjärter", "Ruter"]
    typeDef = ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Kneckt", "Dam", "Kung"]
    
    def __init__(self, cardType,cardColor):
        self.cardType = int(cardType)
        self.cardColor = int(cardColor)

    def __repr__(self):
        return(f"{card.colorDef[self.cardColor]} {card.typeDef[self.cardType]}")
    
    @classmethod
    def resetDeck(cls):
        cls.deck = []
        for x in range(4):
            for y in range (13):
                cls.deck.append(card(y,x))

    @classmethod
    def genCard(cls):
        cardOut = r.choise(cls.deck)
        deck.remove(cardOut)
        return(cardOut)

class table:
    SIZE = 7
    def __init__(self):
        self.generate()

    def generate(self):
        self.table = np.zeros((SIZE, SIZE))
        for y in range (SIZE):
            for x in range (SIZE):
                if x + y <= SIZE-1:
                    pass
                else:
                    pass


card.resetDeck()



pprint (card.deck)
print(len(card.deck))

