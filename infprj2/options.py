# Options menu python file
import pygame
import button
import checkbox
import config
import menumusic
import textbox
import translate

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
    if config.get("lang_select") == "1":
        config.set("lang_select", "0")
        translate.clear()
        translate.init()
    else:
        config.set("lang_select", "1")
        translate.clear()
        translate.init()

def textChanged(game, box, enterPressed):
    pass

def init(game):
    # add checkboxes for settings here
    checkbox.create(game, 64, 64, translate.translate("MUSIC"), int(config.get("snd_enabled")), onBackgroundMusicChanged) 
    checkbox.create(game, 64, 100, translate.translate("LANGUAGE"), int(config.get("lang_select")), onLanguageChanged)

def draw(game):
    # bg = pygame.image.load("assets/img/bg.png")
    # game.screen.blit(bg,(0,0))

    checkbox.draw(game)
    textbox.draw(game)
    button.draw(game, 10, 10, game.width / 10, game.height / 20, translate.translate("BACK"), 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))