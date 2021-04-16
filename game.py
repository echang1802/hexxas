
from battle.battle import battle
from menu.in_game import menu

class game:

    def __init__(self):
        pass

    def start(self):

        self.team = self.create_team()
        self.deck = self.create_deck()
        self.menu = menu()

        ready = False
        while not ready:
            fight = battle(self.team, self.create_ai_team(), sef.deck, self.create_ai_deck())
            fight.battle()

            self.post_battle()

            self.menu.start_menu()

            ready = self.menu.ready

    def create_team(self):
        pass

    def create_deck(self):
        pass

    def create_ai_team(self):
        pass

    def create_ai_deck(self):
        pass

    def post_battle(self):
        pass
