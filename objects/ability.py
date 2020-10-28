
abilities = {
    1 : {
        "effect" : "power",
        "quantity" : 100,
        "filter" : "element",
        "duration" : 1
    },
    2 : {
        "effect" : "frequency",
        "quantity" : 1,
        "filter" : "element",
        "duration" : 1
    },
    3 : {
        "effect" : "power",
        "quantity" : 100,
        "filter" : None,
        "duration" : 1
    },
    4 : {
        "effect" : "power",
        "quantity" : 200,
        "filter" : "element",
        "duration" : 1
    },
    5 : {
        "effect" : "frequency",
        "quantity" : 2,
        "filter" : "element",
        "duration" : 1
    },
    6 : {
        "effect" : "shield",
        "duration" : 1
    }
}

class ability:

    def __init__(self, id):
        self.id = id
        self.effect = abilities[id].effect
        self.quantity = abilities[id].quantity if quantity in abilities[id].keys() else None
        self.filter = abilities[id].filter if quantity in abilities[id].keys() else None
        self.duration = abilities[id].duration if quantity in abilities[id].keys() else None
