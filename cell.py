import random
import pygame

class Cell:
    def __init__(self, col, row, size):
        self.col = col
        self.row = row
        self.x = col * size
        self.y = row * size
        self.rect = pygame.Rect(self.x, self.y, size, size)
        doa = random.randint(0, 1)
        self.alive = False
        if doa == 0:
            self.alive = True
        self.age = 0
        self.umph = 0
