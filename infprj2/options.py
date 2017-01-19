# Options menu python file
import pygame
import button
import checkbox
import config
import menumusic

def update(game):
    pass

def onBackgroundMusicChanged(game):
    if config.get("snd_enabled") == "1":
        config.set("snd_enabled", "0")
        menumusic.stop()
    else:
        config.set("snd_enabled", "1")
        menumusic.init()

def init(game):
    checkbox.create(game, 64, 64, "Muziek", int(config.get("snd_enabled")), onBackgroundMusicChanged) 

def draw(game):
    checkbox.draw(game)
    button.draw(game, 10, 10, game.width / 10, game.height / 20, "terug", 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))