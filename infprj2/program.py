# Imports
import pygame
import mainmenu

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    
    return True

class Game:
    def __init__(self):
        self.state = 0              # state 0 = mainmenu

        # Initiate the game window
        self.width = 640
        self.height = 480
        
        # Start PyGame
        pygame.init()
        
        # Set the resolution
        self.screen = pygame.display.set_mode((self.width, self.height))

    # sets the current game state
    def set_state(self, state):
        self.state = state          # update game state

    # updates the game state
    def update(self):
        if self.state == 0:
            mainmenu.update(self)

    # draws the current frame
    def draw(self):
        if self.state == 0:
            mainmenu.draw(self)

    # game loop
    def loop(self):
        while process_events():
            self.update()
            self.draw()
            pygame.display.flip()

# main function
def Program():
    game = Game()
    game.loop()

# Start the game
Program()