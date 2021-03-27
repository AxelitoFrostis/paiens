#import numpy as np

#board = np.zeros((7, 14))

cardType = []
cardColor = []
deck = []



for x in range (13):
    cardType.append(x)

for x in range(4):
    cardColor.append(x)


class card:
    colorDef = ["Spader", "Klöver", "Hjärter", "Ruter"]
    typeDef = ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Kneckt", "Dam", "Kung"]
    def __init__(self, cardType,cardColor):
        self.cardType = int(cardType)
        self.cardColor = int(cardColor)
    def __repr__(self):
        return(f"{card.colorDef[self.cardColor]} {card.typeDef[self.cardType]}")
        

testCard = card(1, 3)

print(testCard)

