

class elementalPower:

    def __init__(self, quantity, elementId, duration):
        self. quantity = quantity
        self.element = elementId
        self.duration = duration

    def apply_ability(self, hexxa):
        for atk in range(6):
            if hexxa.attacks[atk + 1].element.id == self.element:
                 hexxa.attacks[atk + 1].power += self.quantity

class elementalFrequency:

    def __init__(self, quantity, elementId, duration):
        self.quantity = quantity
        self.element = elementId
        self.duration = duration

    def apply_ability(self, hexxa):
        for atk in range(6):
            if hexxa.attacks[atk + 1].element.id == self.element:
                 hexxa.attacks[atk + 1].frequency += self.quantity
        hexxa.get_probs()

class allPower:

    def __init__(self, quantity, duration):
        self. quantity = quantity
        self.duration = duration

    def apply_ability(self, hexxa):
        for atk in range(6):
            hexxa.attacks[atk + 1].power += self.quantity

class allFrequency:

    def __init__(self, quantity, duration):
        self. quantity = quantity
        self.duration = duration

    def apply_ability(self, hexxa):
        for atk in range(6):
            hexxa.attacks[atk + 1].frequency += self.quantity
        hexxa.get_probs()

class shield:

    def __init__(self, duration):
        self.duration = duration

    def apply_ability(self, hexxa):
        hexxa.shield = True

class ability:

    def __init__(self, id, duration, quantity = None, elementId = None):
        self.id = id
        if id == 1:
            self.ability = elementalPower(quantity, elementId, duration)
        elif id == 2:
            self.ability = elementalFrequency(quantity, elementId, duration)
        elif id == 3:
            self.ability = allPower(quantity, duration)
        elif id == 4:
            self.ability = allFrequency(quantity, duration)
        elif id == 5:
            self.ability = shield(duration)

    def apply(self, hexxa):
        self.ability.apply_ability(hexxa)
