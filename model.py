"""

"""

import random

class Application:
    pass

colors = ["blue", "yellow", "green", "red", "black", "white"]

class Pegs:
    def __init__(self):
        self.pegList = []


    def randomize(self):
        self.pegList = []
        self.pegList.append (random.choice(colors))
        self.pegList.append(random.choice(colors))
        self.pegList.append (random.choice(colors))
        self.pegList.append(random.choice(colors))

class Board:
    """
    This class holds information about the current situation and scenario in/of the game.
    Eg. Objective (when human enters the information, computer randonmly generates it)
    Player history. There will be 2 parts, a guess and a hint. The guess is the same thing as the objective (above).
    Need to determine the status/state of the game. (Win, loss, still playing, etc)
    """
    pass


objective = Pegs()

objective.randomize()
print(objective.pegList)