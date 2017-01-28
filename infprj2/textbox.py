# Import pygame
import pygame
import time
import math

class Textbox:
    def __init__(self, game, x, y, width, text, callback):
        self.game = game
        self.x = x
        self.y = y
        self.text = text
        self.color = (255,255,255)
        self.callback = callback
        self.width = width
        self.height = 32
        self.font = pygame.font.Font(None, 20)
        self.isFocussed = False
        self.timer = time.clock()
    def draw(self):
        pygame.draw.rect(self.game.screen, (0,0,0), (self.x-1, self.y-1, self.width+2, self.height+2))
        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.width, self.height))
        textsize = self.font.size(self.text)
        if self.isFocussed == True and math.floor(((time.clock() - self.timer) / 0.5) % 2) == 0:
            pygame.draw.line(self.game.screen, (0,0,0), (self.x + textsize[0] + 5, self.y + 7), (self.x + textsize[0] + 5, self.y + 22))
        self.btn_text = self.font.render(self.text, 1, (0,0,0))
        self.game.screen.blit(self.btn_text, (self.x + 3, self.y + self.height/2 - (textsize[1]/2)))
    def click(self):
        self.isFocussed = True
    def unfocus(self):
        self.isFocussed = False
    def key_pressed(self, event):

        enterPressed = False
        self.timer = time.clock()

        # A-Z
        if event.key >= 65 and event.key <= 90:
            self.text += chr(event.key)

        # a-z
        if event.key >= 97 and event.key <= 122:
            self.text += chr(event.key)

        # special characters, numeric values
        if event.key >= 32 and event.key <= 64:
            self.text += chr(event.key)

        # enter pressed
        if event.key == 13:
            enterPressed = True
            self.isFocussed = False

        if event.key == pygame.K_F1:
            self.text += "("

        if event.key == pygame.K_F2:
            self.text += ")"

        if event.key == pygame.K_F3:
            self.text += '"'

        # backspace pressed
        if event.key == 8:
            if len(self.text) >= 1:
                self.text = self.text[0:len(self.text) - 1]

        # Execute textChanged callback
        self.callback(self.game, self, enterPressed)

    def update(self):
        pass

textfields = []

# this function is fired when a mouse button is clicked
def click(pos):
    # loop through textfields
    for btn in textfields:
        # check if mouse position is within our range of interest
        if pos[0] > btn.x and pos[0] < btn.width + btn.x:
            if pos[1] > btn.y and pos[1] < btn.height + btn.y:
                # execute button callback
                btn.click()
            else:
                btn.unfocus()
        else:
            btn.unfocus()

# trigger keyevent for the focussed textfield
def key_event(event):
    for btn in textfields:
        if btn.isFocussed:
            btn.key_pressed(event)
            break

# creates a text field
def create(game, x, y, width, text, callback):
    _box = Textbox(game, x, y, width, text, callback)
    textfields.append(_box)

# removes all textfields
def remove(game):
    textfields.clear()   

# updates all textfields
def update(game):
    for box in textfields:
        box.update()

# draws all textfields
def draw(game):
    for box in textfields:
        box.draw()
