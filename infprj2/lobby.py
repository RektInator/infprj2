import pygame
import textbox
import packetevent
from packet import Packet

def draw(game):
    if game.name == "":
        textbox.draw(game)

def ExecuteCommand(game,box,isEnterPressed):
    if isEnterPressed:
        game.name = box.text
        game.sockets.send(Packet("setname:{}".format(box.text)).get())

def update(game):
    pass

def init(game):
    if game.name == "":
        textbox.create(game, 32, 32, 300, "", lambda game,box,isEnterPressed: ExecuteCommand(game,box,isEnterPressed))
    pass
