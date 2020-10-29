
from objects.ability import ability
from objects.element import element

skills = {
    1 : {
        "name" : "pow1ele1",
        "elementId" : 1,
        "abilityTypeId"  : 1,
        "quantity" : 100,
        "duration" : 1
    },
    2 : {
        "name" : "pow1ele2",
        "elementId" : 2,
        "abilityTypeId"  : 1,
        "quantity" : 100,
        "duration" : 1
    },
    3 : {
        "name" : "pow1ele3",
        "elementId" : 3,
        "abilityTypeId"  : 1,
        "quantity" : 100,
        "duration" : 1
    },
    4 : {
        "name" : "pow1ele4",
        "elementId" : 4,
        "abilityTypeId"  : 1,
        "quantity" : 100,
        "duration" : 1
    },
    5 : {
        "name" : "pow1ele5",
        "elementId" : 5,
        "abilityTypeId"  : 1,
        "quantity" : 100,
        "duration" : 1
    },
    6 : {
        "name" : "pow1ele6",
        "elementId" : 6,
        "abilityTypeId"  : 1,
        "quantity" : 100,
        "duration" : 1
    },
    7 : {
        "name" : "fre1ele1",
        "elementId" : 1,
        "abilityTypeId"  : 2,
        "quantity" : 1,
        "duration" : 1
    },
    8 : {
        "name" : "fre1ele2",
        "elementId" : 2,
        "abilityTypeId"  : 2,
        "quantity" : 1,
        "duration" : 1
    },
    9 : {
        "name" : "fre1ele3",
        "elementId" : 3,
        "abilityTypeId"  : 2,
        "quantity" : 1,
        "duration" : 1
    },
    10 : {
        "name" : "fre1ele4",
        "elementId" : 4,
        "abilityTypeId"  : 2,
        "quantity" : 1,
        "duration" : 1
    },
    11 : {
        "name" : "fre1ele5",
        "elementId" : 5,
        "abilityTypeId"  : 2,
        "quantity" : 1,
        "duration" : 1
    },
    12 : {
        "name" : "fre1ele6",
        "elementId" : 6,
        "abilityTypeId"  : 2,
        "quantity" : 1,
        "duration" : 1
    },
    13 : {
        "name" : "pow1",
        "abilityTypeId"  : 3,
        "quantity" : 1,
        "duration" : 1
    },
    14 : {
        "name" : "shield",
        "abilityTypeId"  : 5,
        "duration" : 1
    },
}

class skill:

    def __init__(self, id):
        self.name = skills[id].name
        self.element = element(skills[id].elementId)
        self.ability = ability(
            id = skills[id].abilityTypeId,
            duration = skills[id].duration,
            quantity = skills[id].quantity if "quantity" in skills[id].keys() else None,
            elementId = skills[id].elementId if "elementId" in skills[id].keys() else None
        )

    def play(self, hexxa):
        self.ability.apply(hexxa)

    def __str__(self):
        return self.name
