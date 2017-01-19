# Import pygame
import pygame

class Checkbox:
    def __init__(self, game, x, y, text, callback):
        self.game = game
        self.x = x
        self.y = y
        self.text = text
    def draw(self):
        pass

checkboxes = []

def create(game, x, y, text, callback):
    _box = Checkbox(game, x, y, text, callback)
    checkboxes.append(_box)

def remove(game):
    checkboxes.clear()   

def update(game):
    pass

def draw(game):
    for box in checkboxes:
        box.draw()
