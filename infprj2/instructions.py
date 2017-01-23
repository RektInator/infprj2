# Options menu python file
import pygame
import button
import config
import textbox
import translate

def update(game):
    pass

def init(game):
	pass

def draw(game):
	bg = pygame.image.load("assets/regels.jpg")
	game.screen.blit(bg,(0,0))
	button.draw(game, 10, 10, game.width / 10, game.height / 20, translate.translate("BACK"), 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))
