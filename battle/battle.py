
from battle.fight import fight

class battle:

    def __init__(self, team1, team2, deck1, deck2):
        self.teams = {
            1 : team1,
            2 : team2
        }
        self.decks = {
            1 : deck1,
            2 : deck2
        }
        self.hands = {
            1 : [],
            2 : []
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

    def drawCard(self, player, cards = 1):
        for _ in range(cards):
            self.hands[player].append(self.decks[player].drawCard())

    def turnMenu(self, player):
        print("Turn player {}\nAccion points: {}\nCards in hand: {}\n1. Draw a card.\n2. Play a card.".format(player, self.ap, len(self.hands[player])))
        return input()

    def playCard(self, player):
        print("Cards in hand:")
        for card in self.hands[player]:
            print(card)


    def turn(self, player):
        self.ap = 2
        while self.ap > 0:
            action =  self.turnMenu(player)
            if action == 1:
                self.drawCard(player)
            elif action == 2:
                self.playCard(player)

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
