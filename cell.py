import pygame


class Cell:
    def __init__(self, col, row, size, cell_alive):
        self.col = col
        self.row = row
        self.x = col * size
        self.y = row * size
        self.rect = pygame.Rect(self.x, self.y, size, size)
        self.alive = cell_alive
        self.age = 0
        self.umph = 0
