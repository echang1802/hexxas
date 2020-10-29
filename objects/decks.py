
from random import choice
from objects.skills import skill

class deck:

    def __init__(self):
        self.cards =  []
        self.baseCards = []
        for i in range(20):
            card = choice(list(range(14))) + 1
            self.cards.append(skill(card))
            self.baseCards.append(skill(card))

    def drawCard(self, cards = 1):
        id = choice(list(range(len(self.cards))))
        card = self.cards[id]
        self.cards.pop(id)
        return card

    def restore(self):
        self.cards = []
        for card in range(20):
            self.cards.append(skill(self.baseCards[card].id))
