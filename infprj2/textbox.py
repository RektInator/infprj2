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
        self.focuspos = 0
    def draw(self):
        pygame.draw.rect(self.game.screen, (0,0,0), (self.x-1, self.y-1, self.width+2, self.height+2))
        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.width, self.height))
        textsize = self.font.size(self.text[:self.focuspos])
        if self.isFocussed == True and math.floor(((time.clock() - self.timer) / 0.5) % 2) == 0:
            pygame.draw.line(self.game.screen, (0,0,0), (self.x + textsize[0] + 3, self.y + 7), (self.x + textsize[0] + 3, self.y + 22))
        self.btn_text = self.font.render(self.text, 1, (0,0,0))
        self.game.screen.blit(self.btn_text, (self.x + 3, self.y + self.height/2 - (textsize[1]/2)))
    def click(self, pos):
        self.isFocussed = True
        for x in range(len(self.text)):
            if abs(self.font.size(self.text[:x])[0] + self.x - pos[0] + 2) < 4:
                self.focuspos = x
        if self.font.size(self.text)[0] + self.x - pos[0] < 0:
            self.focuspos = len(self.text)
    def unfocus(self):
        self.isFocussed = False
        self.focuspos = len(self.text)
    def key_pressed(self, event):

        enterPressed = False
        self.timer = time.clock()

        # A-Z
        if event.key >= 65 and event.key <= 90:
            self.text = self.text[0:self.focuspos] + chr(event.key) + self.text[self.focuspos:]
            self.focuspos += 1

        # a-z
        if event.key >= 97 and event.key <= 122:
            self.text = self.text[0:self.focuspos] + chr(event.key) + self.text[self.focuspos:]
            self.focuspos += 1

        # special characters, numeric values
        if event.key >= 32 and event.key <= 64:
            self.text = self.text[0:self.focuspos] + chr(event.key) + self.text[self.focuspos:]
            self.focuspos += 1

        # enter pressed
        if event.key == 13:
            enterPressed = True
            if self.game.state != 2:
                self.isFocussed = False

        if event.key == pygame.K_F1:
            self.text = self.text[0:self.focuspos] + "(" + self.text[self.focuspos:]
            self.focuspos += 1

        if event.key == pygame.K_F2:
            self.text = self.text[0:self.focuspos] + ")" + self.text[self.focuspos:]
            self.focuspos += 1

        if event.key == pygame.K_F3:
            self.text = self.text[0:self.focuspos] + '"' + self.text[self.focuspos:]
            self.focuspos += 1

        if event.key == pygame.K_RIGHT:
            if self.focuspos < len(self.text):
                self.focuspos += 1

        if event.key == pygame.K_LEFT:
            if self.focuspos > 0:
                self.focuspos -= 1

        # backspace pressed
        if event.key == 8:
            if len(self.text) >= 1 and self.focuspos != 0:
                self.text = self.text[0:self.focuspos - 1] + self.text[self.focuspos:]
            if self.focuspos > 0:
                self.focuspos -= 1

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
                btn.click(pos)
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
