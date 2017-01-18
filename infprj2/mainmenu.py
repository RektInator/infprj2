# Main menu python file
import pygame

# Import button lib
import button

def update(game):
    pass

def draw(game):
    # button variables
    btn_width = game.width / 5;
    btn_height = game.height / 10;
    btn_x_off = (game.width / 2) - (btn_width / 2)
    btn_y_off = lambda idx: (game.height / 10) * (idx + 1) + (idx * 10)

    #             scr,  x offset,  y offset,     width,          height,          text,  fontsize,  backcolor,  frontcolor,    callback
    button.draw(game, btn_x_off, btn_y_off(2), int(btn_width), int(btn_height), "Start", 20,      (25,25,25), (255,255,255), lambda: game.set_state(2))
    button.draw(game, btn_x_off, btn_y_off(3), int(btn_width), int(btn_height), "Opties", 20,     (25,25,25), (255,255,255), lambda: game.set_state(1))
    # button.draw(game, btn_x_off, btn_y_off(4), int(btn_width), int(btn_height), "Afsluiten", 20,  (25,25,25), (255,255,255), quit())
    