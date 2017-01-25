# Game python file
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

        game.question = random.randrange(1,70)
        
    def draw(self,game):
        # dit tekent de die
        label = (pygame.font.Font(None, 20)).render(translate.translate("ROLL"),1,(0,0,0))
        self.size = (pygame.font.Font(None, 20)).size(translate.translate("ROLL"))
        if game.get_current_player().did_roll == False and not game.get_current_player().direction == None:
            game.screen.blit(label, (702 - self.size[0]/2, 515))
        button.draw_img(game, game.width - 130, game.height - 70, 64, 64, "", 0, self.image, (0,0,0), self.onclick)

def correct_answer(game):
    for x in range(1,4):
        if translate.translate(game.get_current_player().answers[x-1]) == translate.translate("QUESTIONANSWER{}".format(game.question)):
            return x
            break

    print("Question {} is incorrect!".format(game.question))
    return 1

class GameLogic:
    def __init__(self):
        self.dice = Dice()
    def draw(self, game):
        # draw players in rows
        for plr in game.players:
            plr.draw()

        # draw questions etc
        if game.get_current_player().did_roll and not game.get_current_player().did_answer and not game.get_current_player().moves_left:
            if not game.get_current_player().did_generate_question:

                # remove existing answers
                game.get_current_player().answers.clear()

                # add new answers
                game.get_current_player().answers.append("QUESTION{}_ANSWER1".format(game.question))
                game.get_current_player().answers.append("QUESTION{}_ANSWER2".format(game.question))
                game.get_current_player().answers.append("QUESTION{}_ANSWER3".format(game.question))
                game.get_current_player().answers.append("QUESTION{}".format(game.question))

                # do not re-generate question
                game.get_current_player().did_generate_question = True

            # draw question popup
            if not game.get_current_player().isAI:
                font = pygame.font.Font(None, 20)
                pygame.draw.rect(game.screen,(255,255,255),(24,9,game.width*0.8 + 2,game.height * 0.9 + 2))
                pygame.draw.rect(game.screen,(153,146,245),(25,10,game.width*0.8,game.height * 0.9))
                game.screen.blit(font.render(translate.translate(game.get_current_player().answers[3]), 1, (255,255,255)), (32,17))
                button.draw(game, game.width * 0.25,162,300,60, translate.translate(game.get_current_player().answers[0]), 20, (0,0,0), (255,255,255), lambda game: question_chosen(game, 1))
                button.draw(game, game.width * 0.25,252,300,60, translate.translate(game.get_current_player().answers[1]), 20, (0,0,0), (255,255,255), lambda game: question_chosen(game, 2))
                button.draw(game, game.width * 0.25,342,300,60, translate.translate(game.get_current_player().answers[2]), 20, (0,0,0), (255,255,255), lambda game: question_chosen(game, 3))
            else:
                if random.randrange(1,4) == 2:
                    question_chosen(game, correct_answer(game))
                else:
                    question_chosen(game, random.randrange(1, 4))
        elif not game.get_current_player().did_roll and not game.get_current_player().did_choose_row:
            # draw start buttons
            if not game.get_current_player().isAI:
                if 1 not in game.chosen:
                    button.draw(game, 45, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 1))
                if 2 not in game.chosen:
                    button.draw(game, 175, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 2))
                if 3 not in game.chosen:
                    button.draw(game, 305, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 3))
                if 4 not in game.chosen:
                    button.draw(game, 435, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 4))
            else:
                time.sleep(0.4)
                chosen = False
                while not chosen:
                    number = random.randrange(1,5)
                    if not number in game.chosen:
                        start_chosen(game,number)
                        chosen = True
        elif game.get_current_player().direction == None: 
            if not game.get_current_player().isAI:
                # draw movement buttons
                button.draw_img(game, game.width - 145, game.height - 264, 80, 80, "", 0, "assets/img/pijlomhoog.png", (0,0,0), lambda game: game.get_current_player().set_direction("up"))
                button.draw_img(game, game.width - (145 + 40), game.height - 200, 80, 80, "", 0, "assets/img/pijllinks.png", (0,0,0), lambda game: game.get_current_player().set_direction("left"))
                button.draw_img(game, game.width - (145 - 40), game.height - 200, 80, 80, "", 0, "assets/img/pijlrechts.png", (0,0,0), lambda game: game.get_current_player().set_direction("right"))
                # button.draw(game, 435, game.height * 0.9, 100, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: start_chosen(game, 4))
            else:
                time.sleep(0.3)
                game.get_current_player().set_direction("up")
        elif game.get_current_player().moves_left:
            if game.get_current_player().direction == "up":
                game.get_current_player().go_up()
            elif game.get_current_player().direction == "left":
                game.get_current_player().go_left()
            elif game.get_current_player().direction == "right":
                game.get_current_player().go_right()

        # Draw dice
        if game.get_current_player().did_choose_row and not game.get_current_player().direction == None:
            if game.get_current_player().isAI:
                pygame.display.flip()
                if not game.get_current_player().did_roll:
                    pygame.display.flip()
                    time.sleep(0.4)
                    self.dice.onclick(game)
    
            self.dice.draw(game)

