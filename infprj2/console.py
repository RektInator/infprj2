import pygame
import textbox

def ExecuteCommand(game,box,isEnterPressed):
    if isEnterPressed:
        # execute command

        # close console
        remove(game)
        game.drawconsole = False

def init(game):
    textbox.create(game, 30, 30, 740, "", ExecuteCommand)

def remove(game):
    textbox.remove(game)

def draw(game):
    textbox.draw(game)
