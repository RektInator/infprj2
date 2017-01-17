# Imports
import pygame

# Import game states
import end
import game
import options
import mainmenu
import button

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button.click(event.pos)
        
    return True

class Game:
    def __init__(self):
        self.state = 0              # state 0 = mainmenu

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

    # draws the current frame
    def draw(self):
        
        # Clear the screen
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

        # Flip buffer
        pygame.display.flip()

    # game loop
    def loop(self):
        while process_events():
            self.update()
            self.draw()

# main function
def Program():
    game = Game()
    game.loop()

# Start the game
Program()