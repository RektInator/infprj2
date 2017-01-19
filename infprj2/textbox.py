# Import pygame
import pygame

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
    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.width, self.height))
        textsize = self.font.size(self.text)
        self.btn_text = self.font.render(self.text, 1, (0,0,0))
        self.game.screen.blit(self.btn_text, (self.x + 3, self.y + self.height/2 - (textsize[1]/2)))
    def click(self):
        self.isFocussed = True
    def unfocus(self):
        self.isFocussed = False
    def key_pressed(self, event):
        # A-Z
        if event.key >= 65 and event.key <= 90:
            self.text += chr(event.key)
        # a-z
        if event.key >= 97 and event.key <= 122:
            self.text += chr(event.key)

        # numeric values
        if event.key >= 48 and event.key <= 57:
            self.text += chr(event.key)

        # other keys
        if event.key == 32:
            self.text += chr(event.key)

        # enter pressed
        if event.key == 13:
            self.isFocussed = False

        # backspace pressed
        if event.key == 8:
            if len(self.text) >= 1:
                self.text = self.text[0:len(self.text) - 1]

        # Execute textChanged callback
        self.callback(self.game, self, True)

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

                # Buttons shouldn't overlap. Break loop to increase performance
                break
            else:
                btn.unfocus()
        else:
            btn.unfocus()

def key_event(event):
    for btn in textfields:
        if btn.isFocussed:
            btn.key_pressed(event)
            break

def create(game, x, y, width, text, callback):
    _box = Textbox(game, x, y, width, text, callback)
    textfields.append(_box)

def remove(game):
    textfields.clear()   

def update(game):
    for box in textfields:
        box.update()

def draw(game):
    for box in textfields:
        box.draw()
