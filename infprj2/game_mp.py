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
import config
from packet import Packet

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

        # get our player index
        plr = game.get_current_player()

        # dit pakt een random nummer van 1 t/m 6 en slaat het op in game.dice_roll
        plr.dice_roll = random.randrange(1, 7)
        plr.did_roll = True

        # dit zet het plaatje van de die naar hetgeen wat gegooid is
        self.image = "assets\img\die{}.png".format(plr.dice_roll)

        # Entertainment questions
        if plr.pos.get_col() == 1:
             game.question = random.randrange(1,31)
		# History questions
        elif plr.pos.get_col() == 2:
             game.question = random.randrange(31,44)
		# Sport questions
        elif plr.pos.get_col() == 3:
             game.question = random.randrange(44,59)
		# Geography questions
        elif plr.pos.get_col() == 4:
             game.question = random.randrange(59,70)
        
    def draw(self,game):
        # dit tekent de die
        label = (pygame.font.Font(None, 20)).render(translate.translate("ROLL"),1,(0,0,0))
        self.size = (pygame.font.Font(None, 20)).size(translate.translate("ROLL"))
        if game.get_current_player().did_roll == False and not game.get_current_player().direction == None:
            game.screen.blit(label, (702 - self.size[0]/2, 515))
        button.draw_img(game, game.width - 130, game.height - 70, 64, 64, "", 0, self.image, (0,0,0), self.onclick)

def correct_answer(plr, qix):
    for x in range(1,4):
        if translate.translate(plr.answers[x-1]) == translate.translate("QUESTIONANSWER{}".format(qix)):
            return x

    print("Question {} is incorrect!".format(qix))
    return 1

def question_chosen(game, idx):

    # get current player
    plr = game.get_current_player()
    plr.moves_left = math.ceil(plr.dice_roll / 2)

    correct = correct_answer(plr, game.question)
    print("[DEBUG]: Answer {} selected, {} is the correct answer.".format(idx, correct))

    if correct == idx:
        # let the other clients know that we've answerred the question correctly,
        # therefore update our location
        game.sockets.send(Packet("playermove:{}:{}".format(plr.direction, plr.moves_left)).get())
    else:
        # send 0 steps so the client knows he got it wrong
        game.sockets.send(Packet("playermove:{}:0".format(plr.direction)).get())
    
    # reset player data
    plr.did_roll = False
    plr.did_answer = False
    plr.moves_left = 0
    plr.did_generate_question = False
    plr.direction = None

    # tell the dedicated server that we should move on to the next player
    game.sockets.send(Packet("movedone").get())

class GameLogic:
    def __init__(self):
        self.dice = Dice()
    def draw(self, game):
        # draw players in rows
        for plr in game.players:
            plr.draw()

        # check if its our turn
        if game.index == game.current_player:
            plr = game.get_current_player()
            if plr.did_roll and not plr.did_answer and not plr.moves_left:
                if not plr.did_generate_question:
                    # remove existing answers
                    plr.answers.clear()

                    # add new answers
                    plr.answers.append("QUESTION{}_ANSWER1".format(game.question))
                    plr.answers.append("QUESTION{}_ANSWER2".format(game.question))
                    plr.answers.append("QUESTION{}_ANSWER3".format(game.question))
                    plr.answers.append("QUESTION{}".format(game.question))

                    # do not re-generate question
                    plr.did_generate_question = True

                # draw question popup
                font = pygame.font.Font(None, 20)
                pygame.draw.rect(game.screen,(255,255,255),(24,9,game.width*0.8 + 2,game.height * 0.9 + 2))
                pygame.draw.rect(game.screen,(153,146,245),(25,10,game.width*0.8,game.height * 0.9))
                game.screen.blit(font.render(translate.translate(plr.answers[3]), 1, (255,255,255)), (32,17))
                button.draw(game, game.width * 0.25,162,300,60, translate.translate(plr.answers[0]), 20, (0,0,0), (255,255,255), lambda game: question_chosen(game, 1))
                button.draw(game, game.width * 0.25,252,300,60, translate.translate(plr.answers[1]), 20, (0,0,0), (255,255,255), lambda game: question_chosen(game, 2))
                button.draw(game, game.width * 0.25,342,300,60, translate.translate(plr.answers[2]), 20, (0,0,0), (255,255,255), lambda game: question_chosen(game, 3))
            elif plr.direction == None: 
                # paint direction buttons
                button.draw_img(game, game.width - 145, game.height - 264, 80, 80, "", 0, "assets/img/pijlomhoog.png", (0,0,0), lambda game: plr.set_direction("up"))
                button.draw_img(game, game.width - (145 + 40), game.height - 200, 80, 80, "", 0, "assets/img/pijllinks.png", (0,0,0), lambda game: plr.set_direction("left"))
                button.draw_img(game, game.width - (145 - 40), game.height - 200, 80, 80, "", 0, "assets/img/pijlrechts.png", (0,0,0), lambda game: plr.set_direction("right"))

            # paint dice
            self.dice.draw(game)
        else:
            # not our turn
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
    if steps != 0:
        for x in range(steps + 1):
            if direction == "up":
                plr.go_up()
            elif direction == "left":
                plr.go_left()
            elif direction == "right":
                plr.go_right()  

    plr.moves_left = 0

def OnSetPlayerIndex(client, data):
    # get player by index   
    client.game.get_current_player().our_turn = False
    plr = client.game.get_player_by_index(int(data[1]))

    # debug output
    print("[DEBUG]: SetPlayerIndex packet received, it's now client {} ({})'s turn.".format(plr.index, plr.name))

    # set current player index
    client.game.current_player = int(data[1])
    plr.our_turn = True

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
    if game.get_current_player() is not None:
        turnlabel = font.render("It's \"{}'s\" turn.".format(game.get_current_player().name), 1, (255,255,255))
        game.screen.blit(turnlabel, (0, 0))
    if config.get("developer_mode") == "1":
        textbox.draw(game)

    # Gamelogic drawing
    gamelogic.draw(game)

def callback(game,box,isEnterPressed):
    if isEnterPressed:
        if box.text != "":
            game.sockets.send(Packet(box.text.replace("-",":")).get())
            box.text = ""

def init(game):
    textbox.create(game, 32, 550, 300, "", lambda game,box,isEnterPressed: callback(game,box,isEnterPressed))
    game.isMP = True