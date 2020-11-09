
from objects.decks import deck
from objects.hexxas import hexxas
from battle.battle import battle

fight = battle([
    hexxas(1),hexxas(1),hexxas(1)
],[
    hexxas(1),hexxas(1),hexxas(1)
], deck(), deck())
fight.battle()
