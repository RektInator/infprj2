import pygame
import button
import listbox

def update(game):
    pass

def refresh(game):
    pass

serverbox = None

def serverlist_gettext(game, row, column):
    return "Test"

def serverlist_click(game, row, column):
    pass

def init(game):
    refresh(game)

    # create the serverlist 
    columns = []
    columns.append(listbox.Column(400, "Lobby"))
    columns.append(listbox.Column(200, "Spelers"))
    columns.append(listbox.Column(100, "Ping"))
    serverbox = listbox.create(game, 32, 32, 800 - 64, 20, columns, serverlist_gettext, serverlist_click)

    serverbox.set_rows(10)

def draw(game):
    listbox.draw(game)