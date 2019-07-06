import pygame
import math
import numpy
from cell import Cell

# CONSTANTS
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init pygame
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("the game of Death - a rad skillz joint")
FONT = pygame.font.SysFont('Courier New', 30)
FONT_RGB = RED

# init game values
cellSize = 20
cols = int(SCREEN_WIDTH / cellSize)
rows = int(SCREEN_HEIGHT / cellSize)
grid = numpy.empty([cols, rows], Cell)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# set frame rate
FR = 60

# fill grid with initial values.
def init_grid():
    for i in range(cols):
        for j in range(rows):
            grid[i,j] = Cell(i, j, cellSize)


def draw_grid():
    for i in range(cols):
        for j in range(rows):
            c = grid[i, j]
            if c.alive:
                cell_color = WHITE
            else:
                cell_color = BLACK
            pygame.draw.rect(screen, cell_color, c.rect)

def update_grid():
    new_grid = grid
    for i in range(cols):
        for j in range(rows):
            n = count_neighbors(i, j)
            # if DEAD and exactly 3 neighbors --> ALIVE
            if not grid[i,j].alive and n == 3:
                new_grid[i,j].alive = True
            # if ALIVE and 1 or less neighbors --> DEAD
            if grid[i,j].alive and n < 2:
                new_grid[i,j].alive = False
            # if ALIVE and 4 or more neighbors --> DEAD
            if grid[i,j].alive and n > 3:
                new_grid[i,j].alive = False
            # otherwise, no change from last generation
            new_grid[i,j].age += 1


def count_neighbors(x, y):
    count = 0
    # check all eight neighbors
    for i in range(-1, 2):
        for j in range(-1, 2):
            if grid[(x + i + cols) % cols, (y + j + rows) % rows].alive:
                count += 1
    # but you also counted yourself so remove one if you're alive
    if grid[x, y].alive:
        count -= 1
    return count



# Main Loop
run = True
init_grid()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     maxN += 2
            # if event.key == pygame.K_DOWN and maxN > 2:
            #     maxN -= 2
            # if event.key == pygame.K_RIGHT:
            #     if FR > 9:
            #         FR += 10
            #     else:
            #         FR += 1
            # if event.key == pygame.K_LEFT:
            #     if FR > 19:
            #         FR -= 10
            #     elif FR > 1:
            #         FR -= 1
            continue

    # Clear Screen
    screen.fill(WHITE)

    # Game logic
    update_grid()

    # draw stuff
    draw_grid()




    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FR)

# Close the window and quit.
pygame.quit()
