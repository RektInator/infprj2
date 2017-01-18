# Game python file
import pygame
import button
import random
import time

def update(game):
    pass

# Deze class zorgt ervoor dat het dice systeem werkt
class Dice:
    def __init__(self):
        # zet de begin image van de die naar een lege
        self.image ="assets\img\die0.png"
    def onclick(self,game):
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
        game.dice_roll = random.randrange(1, 7)
        # dit zet het plaatje van de die naar hetgeen wat gegooid is
        self.image = "assets\img\die{}.png".format(game.dice_roll)
    def draw(self,game):
        # dit tekent de die
        button.draw_img(game, game.width - 70, game.height - 70, 64, 64, "", 0, self.image, (0,0,0), self.onclick)

dice = Dice()

def draw(game):
    dice.draw(game)