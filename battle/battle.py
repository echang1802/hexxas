
from battle.fight import fight

class battle:

    def __init__(self, team1, team2):
        self.teams = {
            1: team1,
            2: team2
        }

    def choose_hexxa(self, team):
        print("Player {}".format(team))
        print(self.teams[team])
        print("Choose hexxa:")
        selection = int(input()) - 1
        hex = self.teams[team][selection]
        self.teams[team].pop(selection)
        return hex

    def defeated(self, team):
        if len(self.teams[team]) == 0:
            print("Team{} Defeated!".format(team))
            return None
        return self.choose_hexxa(team)

    def battle(self):
        ready = False

        hex1 = self.choose_hexxa(1)
        hex2 = self.choose_hexxa(2)

        while not ready:
            round = fight(hex1, hex2)
            round.choose_attacks()
            round.resolve_fight(hex1, hex2)
            if hex1.resistance == 0:
                print(hex1.name + " defeated!")
                hex1 = self.defeated(1)
                ready = hex1 is None
            elif hex2.resistance == 0:
                print(hex2.name + " defeated!")
                hex2 = self.defeated(2)
                ready = hex2 is None
