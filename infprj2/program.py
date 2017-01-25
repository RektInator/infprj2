# Imports
import pygame

# Import game states
import escmenu
import end
import game
import options
import mainmenu
import button
import translate
import menumusic
import config
import database
import background
import questions
import checkbox
import textbox
import player
import highscores
import listbox
import serverlist
import instructions
import lobby

class Game:
    def __init__(self):
        self.state = 0              # state 0 = mainmenu
        self.last_state = 0

        # Game variables
        self.players = []
        self.playercount = 0
        self.current_player = 0
        self.has_started = False
        self.question = 0
        self.chosen = []
        self.winner = ""
    
        # Start PyGame
        pygame.init()
        pygame.font.init()

		# Init game funcs
        database.init()
        config.init()
        translate.init()
        menumusic.init()
        questions.init()

        # Initiate the game window
        self.width = 800
        self.height = 600
        
        # Set the resolution
        self.screen = pygame.display.set_mode((self.width, self.height))

    def save(self):
        # save game information in the database
        sid = database.insert("INSERT INTO savegames (players, currentplayer) VALUES ('{}', '{}')".format(self.playercount, self.current_player))
        
        # save each player in the database
        for x in self.players:
            x.save(sid)

        # go to the main menu after saving our data
        self.set_state(0)
        self.has_started = False

    def load(self, sid):
        # load game data into the database
        res = database.execute_query("SELECT * FROM savegames WHERE id = '{}'".format(sid))

        # get game info
        self.playercount = res[0]["players"]
        self.current_player = res[0]["currentplayer"]

        # get info for each player
        res = database.execute_query("SELECT * FROM savegames_player WHERE sid = '{}'".format(sid))

        # loop through all players and load playerdata
        for x in res:
            plr = player.Player(self)
            plr.load(x)
            self.players.append(plr)

        # set state to ingame
        self.set_state(2)
        self.has_started = True

    def get_current_player(self):
        return self.players[self.current_player]

    def set_next_player(self):

        self.get_current_player().did_roll = False
        self.get_current_player().did_answer = False
        self.get_current_player().did_generate_question = False
        self.get_current_player().dice_roll = 0
        self.get_current_player().our_turn = False
        self.get_current_player().set_direction(None)

        self.current_player += 1

        if self.current_player == self.playercount:
            self.current_player = 0
        self.get_current_player().our_turn = True

    def set_current_player(self, idx):
        self.current_player = idx

    def get_last_player(self):
        idx = self.current_player
        if idx == 0:
            idx = self.playercount - 1
        else:
            idx -= 1

        return self.players[idx]

    # sets the current game state
    def set_state(self, state):
        checkbox.remove(self)
        textbox.remove(self)
        listbox.remove(self)

        self.last_state = self.state
        self.state = state          # update game state

        if self.state == 0:    
            mainmenu.init(self)
        elif self.state == 1:
            options.init(self)
        elif self.state == 2:
            game.init(self)
        elif self.state == 3:
            end.init(self)
        elif self.state == 4:
            escmenu.init(self)
        elif self.state == 5:
            highscores.init(self)
        elif self.state == 6:
            serverlist.init(self)
        elif self.state == 7:
            instructions.init(self)
        elif self.state == 8:
            lobby.init(self)

    # updates the game state
    def update(self):
        button.update(self)
        checkbox.update(self)
        textbox.update(self)
        listbox.update(self)

        if self.state == 0:    
            mainmenu.update(self)
        elif self.state == 1:
            options.update(self)
        elif self.state == 2:
            game.update(self)
        elif self.state == 3:
            end.update(self)
        elif self.state == 4:
            escmenu.update(self)
        elif self.state == 5:
            highscores.update(self)
        elif self.state == 6:
            serverlist.update(self)
        elif self.state == 7:
            instructions.update(self)
        elif self.state == 8:
            lobby.update(self)

    # draws the current frame
    def draw(self):
        # draw the background
        self.screen.fill((0, 0, 0))

        # Draw the correct data
        if self.state == 0:
            mainmenu.draw(self)
        elif self.state == 1:
            options.draw(self)
        elif self.state == 2:
            game.draw(self)
        elif self.state == 3:
            end.draw(self)
        elif self.state == 4:
            escmenu.draw(self)
        elif self.state == 5:
            highscores.draw(self)
        elif self.state == 6:
            serverlist.draw(self)
        elif self.state == 7:
            instructions.draw(self)
        elif self.state == 8:
            lobby.draw(self)

        # Flip buffer
        pygame.display.flip()

    # game loop
    def loop(self):
        while process_events():
            self.update()
            self.draw()

    # Add all functions that require shutdown here
    def exit(self):
        config.quit()
        database.quit()
        quit()

_game = Game()

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _game.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button.click(event.pos)
            checkbox.click(event.pos)
            textbox.click(event.pos)
            listbox.click(event.pos)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if _game.state == 2:
                _game.state = 4
            elif _game.state == 4:
                _game.state = 2
        elif event.type == pygame.KEYDOWN:
            textbox.key_event(event)
        
    return True

# main function
def Program():
    # _game = Game()
    _game.loop()

# Start the game
Program()