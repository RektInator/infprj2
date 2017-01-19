# End-screen python file
import pygame

def update(game):
    pass

def init(game):
    pass

def draw(game):
    # Termination screen colour
    game.screen.fill((199, 251, 126))
    font = pygame.font.Font(None, 72)

    # Termination screen text + colour
    label_1 = font.render("Gewonnen!!", 1, (255,8,148))
    size = font.size("Gewonnen!!")

    # Placement text in screen
    game.screen.blit(label_1,(int(game.width/2 - (size[0]/2)), game.height/2 - (size[1]/2)))
    