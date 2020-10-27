
from objects.elements import element

def get_probs(attacks):
    from numpy import array
    totalFrequency = 0
    probs = array([0,0,0,0,0,0])
    for atk in attacks.keys():
        totalFrequency += attacks[atk].frequency
        probs[atk - 1] = attacks[atk].frequency
    probs = probs.cumsum() / totalFrequency
    return probs

class attack:

    def __init__(self, id):
        attacks = {
            1 :  {
                "name" : "atk1",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            2 :  {
                "name" : "atk2",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            3 :  {
                "name" : "atk3",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            4 :  {
                "name" : "atk4",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            5 :  {
                "name" : "atk5",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            6 :  {
                "name" : "atk6",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            7 :  {
                "name" : "atk7",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            8 :  {
                "name" : "atk8",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            9 :  {
                "name" : "atk9",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
            10 :  {
                "name" : "atk10",
                "element" : 1,
                "power" : 100,
                "frequency" : 2
            },
        }
        self.name = attacks[id]["name"]
        self.element = element(attacks[id]["element"])
        self.power = attacks[id]["power"]
        self.frequency = attacks[id]["frequency"]
        self.stats = {
            "used" : 0,
            "hits" : 0,
            "fail" : 0
        }

    def __str__(self):
        return self.name
