
from numpy import array
from random import choice, choices
from objects.elements import element
from objects.attacks import attack

def get_basic_stats(id):
    hexxas = {
        1 : {
            "name" : "hexxa1",
            "element" : 1,
            "resistance" : 1,
            "attacks" : [1,2,3,4,5,6,7,8,9,10]
        }
    }
    return hexxas[id]

class hexxas:

    def __init__(self, id):
        basicStats = get_basic_stats(id)
        self.id = id
        self.name = basicStats["name"]
        self.element = element(basicStats["element"])
        self.create_hexxa(basicStats)
        self.exerience = {
            "experience" : 0,
            "battles" : 0,
            "battlesWon" : 0,
            "battlesLost" : 0,
            "fightsWon" : 0,
            "fightsLost" : 0
        }
        # Battles states variables
        self.shield = False

    def get_probs(self):
        totalFrequency = 0
        probs = array([0,0,0,0,0,0])
        for atk in range(6):
            totalFrequency += self.attacks[atk + 1].frequency
            probs[atk] = self.attacks[atk + 1].frequency
        self.attacks["probabilities"] = probs.cumsum() / totalFrequency

    def create_hexxa(self, basicStats):
        # Base stats
        self.resistance = basicStats["resistance"]
        attacks = choices(basicStats["attacks"], k = 6)
        self.attacks = {
            1 : attack(attacks[0]),
            2 : attack(attacks[1]),
            3 : attack(attacks[2]),
            4 : attack(attacks[3]),
            5 : attack(attacks[4]),
            6 : attack(attacks[5])
        }

        # Individual stats
        updatedStats = choices(["res","atk_1_pow","atk_1_fre","atk_2_pow","atk_2_fre","atk_3_pow","atk_3_fre","atk_4_pow","atk_4_fre","atk_5_pow","atk_5_fre","atk_6_pow","atk_6_fre"], k = 10)
        for stat in updatedStats:
            if "res" in stat:
                self.resistance  += 1
            elif "pow" in stat:
                atkNumber = int(stat.split("_")[1])
                self.attacks[atkNumber].power += 100
                self.attacks[atkNumber].basePower += 100
            else:
                atkNumber = int(stat.split("_")[1])
                self.attacks[atkNumber].frequency += 1
                self.attacks[atkNumber].baseFrequency += 1

        # get attacks probabilities
        self.get_probs()

    def restoreAttacks(self):
        for atk in range(6):
            self.attacks[atk].restore()
        self.get_probs()

    def __str__(self):
        aux = self.name + "\nElement: " + self.element.name + "\nResistance: " + str(self.resistance) + "\nAttacks:"
        for atk in range(6):
            aux += "\n" + str(self.attacks[atk])
        return aux

    def __repr__(self):
        aux = self.name + "\nElement: " + self.element.name + "\nResistance: " + str(self.resistance) + "\nAttacks:"
        for atk in range(6):
            aux += "\n" + str(self.attacks[atk + 1])
        return aux
