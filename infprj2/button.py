# Button class to make button drawing easier in pygame.
# Micky Langeveld

# Import pygame
import pygame

# button array
buttons = []

# button class
class Button:
    def __init__(self, game, x, y, width, height, text, size, backcolor, frontcolor, callback, image, outline=True):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size
        self.backcolor = backcolor
        self.frontcolor = frontcolor
        self.callback = callback
        self.font = pygame.font.Font(None, size)
        self.image = image
        self.outline = outline
    def draw(self):
        textsize = self.font.size(self.text)
        
        if len(self.image):
            self.game.screen.blit(pygame.image.load(self.image), (self.x, self.y))
        else:
            if self.outline == True:
                pygame.draw.rect(self.game.screen, (255,255,255), (self.x-1, self.y-1, self.width+2, self.height+2))
            pygame.draw.rect(self.game.screen, self.backcolor, (self.x, self.y, self.width, self.height))
        self.btn_text = self.font.render(self.text, 1, self.frontcolor)
        self.game.screen.blit(self.btn_text, (self.x + self.width/2 - (textsize[0]/2), self.y + self.height/2 - (textsize[1]/2)))
    def click(self):
        self.callback(self.game)

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
def update(game):
    buttons.clear()

# create new buttons
def draw(game, x, y, width, height, text, size, backcolor, frontcolor, callback):
    # alloc button
    _btn = Button(game, x, y, width, height, text, size, backcolor, frontcolor, callback, "")
    _btn.draw()

    # add button to list
    buttons.append(_btn)

def draw_img(game, x, y, width, height, text, size, image, frontcolor, callback):
    # alloc button
    _btn = Button(game, x, y, width, height, text, size, (0, 0, 0), frontcolor, callback, image)
    _btn.draw()

    # add button to list
    buttons.append(_btn)