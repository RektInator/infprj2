# Options menu python file
import pygame
import button
import checkbox
import config
import menumusic
import textbox

def update(game):
    pass

def onBackgroundMusicChanged(game):
    if config.get("snd_enabled") == "1":
        config.set("snd_enabled", "0")
        menumusic.stop()
    else:
        config.set("snd_enabled", "1")
        menumusic.init()

def textChanged(game, box):
    pass

def init(game):
    # add checkboxes for settings here
    checkbox.create(game, 64, 64, "Muziek", int(config.get("snd_enabled")), onBackgroundMusicChanged) 

    # add textfields for settings here
    textbox.create(game, 64, 100, 200, "test", textChanged)

def draw(game):
    bg = pygame.image.load("assets/img/bg.png")
    game.screen.blit(bg,(0,0))

    checkbox.draw(game)
    textbox.draw(game)
    button.draw(game, 10, 10, game.width / 10, game.height / 20, "terug", 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))