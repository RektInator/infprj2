# End-screen python file
import pygame

def update(game):
    pass

def draw(game):
    font = pygame.font.Font(None, 20)
    label_1 = font.render("Tekst hier", 1, (255,255,225))
    game.screen.blit(label_1, (32, 32))