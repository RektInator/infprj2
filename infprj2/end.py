# End-screen python file
import pygame
import button
import translate

def update(game):
    pass

def init(game):
    pass

def draw(game):
    # Termination screen colour
    game.screen.fill((160, 187, 194))
    font = pygame.font.Font("Helvetica", 72)

    # Termination screen text + colour
    label_1 = font.render(translate.translate("PLAYER_WON"), 1, (255,8,148))
    size = font.size(translate.translate("PLAYER_WON"))

    # Placement text in screen
    game.screen.blit(label_1,(int(game.width/2 - (size[0]/2)), game.height*0.1 - (size[1]/2)))
    
    bg = pygame.image.load("assets/Lego_met_vlag4.png")
    game.screen.blit(bg,(game.width/2.4 ,game.height*0.2 ))

    # button variables
    btn_width = game.width / 5;
    btn_height = game.height / 10;
    btn_x_off = (game.width / 2) - (btn_width / 2)
    btn_y_off = lambda idx: (game.height / 10) * (idx + 1) + (idx * 10)

    button.draw(game, btn_x_off, btn_y_off(6), int(btn_width), int(btn_height), translate.translate("BACK"), 20, (25,25,25), (255,255,255), lambda x: game.set_state(0))