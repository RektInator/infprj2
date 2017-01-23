# Escape menu
import pygame
import button
import translate

def update(game):
    pass

def init(game):
    pass

def draw(game):
    # button variables
    btn_width = game.width / 5;
    btn_height = game.height / 10;
    btn_x_off = (game.width / 2) - (btn_width / 2)
    btn_y_off = lambda idx: (game.height / 10) * (idx + 1) + (idx * 10)

    # "Pauze" tekst
    # Todo

    #             scr,  x offset,  y offset,     width,          height,          text,  fontsize,  backcolor,  frontcolor,    callback
    button.draw(game, btn_x_off, btn_y_off(2), int(btn_width), int(btn_height), translate.translate("BACK"), 20,      (25,25,25), (255,255,255), lambda x: game.set_state(2))
    button.draw(game, btn_x_off, btn_y_off(3), int(btn_width), int(btn_height), translate.translate("OPTIONS"), 20,      (25,25,25), (255,255,255), lambda x: game.set_state(1))
    button.draw(game, btn_x_off, btn_y_off(4), int(btn_width), int(btn_height), "Save", 20,      (25,25,25), (255,255,255), lambda game: game.save())
    button.draw(game, btn_x_off, btn_y_off(5), int(btn_width), int(btn_height), translate.translate("QUIT"), 20,      (25,25,25), (255,255,255), lambda x: game.exit())
