# End-screen python file
import pygame

def update(game):
    pass

def draw(game):
    font = pygame.font.Font(None, 48)
    label_1 = font.render("Gewonnen!!", 1, (255,8,148))
    size = font.size("Gewonnen!!")
    game.screen.blit(label_1,(int(game.width/2 - (size[0]/2)), 32))