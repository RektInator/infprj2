import pygame

class Column:
    def __init__(self, width, title):
        self.width = width
        self.title = title

class Listbox:
    def __init__(self, game, x, y, width, max_items, columns, ondraw, onclick, onupdate):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = max_items * 20
        self.item_count = 0
        self.columns = columns
        self.ondraw = ondraw
        self.onclick = onclick
        self.onupdate = onupdate
        self.start_idx = 0                  # for future scrollbars
    def set_rows(self, cnt):
        self.item_count = cnt
    def draw(self):
        
        # column header font
        hdrfont = pygame.font.Font(None, 36)

        # column text font
        colfont = pygame.font.Font(None, 20)

        column_idx = 0
        column_width_start = self.x

        for col in self.columns:
            # render header
            name = hdrfont.render(col.title, 1, (255,255,255))
            self.game.screen.blit(name, (column_width_start, self.y))

            # draw items in list
            for idx in range(self.start_idx + self.item_count):
        
                # show a maximum of 15 values in the list
                if idx >= 15:
                    break

                # draw column data
                colval = self.ondraw(self.game, idx, column_idx)
                collabel = colfont.render(colval, 1, (255,255,255))
                self.game.screen.blit(collabel, (column_width_start, self.y + 24 + (22 * idx)))
                # print("Entry {} is {}".format(idx, colval))

            # increment values
            column_width_start += col.width
            column_idx += 1

    def click(self, pos):
        pass

    def update(self):
        self.onupdate(self.game, self)

listboxes = []

def remove(game):
    listboxes.clear()

def update(game):
    for listbox in listboxes:
        listbox.update()

def create(game, x, y, width, item_count, columns, ondraw, onclick, onupdate):
    _box = Listbox(game, x, y, width, item_count, columns, ondraw, onclick, onupdate)
    listboxes.append(_box)

def draw(game):
    for listbox in listboxes:
        listbox.draw()

# this function is fired when a mouse button is clicked
def click(pos):
    # loop through buttons
    for btn in listboxes:
        # check if mouse position is within our range of interest
        if pos[0] > btn.x and pos[0] < btn.width + btn.x:
            if pos[1] > btn.y and pos[1] < btn.height + btn.y:
                # execute button callback
                btn.click(pos)

                # Buttons shouldn't overlap. Break loop to increase performance
                break