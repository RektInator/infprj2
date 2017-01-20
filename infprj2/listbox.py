import pygame

def update(game):
    pass

class Column:
    def __init__(self, width, title):
        self.width = width
        self.title = title

class Listbox:
    def __init__(self, game, x, y, width, max_items, columns, ondraw, onclick):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = max_items * 20
        self.item_count = 0
        self.columns = columns
        self.ondraw = ondraw
        self.onclick = onclick
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
            for idx in range(0, self.item_count):
                colval = self.ondraw(self.game, idx, column_idx)
                collabel = hdrfont.render(colval, 1, (255,255,255))
                self.game.screen.blit(collabel, (column_width_start, self.y + 24 + (26 * idx)))

            # increment values
            column_width_start += col.width
            column_idx += 1

    def update(self):
        pass

listboxes = []

def remove(game):
    listboxes.clear()

def create(game, x, y, width, item_count, columns, ondraw, onclick):
    _box = Listbox(game, x, y, width, item_count, columns, ondraw, onclick)
    listboxes.append(_box)

    return _box

def update(game):
    pass

def draw(game):
    for listbox in listboxes:
        listbox.draw()

def click(game):
    pass