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

def onBackgroundMusicChanged(game,box):
    if config.get("snd_enabled") == "1":
        config.set("snd_enabled", "0")
        menumusic.stop()
    else:
        config.set("snd_enabled", "1")
        menumusic.init()

def onLanguageChanged(game,box):
    if config.get("lang_select") == "1":
        config.set("lang_select", "0")
        translate.clear()
        translate.init()
    else:
        config.set("lang_select", "1")
        translate.clear()
        translate.init()

def onDeveloperChanged(game,box):
    if config.get("developer_mode") == "1":
        config.set("developer_mode", "0")
    else:
        config.set("developer_mode", "1")

def textChanged(game, box, enterPressed):
    pass

def init(game):
    # add checkboxes for settings here
    checkbox.create(game, game.width * 0.3 , game.height * 0.325, translate.translate("MUSIC"), int(config.get("snd_enabled")), onBackgroundMusicChanged) 
    checkbox.create(game, game.width * 0.3, game.height * 0.475, translate.translate("LANGUAGE"), int(config.get("lang_select")), onLanguageChanged)
    checkbox.create(game, game.width * 0.3, game.height * 0.625, "Dev mode", int(config.get("developer_mode")), onDeveloperChanged)

def draw(game):
    pygame.draw.rect(game.screen,(255,255,255),(game.width * 0.2,game.height * 0.2,game.width * 0.55,game.height * 0.6))
    pygame.draw.rect(game.screen,(0,0,0),(game.width * 0.22,game.height * 0.23,game.width * 0.51,game.height * 0.55))
    bg = pygame.image.load("assets/euros.png")
    game.screen.blit(bg,(game.width * 0.7 ,game.height * 0.35))
    checkbox.draw(game)
    textbox.draw(game)
    button.draw(game, 10, 10, game.width / 10, game.height / 20, translate.translate("BACK"), 20, (25,25,25), (255,255,255), lambda x: game.set_state(game.last_state))

