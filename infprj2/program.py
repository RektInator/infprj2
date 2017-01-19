# Imports
import pygame

# Import game states
import escmenu
import end
import game
import options
import mainmenu
import button
import translate
import menumusic
import config
import score
import background

class Game:
    def __init__(self):
        self.state = 0              # state 0 = mainmenu
        self.last_state = 0

        # Game variables
        self.dice_roll = 0

		# Init game funcs
        config.init()
        translate.init()
        menumusic.init()

        # Initiate the game window
        self.width = 800
        self.height = 600
        
        # Start PyGame
        pygame.init()
        pygame.font.init()
        
        # Set the resolution
        self.screen = pygame.display.set_mode((self.width, self.height))

    # sets the current game state
    def set_state(self, state):
        self.last_state = self.state
        self.state = state          # update game state

    # updates the game state
    def update(self):
        button.update()

        if self.state == 0:    
            mainmenu.update(self)
        elif self.state == 1:
            options.update(self)
        elif self.state == 2:
            game.update(self)
        elif self.state == 3:
            end.update(self)
        elif self.state == 4:
            escmenu.update(self)

    # draws the current frame
    def draw(self):
        
        # draw the background
       
        self.screen.fill((0, 0, 0))

        # Draw the correct data
        if self.state == 0:
            mainmenu.draw(self)
        elif self.state == 1:
            options.draw(self)
        elif self.state == 2:
            game.draw(self)
        elif self.state == 3:
            end.draw(self)
        elif self.state == 4:
            escmenu.draw(self)

        # Flip buffer
        pygame.display.flip()

    # game loop
    def loop(self):
        while process_events():
            self.update()
            self.draw()

_game = Game()

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button.click(event.pos)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if _game.state == 2:
                _game.state = 4
            elif _game.state == 4:
                _game.state = 2
        
    return True

# main function
def Program():
    # _game = Game()
    _game.loop()

# Start the game
Program()