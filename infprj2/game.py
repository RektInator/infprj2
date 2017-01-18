# Game python file
import pygame
import button

def update(game):
    pass

class Dice:
    def __init__(self):
        self.image = "assets\img\die1.png"
    def onclick(self):
        self.image = "assets\img\die2.png"
    def draw(self,game):
        button.draw_img(game, game.width - 70, game.height - 70, 64, 64, "", 0, self.image, (0,0,0), self.onclick)

dice = Dice()

def draw(game):
    dice.draw(game)