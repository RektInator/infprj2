# Import pygame
import pygame

class Checkbox:
    def __init__(self, game, x, y, text, checked, callback):
        self.game = game
        self.x = x
        self.y = y
        self.text = text
        self.isChecked = checked
        self.color = (10,10,10)
    def draw(self):
        if self.isChecked:
            self.color = (240,240,240)
        else:
            self.color = (10, 10, 10)

        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, 32, 32))
    def update(self):
        pass

checkboxes = []

def create(game, x, y, text, state, callback):
    _box = Checkbox(game, x, y, text, state, callback)
    checkboxes.append(_box)

def remove(game):
    checkboxes.clear()   

def update(game):
    for box in checkboxes:
        box.update()

def draw(game):
    for box in checkboxes:
        box.draw()
