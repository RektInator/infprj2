# Options menu python file
import pygame
import button

def update(game):
    pass

def draw(game):
    button.draw(game, 10, 10, game.width / 10, game.height / 20, "terug", 20,     (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))