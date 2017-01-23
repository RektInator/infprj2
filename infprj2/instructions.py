# Options menu python file
import pygame
import button
import config
import textbox
import translate

def update(game):
    pass

def init(game):
	textbox.create(game,32,60,game.width * 0.5, "Hi", lambda x: game.set_state(7))


def draw(game):
	file = open("assets\instructions.txt", "r")
	data = file.read()
	textbox.draw(game)
	button.draw(game, 10, 10, game.width / 10, game.height / 20, translate.translate("BACK"), 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))