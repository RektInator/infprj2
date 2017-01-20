import pygame

def update(game):
    pass

class Column:
    def __init__(self, width, title):
        self.width = width
        self.title = title

class Listbox:
    def __init__(self, game, x, y, width, item_count, columns):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = item_count * 20
        self.item_count = item_count
    def draw(self):
        pass
    def update(self):
        pass

listboxes = []

def remove(game):
    listboxes.clear()

def add(game, x, y, width, item_count, columns):
    listboxes.append(Listbox(game, x, y, width, item_count, columns))

def draw(game):
    pass

def click(game):
    pass