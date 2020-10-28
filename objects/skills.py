
from objects.ability import ability
from objects.element import element

skills = {
    1 : {
        "name" : "pow1ele1",
        "elementId" : 1,
        "abilityId"  : 1
    },
    2 : {
        "name" : "pow1ele2",
        "elementId" : 2,
        "abilityId"  : 1
    },
    3 : {
        "name" : "pow1ele3",
        "elementId" : 3,
        "abilityId"  : 1
    },
    4 : {
        "name" : "pow1ele4",
        "elementId" : 4,
        "abilityId"  : 1
    },
    5 : {
        "name" : "pow1ele5",
        "elementId" : 5,
        "abilityId"  : 1
    },
    6 : {
        "name" : "pow1ele6",
        "elementId" : 6,
        "abilityId"  : 1
    },
    7 : {
        "name" : "fre1ele1",
        "elementId" : 1,
        "abilityId"  : 2
    },
    8 : {
        "name" : "fre1ele2",
        "elementId" : 2,
        "abilityId"  : 2
    },
    9 : {
        "name" : "fre1ele3",
        "elementId" : 3,
        "abilityId"  : 2
    },
    10 : {
        "name" : "fre1ele4",
        "elementId" : 4,
        "abilityId"  : 2
    },
    11 : {
        "name" : "fre1ele5",
        "elementId" : 5,
        "abilityId"  : 2
    },
    12 : {
        "name" : "fe1ele6",
        "elementId" : 6,
        "abilityId"  : 2
    },
}

class skill:

    def __init__(self, id):
        self.name = skills[id].name
        sellf.element = element(skills[id].elementId)
        self.ability = ability(skills[id].abilityId)

    def __str__(self):
        return self.name
