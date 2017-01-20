class Position:
    def __init__(self, col, x, y):
        self.col = col
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_col(self):
        return self.col

class Player:
    def __init__(self):
        self.our_turn = False
        self.did_generate_question = False
        self.dice_roll = 0
        self.did_roll = False
        self.answers = []           # hols the current answers the player can choose from
        self.pos = None
        self.name = ""
        self.isAI = False
    def setpos(self, col, x, y):
        self.pos = Position(col, x, y)
    def setname(self, name):
        self.name = name
    def setai(self, ai):
        self.isAI = ai