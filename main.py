#!/usr/bin/python3
# -*- coding: utf-8 -*

"""4 in a row game with pygame"""

import os
import tkinter as tk

from pygame import *

init()

# Setup display

root = tk.Tk()

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenheight()

HEIGHT = 800
WIDTH = 600

win_x = screen_width // 2 - WIDTH // 2
win_y = screen_height // 2 - HEIGHT // 2

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{win_x},{win_y}"
win = display.set_mode((WIDTH, HEIGHT)) # main window
display.set_caption("4 in a row")

SIZE = WIDTH # grid size

Y = HEIGHT // 2 - SIZE // 2

grid_surface = Surface((SIZE, SIZE), SRCALPHA) # window containing only the grid

# Colors 
BACKGROUND = (37, 34, 51)
GRID = (57, 51, 77)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Games settings

grid = [['E' for _ in range(7)] for _ in range(5)]
grid.append(['A' for _ in range(7)])

# Setup game loop

FPS = 30
clock = time.Clock()
run = True

def draw_grid(surface, background, red, yellow, grid):
    """Draw the grid and the tokens in it"""

    s = surface.get_width() # width of the grid_surface
    w = s // 7 # width of a square
    pt = (s - (6 * w)) // 2  
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in 'AE':
                draw.circle(surface, background, (w//2+j*w, pt+w//2+i*w), w*42//100)

win.fill(BACKGROUND)
grid_surface.fill(GRID)
draw_grid(grid_surface, BACKGROUND, RED, YELLOW, grid)
win.blit(grid_surface, (0, Y))
display.update()

while run:
    clock.tick(FPS)

    events = event.get()

    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            run = False

quit()