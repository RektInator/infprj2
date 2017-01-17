# Button class to make button drawing easier in pygame.
# Micky Langeveld

# Import pygame
import pygame

# button array
buttons = []

# button class
class Button:
    def __init__(self, game, x, y, width, height, text, size, backcolor, frontcolor, callback):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.backcolor = backcolor
        self.frontcolor = frontcolor
        self.callback = callback
        self.font = pygame.font.Font(None, size)
    def draw(self):
        pygame.draw.rect(self.game.screen, self.backcolor, (self.x, self.y, self.width, self.height))
        self.btn_text = self.font.render(self.text, 1, self.frontcolor)
        self.game.screen.blit(self.btn_text, (self.x, self.y))
    def click(self):
        self.callback()

# this function is fired when a mouse button is clicked
def click(pos):
    # loop through buttons
    for btn in buttons:
        # check if mouse position is within our range of interest
        if pos[0] > btn.x and pos[0] < btn.width + btn.x:
            if pos[1] > btn.y and pos[1] < btn.height + btn.y:
                # execute button callback
                btn.click()

                # Buttons shouldn't overlap. Break loop to increase performance
                break

# clear buttons this frame
def update():
    buttons.clear()

# create new buttons
def create(game, x, y, width, height, text, size, backcolor, frontcolor, callback):
    _btn = Button(game, x, y, width, height, text, size, backcolor, frontcolor, callback)
    _btn.draw()

    buttons.append(_btn)