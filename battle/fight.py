
from numpy import where
from random import random as rd
#from objects.attacks import get_probs

class fight:

    def __init__(self, hexxa1, hexxa2):
        self.attacks1 = hexxa1.attacks
        self.attacks2 = hexxa2.attacks

    def choose_attacks(self):
        atk1 = rd()
        self.atk1 = self.attacks1[where(self.attacks1["probabilities"] > atk1)[0][0] + 1]
        atk2 = rd()
        self.atk2 = self.attacks2[where(self.attacks2["probabilities"] > atk2)[0][0] + 1]

    def resolve_fight(self, hexxa1, hexxa2):
        print(hexxa1.name + " Usa:")
        print(self.atk1.name)
        print(hexxa2.name + " Usa:")
        print(self.atk2.name)

        if self.atk1.power > self.atk2.power:
            hexxa2.resistance -= 1
            print("Round won by hexxa1")
        elif self.atk1.power < self.atk2.power:
            hexxa1.resistance-= 1
            print("Round won by hexxa2")
        else:
            print("Round drawn")
