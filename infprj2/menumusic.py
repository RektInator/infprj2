# Import pygame
import pygame
import config

def load(file):
    pygame.mixer.music.load(file)

def play():
    pygame.mixer.music.play(-1)

def stop():
    pygame.mixer.music.stop()

def init():
    # Check if menu music should be enabled
    if config.get("snd_enabled") == True:
        load("background.mp3")
        play()