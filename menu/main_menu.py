
from game import game

class main_menu:

    def __init__(self):
        self.options = {
            1 : "Battle",
            2 : "Exit"
        }

        self.title = "Hexxas"


    def start_menu(self):
        ready = False
        while not ready:
            print(self.title)
            print()
            print("Selecciona una opción:")
            for id, opt in self.options.items():
                print("{} - {}".format(id, opt))
            selected = int(input())
            if not selected in self.options.keys():
                continue
            ready = self.action(selected)

    def action(self, selected):
        if self.options[selected] == "Exit":
            return True
        newGame = game()
        newGame.start()
