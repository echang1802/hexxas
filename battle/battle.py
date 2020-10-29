
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

    def choose_hexxa(self, player):
        print("Player {}".format(player))
        print(self.teams[player])
        print("Choose hexxa:")
        selection = int(input()) - 1
        hex = self.teams[player][selection]
        self.teams[player].pop(selection)
        return hex

    def defeated(self, player):
        if len(self.teams[player]) == 0:
            print("Player {} Defeated!".format(player))
            return None
        return self.choose_hexxa(player)

    def checkDefeated(self, player):
        if self.hexxa[player].resistance > 0:
            return False
        print(self.hexxa[player].name + " defeated!")
        self.hexxa[player] = self.defeated(player)
        return self.hexxa[player] is None

    def drawCard(self, player, cards = 1):
        for _ in range(cards):
            self.hands[player].append(self.decks[player].drawCard())
        self.ap -= 1

    def turnMenu(self, player):
        print("Turn player {}\nAccion points: {}\nCards in hand: {}\n1. Draw a card.\n2. Play a card.\n3. Show hexxa".format(player, self.ap, len(self.hands[player])))
        return int(input())

    def playCard(self, player):
        print("Cards in hand:")
        for card in self.hands[player]:
            print(card)
        print("0. return")
        action = int(input())
        if action == 0:
            return
        self.hands[player][action + 1].play(self.hexxa[player])
        self.ap -= 1

    def turn(self, player):
        self.ap = 2
        while self.ap > 0:
            action = self.turnMenu(player)
            if action == 1:
                self.drawCard(player)
            elif action == 2:
                self.playCard(player)
            elif action == 3:
                print(self.hexxa[player])

    def battle(self):
        ready = False
        self.hexxa = {
            1: self.choose_hexxa(1),
            2: self.choose_hexxa(2)
        }
        self.ap = 0
        self.drawCard(1, 3)
        self.drawCard(2, 3)

        while not ready:
            self.turn(1)
            self.turn(2)
            round = fight(self.hexxa[1], self.hexxa[2])
            round.choose_attacks()
            round.resolve_fight()
            round.restore()
            ready = self.checkDefeated(1)
            ready = self.checkDefeated(2) or ready
