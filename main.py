import numpy as np
import random as r
from pprint import pprint

#board = np.zeros((7, 14))

deck = []



class card:
    colorDef = ["Spader", "Klöver", "Hjärter", "Ruter"]
    typeDef = ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Kneckt", "Dam", "Kung"]
    
    def __init__(self, cardType,cardColor, visible):
        self.cardType = int(cardType)
        self.cardColor = int(cardColor)
        self.visible = bool(visible)

    def __repr__(self):
        return(f"{card.colorDef[self.cardColor]} {card.typeDef[self.cardType]} ({self.visible})")
    
    @classmethod
    def resetDeck(cls):
        cls.deck = []
        for x in range(4):
            for y in range (13):
                cls.deck.append(card(y, x, False))

    @classmethod
    def genCard(cls, visible):
        cardOut = cls.deck.pop(r.randint(0,len(cls.deck)-1))
        cardOut.visible = bool(visible)
        return(cardOut)

class table:
    SIZE = 7
    def __init__(self):
        self.generate()

    def generate(self):
        card.resetDeck()
        self.table = np.empty(shape = (self.SIZE * 2, self.SIZE), dtype=object)
        for y in range (self.SIZE):
            for x in range (self.SIZE):
                if x + y <= self.SIZE-1:
                    self.table[y,x] = card.genCard(x + y == self.SIZE-1)
        self.deck = card.deck


class run:
    def __init__(self, level, table):
        self.level = int(level)
        self.table = table

        if self.level == 0:
            self.easy(self.table)
        elif self.level == 1:
            self.hard(self.table)
    
    def easy(self, table):
        run.match(table, run.drawCard.easy())

    def hard(self, table):
        run.match(table, run.drawCard.hard())

    @staticmethod
    def match(table, card):
        cols = [i for i in range (table.SIZE)]
        compare = [card]
            
        for x in cols:
            for y in range (table.SIZE * 2 - 1):
                try:
                    if type(table.table [y, x]) == type(card):
                        if table.table [y, x].visible ==  True:
                            compare.append(table[y, x])
                except:
                    pass

        print(compare)
        
    
    class drawCard:
        @staticmethod
        def easy():
            return

        @staticmethod
        def hard():
            return



#pprint (card.deck)
#print(len(card.deck))

myTable = table()

#pprint(myTable.table)
instance = run(0, myTable)
