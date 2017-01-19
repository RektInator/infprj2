# Import pygame
import pygame

# Textbox class
class Textbox:
    def __init__(self, x, y, width, height, backcolor, frontcolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.backcolor = backcolor
        self.frontcolor = frontcolor
        
textfields = []

# todo....
def draw(x, y, width, height, backcolor, frontcolor):
    _txt = Textbox(x, y, width, height, backcolor, frontcolor)
    textfields.append(_txt)