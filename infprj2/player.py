import pygame

# constant variables
row_xoff = [32, 162, 292, 422]
row_xoff_s = [32, 110 - 10 - 32]

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
    def __init__(self, game):
        self.game = game
        self.our_turn = False
        self.did_generate_question = False
        self.dice_roll = 0
        self.did_roll = False
        self.did_answer = False
        self.answers = []           # holds the current answers the player can choose from
        self.pos = Position(0, 0, 0)
        self.name = ""
        self.isAI = False
        self.did_choose_row = False
        self.moves_left = 0
        self.score = 0
    def setpos(self, col, x, y):
        self.pos = Position(col, x, y)
    def setname(self, name):
        self.name = name
    def setai(self, ai):
        self.isAI = ai

    # player movement funcs
    def go_left(self):
        self.moves_left -= 1
        if not self.moves_left:
            self.game.set_next_player()

        if self.pos.get_col() == 1 and self.pos.get_x() == 0:
            self.pos.col = 4
            self.pos.x = 1
        elif self.pos.x == 0:
            self.pos.col -= 1
            self.pos.x = 1
        else:
            self.pos.x -= 1
    def go_right(self):
        self.moves_left -= 1
        if not self.moves_left:
            self.game.set_next_player()

        if self.pos.get_col() == 4 and self.pos.get_x() == 1:
            self.pos.col = 1
            self.pos.x = 0
        elif self.pos.x == 1:
            self.pos.col += 1
            self.pos.x = 0
        else:
            self.pos.x += 1
    def go_up(self):
        self.moves_left -= 1
        if not self.moves_left:
            self.game.set_next_player()

        self.pos.y += 1

    # player draw func
    def draw(self):
        if not self.pos.col == 0:
            # player coordinates
            xpos = row_xoff[self.pos.col - 1] + row_xoff_s[self.pos.x]
            ypos = (480 - (self.pos.y * 27))

            # draw player name
            font = pygame.font.Font(None, 26)
            playername = font.render(self.name, 1, (0,0,0))
            size = font.size(self.name)
            self.game.screen.blit(playername, (xpos - size[0]/2, ypos - 30))

            # draw player circle
            pygame.draw.circle(self.game.screen, (0, 0, 0), (xpos, ypos), 10, 10)
