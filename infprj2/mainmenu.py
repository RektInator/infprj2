# Main menu python file
import pygame
import translate
import database
import options
import instructions
# Import button lib
import button

def update(game):
    pass

def init(game):
    pass

def loadgame(game):
    game.players.clear()
    res = database.execute_query("SELECT * FROM savegames ORDER BY id DESC")
    game.load(res[0]["id"])

def draw(game):
    bg = pygame.image.load("assets/img/bg.png")
    game.screen.blit(bg,(0,0))

    # button variables
    btn_width = game.width / 5;
    btn_height = game.height / 10;
    btn_x_off = (game.width / 2) - (btn_width / 2)
    btn_y_off = lambda idx: (game.height / 10) * (idx + 1) + (idx * 10)

    #             scr,  x offset,  y offset,     width,          height,          text,  fontsize,  backcolor,  frontcolor,    callback
    button.draw(game, btn_x_off, btn_y_off(0), int(btn_width), int(btn_height), "Start", 20,      (25,25,25), (255,255,255), lambda x: game.set_state(2))
    button.draw(game, btn_x_off, btn_y_off(1), int(btn_width), int(btn_height), "Load", 20,      (25,25,25), (255,255,255), lambda x: loadgame(x))    
    button.draw(game, btn_x_off, btn_y_off(2), int(btn_width), int(btn_height), "Multiplayer", 20,      (25,25,25), (255,255,255), lambda x: game.set_state(6))    
    button.draw(game, btn_x_off, btn_y_off(3), int(btn_width), int(btn_height), translate.translate("OPTIONS"), 20,     (25,25,25), (255,255,255), lambda x: game.set_state(1))
    button.draw(game, btn_x_off, btn_y_off(4), int(btn_width), int(btn_height), translate.translate("INSTRUCTIONS"), 20,      (25,25,25), (255,255,255), lambda x: game.set_state(7))
    button.draw(game, btn_x_off, btn_y_off(5), int(btn_width), int(btn_height), "Leaderboard", 20,      (25,25,25), (255,255,255), lambda x: game.set_state(5))
    button.draw(game, btn_x_off, btn_y_off(6), int(btn_width), int(btn_height), translate.translate("QUIT"), 20,      (25,25,25), (255,255,255), lambda x: game.exit())
    # button.draw(game, btn_x_off, btn_y_off(7), int(btn_width), int(btn_height), "Afsluiten", 20,  (25,25,25), (255,255,255), game.exit())
    