import pygame
import textbox
import packetevent
import listbox
import button
from packet import Packet

def draw(game):
    if game.name == "":
        textbox.draw(game)
    else:
        listbox.draw(game)
        # if game.players[0].name == game.name:
        #    button.draw(game, 670, 32, 100, 32, translate.translate("START_GAME"), 20, (0,0,0), (255,255,255), lambda game: game.sockets.send(Packet("startgame").get()))

def Setname(game,box,isEnterPressed):
    if isEnterPressed:
        game.name = box.text
        game.sockets.send(Packet("setname:{}".format(box.text)).get())

def update(game):
    # listbox.update(game)
    pass

# asks for the text for the current row / column combination
def playerlist_gettext(game, row, column):
    plrcount = game.get_player_count()
    # print("Row {} Playercount {}".format(row, plrcount))

    if row == plrcount:
        return "<Unnamed player>"

    if not game.players[row].name:
        return "<Unnamed player>"

    return game.players[row].name

# this is being called when a serverlist item is being clicked
def playerlist_click(game, row, column):
    pass

# this is being called when the serverlist should update itself
def playerlist_update(game, box):
    box.item_count = game.get_player_count()

def init(game):
    textbox.create(game, 32, 32, 300, "", lambda game,box,isEnterPressed: Setname(game,box,isEnterPressed))

    # create the player list 
    columns = []
    columns.append(listbox.Column(400, "Spelers"))
    listbox.create(game, 32, 96, 800 - 64, 20, columns, playerlist_gettext, playerlist_click, playerlist_update)