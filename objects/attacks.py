
from objects.elements import element

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
                "element" : 2,
                "power" : 100,
                "frequency" : 2
            },
            3 :  {
                "name" : "atk3",
                "element" : 3,
                "power" : 100,
                "frequency" : 2
            },
            4 :  {
                "name" : "atk4",
                "element" : 4,
                "power" : 100,
                "frequency" : 2
            },
            5 :  {
                "name" : "atk5",
                "element" : 5,
                "power" : 100,
                "frequency" : 2
            },
            6 :  {
                "name" : "atk6",
                "element" : 6,
                "power" : 100,
                "frequency" : 2
            },
            7 :  {
                "name" : "atk7",
                "element" : 1,
                "power" : 200,
                "frequency" : 2
            },
            8 :  {
                "name" : "atk8",
                "element" : 2,
                "power" : 200,
                "frequency" : 2
            },
            9 :  {
                "name" : "atk9",
                "element" : 3,
                "power" : 200,
                "frequency" : 2
            },
            10 :  {
                "name" : "atk10",
                "element" : 4,
                "power" : 200,
                "frequency" : 2
            },
        }
        self.id = id
        self.name = attacks[id]["name"]
        self.element = element(attacks[id]["element"])
        self.power = attacks[id]["power"]
        self.frequency = attacks[id]["frequency"]
        self.basePower = attacks[id]["power"]
        self.baseFrequency = attacks[id]["frequency"]
        self.stats = {
            "used" : 0,
            "hits" : 0,
            "fail" : 0
        }

    def restore(self):
        self.power = self.basePower
        self.frequency = self.baseFrequency

    def __str__(self):
        return self.name + " - " + self.element.name + " - " + str(self.power)
