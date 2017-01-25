import pygame
import textbox

def draw(game):
    if game.name == "":
        textbox.draw(game)
    pass

def ExecuteCommand(game,box,isEnterPressed):
    if isEnterPressed:
        game.name = box.text

def update(game):
    pass

def init(game):
    if game.name == "":
        textbox.create(game, 32, 32, 300, "", lambda game,box,isEnterPressed: ExecuteCommand(game,box,isEnterPressed))
    pass
