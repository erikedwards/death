import pygame
import math
import random
import numpy
import copy
from cell import Cell

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

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
cellSize = 5
cols = int(SCREEN_WIDTH / cellSize)
rows = int(SCREEN_HEIGHT / cellSize)
grid = numpy.empty([cols, rows], Cell)
# grid = numpy.array([cols, rows], Cell)
seed_rate = 5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# set frame rate
FR = 10


# fill grid with initial values.
def init_grid():
    for i in range(cols):
        for j in range(rows):
            # get a random number 0 - 100
            luck = random.randint(0, 100)
            # percentage that live
            survives = False
            if luck > 100 - seed_rate:
                survives = True
            grid[i, j] = Cell(i, j, cellSize, survives)


def draw_grid():
    for i in range(cols):
        for j in range(rows):
            c = grid[i, j]
            young = 10
            mid = 30
            if c.alive:
                if c.age < young:
                    cell_color = GREEN
                elif young <= c.age < mid:
                    cell_color = BLUE
                elif mid <= c.age:
                    cell_color = RED
            else:
                cell_color = BLACK
            pygame.draw.rect(screen, cell_color, c.rect)


def update_grid():
    # new_grid = numpy.copy(grid)

    # copy grid
    new_grid = numpy.empty([cols, rows], Cell)
    for i in range(cols):
        for j in range(rows):
            new_grid[i, j] = copy.copy(grid[i, j])


    for i in range(cols):
        for j in range(rows):
            n = count_neighbors(i, j)
            # if DEAD and exactly 3 neighbors --> ALIVE
            if not grid[i,j].alive and n == 3:
                new_grid[i,j].alive = True
                new_grid[i, j].age = -1
            # if ALIVE and 1 or less neighbors --> DEAD
            if grid[i,j].alive and n < 2:
                new_grid[i,j].alive = False
            # if ALIVE and 4 or more neighbors --> DEAD
            if grid[i,j].alive and n > 3:
                new_grid[i,j].alive = False
            # otherwise, no change from last generation
            # but age the living
            if new_grid[i,j].alive:
                new_grid[i,j].age += 1
    return new_grid


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
            if event.key == pygame.K_UP:
                seed_rate += 5
            if event.key == pygame.K_DOWN and seed_rate > 5:
                seed_rate -= 5
            if event.key == pygame.K_RIGHT:
                if FR > 9:
                    FR += 10
                else:
                    FR += 1
            if event.key == pygame.K_LEFT:
                if FR > 19:
                    FR -= 10
                elif FR > 1:
                    FR -= 1
            if event.key == pygame.K_RETURN:
                init_grid()

    # Clear Screen
    screen.fill(WHITE)

    # draw stuff
    draw_grid()

    # show seed value
    seed_string = "Seed Value: " + str(seed_rate) + "  [UP/DOWN Arrows to change]"
    seed_surf = FONT.render(seed_string, True, FONT_RGB)
    nX = 20
    nY = SCREEN_HEIGHT - 80
    screen.blit(seed_surf, (nX, nY))

    # show frame rate
    FR_String = "Frame rate: " + str(FR) + "  [LEFT/RIGHT Arrows to change]"
    FR_surf = FONT.render(FR_String, True, FONT_RGB)
    nX = 20
    nY = SCREEN_HEIGHT - 40
    screen.blit(FR_surf, (nX, nY))

    # --- Update the screen
    pygame.display.flip()

    # Game logic
    next_grid = update_grid()
    grid = numpy.copy(next_grid)

    # --- Limit to 60 frames per second
    clock.tick(FR)

# Close the window and quit.
pygame.quit()
