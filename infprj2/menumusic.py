# Import pygame
import pygame
import config
from pygame import mixer

mixer.init()

def load(file):
    pygame.mixer.music.load(file)

def play():
    pygame.mixer.music.play(-1)

def stop():
    pygame.mixer.music.stop()

def init():
    # Check if menu music should be enabled
    if config.get("snd_enabled") == "1":
        load("assets/background.mp3")
        play()

#Different sounds
applause_snd = pygame.mixer.Sound("assets/applause6.wav")
yay_snd = pygame.mixer.Sound("assets/yay.wav")
correct_snd = pygame.mixer.Sound("assets/Correct sound.wav")
wrong_snd = pygame.mixer.Sound("assets/Wrong sound.wav")
