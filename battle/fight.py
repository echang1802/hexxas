
from numpy import where
from random import random as rd
#from objects.attacks import get_probs

class fight:

    def __init__(self, hexxa1, hexxa2):
        self.hexxa1 = hexxa1
        self.hexxa2 = hexxa2

    def choose_attacks(self):
        atk1 = rd()
        self.atk1 = self.hexxa1.attacks[where(self.hexxa1.attacks["probabilities"] > atk1)[0][0] + 1]
        atk2 = rd()
        self.atk2 = self.hexxa2.attacks[where(self.hexxa2.attacks["probabilities"] > atk2)[0][0] + 1]

    def resolve_fight(self):
        print("Player1 " + self.hexxa1.name + " use:")
        print(self.atk1)
        print("Player2 " + self.hexxa2.name + " use:")
        print(self.atk2)

        if self.atk1.power > self.atk2.power:
            self.hexxa2.resistance -= 1 if not self.hexxa2.shield else 0
            print("Round won by player 1")
        elif self.atk1.power < self.atk2.power:
            self.hexxa1.resistance-= 1 if not self.hexxa1.shield else 0
            print("Round won by player 2")
        else:
            print("Round drawn")

    def restore(self):
        self.hexxa1.restoreAttacks()
        self.hexxa2.restoreAttacks()
