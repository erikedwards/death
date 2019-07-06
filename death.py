import pygame
import math
from Cell import cell

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
size = 20
cols = int(SCREEN_WIDTH / size)
rows = int(SCREEN_HEIGHT / size)
grid = [[]]



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main Loop
run = True

# set frame rate
FR = 60

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

    # Game logic

    # Clear Screen
    screen.fill(WHITE)


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FR)

    # Close the window and quit.
pygame.quit()