gamelogic = GameLogic()

def question_chosen(game, idx):
    # game.set_next_player()
    # gamelogic.dice.image = "assets\img\die0.png"
    # check if the question was answerred correctly
    
    # increment score for correct question, and set the amount of moves we can make.
    if translate.translate(game.get_current_player().answers[idx-1]) == translate.translate("QUESTIONANSWER{}".format(game.question)):
        game.get_current_player().score += 15
        game.get_current_player().moves_left = math.ceil(game.get_current_player().dice_roll / 2)
    else:
        game.get_current_player().score -= 10
        game.set_next_player()

def start_chosen(game, idx):
    game.get_current_player().setpos(idx, 0, 0)
    game.get_current_player().did_choose_row = True
    game.chosen.append(idx)
    game.set_next_player()

def SetPlayerCount(game, idx):
    if idx == 2:
        game.players.append(player.Player(game))
        game.players.append(player.Player(game))
        textbox.create(game, game.width * 0.3, game.height * 0.2, 250, "", lambda game,box,isEnterPressed: SetName(0, game, box))
        textbox.create(game, game.width * 0.3, game.height * 0.35, 250, "", lambda game,box,isEnterPressed: SetName(1, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.35, "AI", False, lambda game,box: SetAI(1, game, box))
    if idx == 3:
        game.players.append(player.Player(game))
        game.players.append(player.Player(game))
        game.players.append(player.Player(game))
        textbox.create(game, game.width * 0.3, game.height * 0.2, 250, "", lambda game,box,isEnterPressed: SetName(0, game, box))
        textbox.create(game,game.width * 0.3, game.height * 0.35, 250, "", lambda game,box,isEnterPressed: SetName(1, game, box))
        textbox.create(game, game.width * 0.3, game.height * 0.50, 250, "", lambda game,box,isEnterPressed: SetName(2, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.35, "AI", False, lambda game,box: SetAI(1, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.50, "AI", False, lambda game,box: SetAI(2, game, box))
    if idx == 4:
        game.players.append(player.Player(game))
        game.players.append(player.Player(game))
        game.players.append(player.Player(game))
        game.players.append(player.Player(game))
        textbox.create(game, game.width * 0.3, game.height * 0.2, 250, "", lambda game,box,isEnterPressed: SetName(0, game, box))
        textbox.create(game, game.width * 0.3, game.height * 0.35, 250, "", lambda game,box,isEnterPressed: SetName(1, game, box))
        textbox.create(game, game.width * 0.3, game.height * 0.50, 250, "", lambda game,box,isEnterPressed: SetName(2, game, box))
        textbox.create(game, game.width * 0.3, game.height * 0.65, 250, "", lambda game,box,isEnterPressed: SetName(3, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.20, "AI", False, lambda game,box: SetAI(0, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.35, "AI", False, lambda game,box: SetAI(1, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.50, "AI", False, lambda game,box: SetAI(2, game, box))
        checkbox.create(game, game.width * 0.7, game.height * 0.65, "AI", False, lambda game,box: SetAI(3, game, box))

    game.playercount = idx

def StartGame(game):
    
    for x in range(0, game.playercount):
        if not len(game.players[x].name):
            return

    game.has_started = True

def draw(game):
    if game.has_started:
        # Make sure the playername boxes are gone
        textbox.remove(game)
        checkbox.remove(game)
	    # Achtergrond kleur
        pygame.draw.rect(game.screen,(204,204,204),(600,0,game.width * 0.9,game.height * 1))

	    # Teken categorie kleur
        pygame.draw.rect(game.screen,(255,0,0),(32,32,110,game.height * 0.8))
        pygame.draw.rect(game.screen,(255,239,0),(162,32,110,game.height * 0.8))
        pygame.draw.rect(game.screen,(52,163,253),(292,32,110,game.height * 0.8))
        pygame.draw.rect(game.screen,(24,208,27),(422,32,110,game.height * 0.8))
        game.screen.blit(pygame.image.load("assets\img\dots.png"), (60, 98))

	    # Start onder categorie
        font = pygame.font.Font(None, 48)
        font2 = pygame.font.Font(None, 20)
        font3 = pygame.font.Font(None, 28)
        # label_1 = font.render("Start", 1, (255,255,255))
        # size = font.size("Start")
        # game.screen.blit(label_1,(45, game.height * 0.9))
        # game.screen.blit(label_1,(175, game.height * 0.9))
        # game.screen.blit(label_1,(305, game.height * 0.9))
        # game.screen.blit(label_1,(435, game.height * 0.9))

        # Player turn info
        turnlabel = font3.render("It's \"{}'s\" turn.".format(game.get_current_player().name), 1, (255,255,255))
        game.screen.blit(turnlabel, (0, 0))

        # Gamelogic drawing
        gamelogic.draw(game)
    elif game.playercount:
        game.screen.fill((60,60,60))
        font = pygame.font.Font(None, 30)
        label_1 = font.render(translate.translate("MAKE"), 1, (255,255,255))
        size = font.size(translate.translate("MAKE"))
        game.screen.blit(label_1,(game.width * 0.32, game.height * 0.1))
        # Draw the boxes for the player names
        textbox.draw(game)
        checkbox.draw(game)
        button.draw(game, game.width * 0.4, game.height * 0.8, 64, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: StartGame(game))
    else:
        game.screen.fill((60,60,60))
        button.draw(game, 10, 10, game.width / 10, game.height / 20, translate.translate("BACK"), 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))
        font = pygame.font.Font(None, 30)
        label_1 = font.render(translate.translate("AMOUNT"), 1, (255,255,255))
        size = font.size(translate.translate("AMOUNT"))
        game.screen.blit(label_1,(game.width * 0.37, game.height * 0.2))
        button.draw(game, game.width * 0.42, game.height * 0.3, 128, 64, "2", 30, (0,0,0), (255,255,255), lambda game: SetPlayerCount(game, 2))
        button.draw(game, game.width * 0.42, game.height * 0.45, 128, 64, "3", 30, (0,0,0), (255,255,255), lambda game: SetPlayerCount(game, 3))
        button.draw(game, game.width * 0.42, game.height * 0.60, 128, 64, "4", 30, (0,0,0), (255,255,255), lambda game: SetPlayerCount(game, 4))

# This function is being called when the text in a name box changes
def SetName(idx, game, box):
    game.players[idx].setname(box.text)

# This function is called when an AI checkbox is clicked.
def SetAI(idx, game, box):
    print("Player {} AI state is {}".format(idx, box.isChecked))
    game.players[idx].setai(box.isChecked)

def init(game):
    pass