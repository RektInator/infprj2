# End-screen python file
import pygame
import button
import translate
import database


class ScoreDef:
    def __init__(self, name, score):
        self.name = name
        self.score = score

scores = []

def update(game):
    pass

def init(game):
    refresh(game)
    pass

def refresh(game):
    # Clear existing score definitions
    scores.clear()

    # Fetch new scores
    res = database.execute_query("SELECT accounts.username as name, score.score as score FROM score,accounts WHERE score.id = accounts.id ORDER BY score.score DESC")

    # Add scores to list
    for row in res:
        idx = ScoreDef(row["name"], row["score"])
        scores.append(idx)

def draw(game):
    button.draw(game, 670, 32, 100, 32, translate.translate("REFRESH"), 20, (0,0,0), (255,255,255), refresh)
    button.draw(game, 32, 32, 100, 32, translate.translate("BACK"), 20, (0,0,0), (255,255,255), lambda game: game.set_state(0))

    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 28)

    name = font.render(translate.translate("PLAYER"), 1, (255,255,255))
    score = font.render("SCORE", 1, (255,255,255))

    pygame.draw.line(game.screen,(255,255,255),(180,91),(320,91))
    pygame.draw.line(game.screen,(255,255,255),(480,91),(610,91))

    game.screen.blit(name, (200, 64))
    game.screen.blit(score, (500, 64))

    idx = 0;
    for x in scores:
        if idx >= 10:
            break

        uname = font2.render(x.name, 1, (255,255,255))
        pscore = font2.render(str(x.score), 1, (255,255,255))

        game.screen.blit(uname, (200, 100 + (idx * 28)))
        game.screen.blit(pscore, (500, 100 + (idx * 28)))

        idx += 1

    pass
