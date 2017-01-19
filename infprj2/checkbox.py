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
        self.callback = callback
        self.width = 32
        self.height = 32
        self.font = pygame.font.Font(None, 20)
    def draw(self):
        if self.isChecked:
            self.color = (240,240,240)
        else:
            self.color = (10, 10, 10)

        textsize = self.font.size(self.text)
        self.btn_text = self.font.render(self.text, 1, (255,255,255))
        self.game.screen.blit(self.btn_text, (self.x + 48, self.y + self.height/2 - (textsize[1]/2)))

        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.width, self.height))
    def click(self):
        self.isChecked = not self.isChecked
        self.callback(self.game)
    def update(self):
        pass

checkboxes = []

# this function is fired when a mouse button is clicked
def click(pos):
    # loop through buttons
    for btn in checkboxes:
        # check if mouse position is within our range of interest
        if pos[0] > btn.x and pos[0] < btn.width + btn.x:
            if pos[1] > btn.y and pos[1] < btn.height + btn.y:
                # execute button callback
                btn.click()

                # Buttons shouldn't overlap. Break loop to increase performance
                break

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
