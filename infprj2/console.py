import pygame
import textbox

def ExecuteCommand(game,box,isEnterPressed):
    print(box.text)

    # close the console
    remove(game)
    game.drawconsole = False

def init(game):
    textbox.create(game, 30, 30, 740, "", ExecuteCommand)

def remove(game):
    textbox.remove(game)

def draw(game):
    textbox.draw(game)