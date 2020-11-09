

class element:

    def __init__(self, id):
        elements = {
            1 : {
                "name" : "fire",
                "ability" : ""
            },
            2 : {
                "name" : "water",
                "ability" : ""
            },
            3 : {
                "name" : "earth",
                "ability" : ""
            },
            4 : {
                "name" : "wind",
                "ability" : ""
            },
            5 : {
                "name" : "ligth",
                "ability" : ""
            },
            6 : {
                "name" : "dark",
                "ability" : ""
            },
        }
        self.id = id
        self.name = elements[id]["name"]
        self.ability = elements[id]["ability"]

    def __str__(self):
        return self.name
