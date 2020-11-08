#!/usr/bin/python3
# -*- coding: utf-8 -*

"""4 in a row game with pygame"""

import os
import tkinter as tk

from pygame import *
from random import choice
init()

# Setup display

root = tk.Tk()

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenheight()

HEIGHT = screen_height * 80 // 100
WIDTH = HEIGHT * 75 // 100

win_x = screen_width // 2 - WIDTH // 2
win_y = screen_height // 2 - HEIGHT // 2

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{win_x},{win_y}"
win = display.set_mode((WIDTH, HEIGHT)) # main window
display.set_caption("4 in a row")

SIZE = WIDTH # grid size

Y = HEIGHT // 2 - SIZE // 2

grid_surface = Surface((SIZE, SIZE), SRCALPHA) # window containing only the grid
size_grid = grid_surface.get_width() # width of the grid surface
square_width = size_grid // 7

# Colors 
BACKGROUND = (37, 34, 51)
GRID = (57, 51, 77)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Games settings

grid = [['E' for _ in range(7)] for _ in range(5)]
grid.append(['A' for _ in range(7)])
player = True # wether the player or the bot plays

player_token = 'R'
bot_token = 'Y'

turns = 0

# Setup game loop

FPS = 30
clock = time.Clock()
run = True
play = True
changements = True

def bot(grid):
    """Choose the best column for the bot to play
    Return: int the number of the column"""
    cols = [] # list of columns with an available square
    for j in range(len(grid[0])): # iterate through each column
        col = [grid[i][j] for i in range(len(grid))]
        if 'A' in col: cols.append(j) # add column number if it has an available square
    return choice(cols)

def draw_grid(surface, background, red, yellow, grid, size_grid, square_width):
    """Draw the grid and the tokens in it"""

    s = size_grid
    w = square_width
    pt = (s - (6 * w)) // 2  
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in 'AE':
                draw.circle(surface, background, (w//2+j*w, pt+w//2+i*w), w*42//100)
            elif grid[i][j] == 'R':
                draw.circle(surface, red, (w//2+j*w, pt+w//2+i*w), w*42//100)
            elif grid[i][j] == 'Y':
                draw.circle(surface, yellow, (w//2+j*w, pt+w//2+i*w), w*42//100)

def won(grid):
    for i in range(len(grid)):
        for j in range(3):
            row = [grid[i][j + x] for x in range(3)]
            if not 'E' in row:
                if len(set(row)) == 1:
                    return True

    return False

while run:
    clock.tick(FPS)

    while play:

        if player: # player's turn
            for e in event.get():
                if e.type == QUIT:
                    play = False
                    run = False

                elif e.type == MOUSEBUTTONUP and e.button == 1:
                    pos = mouse.get_pos()
                    r = Rect(0, (HEIGHT - WIDTH) // 2, SIZE, SIZE)
                    if r.collidepoint(pos):
                        x = pos[0]
                        x //= square_width
                        if x == 7: x = 6
                        col = [grid[i][x] for i in range(len(grid))]
                        if 'A' in col:
                            i = col.index('A')
                            if i > 0: col[i - 1] = 'A'
                            col[i] = player_token
                            for i in range(len(grid)): grid[i][x] = col[i]
                            player = False   
                            changements = True
        else: # bot's turn
            col_num = bot(grid)
            col = [grid[i][col_num] for i in range(len(grid))]
            i = col.index('A')
            if i > 0: col[i - 1] = 'A'
            col[i] = bot_token
            for i in range(len(grid)): grid[i][col_num] = col[i]    
            time.delay(500)
            player = True        
            changements = True     

        if changements:
            win.fill(BACKGROUND)
            grid_surface.fill(GRID)
            draw_grid(grid_surface, BACKGROUND, RED, YELLOW, grid, size_grid, square_width)
            win.blit(grid_surface, (0, Y))
            display.update()

            turns += 1
            if turns >= 7:
                play = not won(grid)
                run = play
            changements = False
quit()