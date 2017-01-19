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


def onLanguageChanged(game):
    if config.get("lang_select") == "0":
        config.set("lang_select", "1")
    else:
        config.set("lang_select", "0")
   


def init(game):
    # add checkboxes for settings here
    checkbox.create(game, 64, 64, "Muziek", int(config.get("snd_enabled")), onBackgroundMusicChanged)
    checkbox.create(game, 64, 128, "Taal", int(config.get("lang_select")), onLanguageChanged)

def draw(game):
    bg = pygame.image.load("assets/img/bg.png")
    game.screen.blit(bg,(0,0))
    game.screen.blit((pygame.font.Font(None, 20)).render("Herstart spel voor verandering", 1, (98,212,123)),(game.height * 0.5,game.width * 0.5))
    checkbox.draw(game)
    button.draw(game, 10, 10, game.width / 10, game.height / 20, "terug", 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))
    