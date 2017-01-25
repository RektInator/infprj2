# game_mp python file
# todo: make this class work together with the networking stuff.
import pygame
import button
import random
import time
import translate
import questions
import textbox
import player
import checkbox
import math
from game import correct_answer

def update(game):
    pass

# Deze class zorgt ervoor dat het dice systeem werkt
class Dice:
    def __init__(self):
        # zet de begin image van de die naar een lege
        self.image = "assets\img\die0.png"
    def onclick(self,game):
        if game.get_current_player().did_roll:
            return

        # TODO: niet display.flip gebruiken
        for x in range(15):
            self.newimg = "assets\img\die{}.png".format(random.randrange(1,7))
            while self.newimg == self.image:
                self.newimg = "assets\img\die{}.png".format(random.randrange(1,7))
            self.image = self.newimg
            self.draw(game)
            pygame.display.flip()
            time.sleep(0.05)

        # dit pakt een random nummer van 1 t/m 6 en slaat het op in game.dice_roll
        game.get_current_player().dice_roll = random.randrange(1, 7)
        game.get_current_player().did_roll = True

        # dit zet het plaatje van de die naar hetgeen wat gegooid is
        self.image = "assets\img\die{}.png".format(game.get_current_player().dice_roll)

        	#Entertainment questions
        if game.get_current_player().pos.get_col() == 1:
             game.question = random.randrange(1,31)
				#History questions
        elif game.get_current_player().pos.get_col() == 2:
             game.question = random.randrange(31,44)
				#Sport questions
        elif game.get_current_player().pos.get_col() == 3:
             game.question = random.randrange(44,59)
				#Geography questions
        elif game.get_current_player().pos.get_col() == 4:
             game.question = random.randrange(59,70)
        
    def draw(self,game):
        # dit tekent de die
        label = (pygame.font.Font(None, 20)).render(translate.translate("ROLL"),1,(0,0,0))
        self.size = (pygame.font.Font(None, 20)).size(translate.translate("ROLL"))
        if game.get_current_player().did_roll == False and not game.get_current_player().direction == None:
            game.screen.blit(label, (702 - self.size[0]/2, 515))
        button.draw_img(game, game.width - 130, game.height - 70, 64, 64, "", 0, self.image, (0,0,0), self.onclick)

class GameLogic:
    def __init__(self):
        self.dice = Dice()
    def draw(self, game):
        # draw players in rows
        for plr in game.players:
            plr.draw()

        pass

gamelogic = GameLogic()

# Networking callbacks
def OnClientStart(client, data):
    # get player by index
    plr = client.game.get_player_by_index(int(data[1]))

    # set position of current player
    plr.setpos(int(data[2]), int(data[3]), int(data[4]))

    # debug output
    print("[DEBUG]: ClientStart packet received, client {} ({}) is starting at position {} {} {}.".format(plr.index, plr.name, plr.pos.col, plr.pos.x, plr.pos.y))

def OnClientMove(client, data):
    # get player by index
    plr = client.game.get_player_by_index(int(data[1]))

    # get direction
    direction = data[2]

    # get steps
    steps = int(data[3])

    # debug output
    print("[DEBUG]: ClientMove packet received, client {} ({}) is moving {} steps in direction {}.".format(plr.index, plr.name, steps, direction))

    # update data
    plr.moves_left = steps

    # loop through steps and update data
    for x in range(steps):
        if direction == "up":
            plr.go_up()
        elif direction == "left":
            plr.go_left()
        elif direction == "right":
            plr.go_right()

def OnSetPlayerIndex(client, data):
    # get player by index
    plr = client.game.get_player_by_index(int(data[1]))

    # debug output
    print("[DEBUG]: SetPlayerIndex packet received, it's now client {} ({})'s turn.".format(plr.index, plr.name))

    # set current player index
    client.game.current_player = int(data[1])

# Main draw function
def draw(game):
    # Background color
    pygame.draw.rect(game.screen,(204,204,204),(600,0,game.width * 0.9,game.height * 1))

    # Paint category colors
    pygame.draw.rect(game.screen,(255,0,0),(32,32,110,game.height * 0.8))
    pygame.draw.rect(game.screen,(255,239,0),(162,32,110,game.height * 0.8))
    pygame.draw.rect(game.screen,(52,163,253),(292,32,110,game.height * 0.8))
    pygame.draw.rect(game.screen,(24,208,27),(422,32,110,game.height * 0.8))
    game.screen.blit(pygame.image.load("assets\img\dots.png"), (60, 98))

    # Alloc font
    font = pygame.font.Font(None, 28)

    # Player turn info
    turnlabel = font.render("It's \"{}'s\" turn.".format(game.get_current_player().name), 1, (255,255,255))
    game.screen.blit(turnlabel, (0, 0))

    # Gamelogic drawing
    gamelogic.draw(game)

def init(game):
    game.isMP = True