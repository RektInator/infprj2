# Game python file
import pygame
import button
import random
import time
import translate
import questions
import textbox
import player

def update(game):
    pass

# Deze class zorgt ervoor dat het dice systeem werkt
class Dice:
    def __init__(self):
        # zet de begin image van de die naar een lege
        self.image ="assets\img\die0.png"
    def onclick(self,game):
        game.get_last_player().did_roll = False

        if game.get_current_player().did_roll:
            return

        # TODO: niet display.flip gebruiken
        for x in range(20):
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
    def draw(self,game):
        # dit tekent de die
        if game.get_current_player().dice_roll == 0:
            game.screen.blit((pygame.font.Font(None, 20)).render("Roll the die!", 1, (0,0,0)),(665, 515))
        button.draw_img(game, game.width - 130, game.height - 70, 64, 64, "", 0, self.image, (0,0,0), self.onclick)

dice = Dice()

def question_chosen(game, idx):
    game.ourturn = False

def callback_question1(game):
    question_chosen(game, 1)
    
def callback_question2(game):
    question_chosen(game, 2)

def callback_question3(game):
    question_chosen(game, 3)

def SetPlayerCount(game, idx):
    for x in range(0, idx):
        game.players.append(player.Player())
        textbox.create(game, 32, 32 + (32 * x), 100, "", lambda game,box,isEnterPressed: SetName(x, game, box))
        
    game.playercount = idx

def StartGame(game):
    game.has_started = True

def draw(game):
    if game.has_started:
        # Make sure the playername boxes are gone
        textbox.remove(game)

	    # Achtergrond kleur
        pygame.draw.rect(game.screen,(204,204,204),(600,0,game.width * 0.9,game.height * 1))

	    # Teken dice
        dice.draw(game)

	    # Teken categorie kleur
        pygame.draw.rect(game.screen,(255,0,0),(32,32,110,game.height * 0.8))
        pygame.draw.rect(game.screen,(255,239,0),(162,32,110,game.height * 0.8))
        pygame.draw.rect(game.screen,(52,163,253),(292,32,110,game.height * 0.8))
        pygame.draw.rect(game.screen,(24,208,27),(422,32,110,game.height * 0.8))

	    # Start onder categorie
        font = pygame.font.Font(None, 48)
        font2 = pygame.font.Font(None, 20)
        label_1 = font.render("Start", 1, (255,255,255))
        size = font.size("Start")
        game.screen.blit(label_1,(45, game.height * 0.9))
        game.screen.blit(label_1,(175, game.height * 0.9))
        game.screen.blit(label_1,(305, game.height * 0.9))
        game.screen.blit(label_1,(435, game.height * 0.9))

        # Teken popup venster
    elif game.playercount:
        # Draw the boxes for the player names
        textbox.draw(game)
        button.draw(game, 32, 200, 64, 32, "Start", 20, (0,0,0), (255,255,255), lambda game: StartGame(game))
    else:
        button.draw(game, 32, 32, 64, 32, "2", 20, (0,0,0), (255,255,255), lambda game: SetPlayerCount(game, 2))
        button.draw(game, 32, 100, 64, 32, "3", 20, (0,0,0), (255,255,255), lambda game: SetPlayerCount(game, 3))
        button.draw(game, 32, 100 + (100 - 32), 64, 32, "4", 20, (0,0,0), (255,255,255), lambda game: SetPlayerCount(game, 4))

def SetName(idx, game, box):
    game.players[idx].setname(box.text)

def init(game):
    pass