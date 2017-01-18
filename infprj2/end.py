# End-screen python file
import pygame

def update(game):
    pass

def draw(game):
    game.screen.fill((199, 251, 126))
    font = pygame.font.Font(None, 72)
    label_1 = font.render("Gewonnen!! (ﾉ◕ヮ◕)ﾉ*:・ﾟ✧", 1, (255,8,148))
    size = font.size("Gewonnen!!")
    game.screen.blit(label_1,(int(game.width/2 - (size[0]/2)), game.height/2 - (size[1]/2)))
    