import pygame
import sys
from math import *

import physics_engine

pygame.init()
display = None
width = None
height = None
clock = pygame.time.Clock()
ground = 50

def init(screen):
    global width, height, display
    display = screen
    (width, height) = display.get_rect().size
    height -= ground

class Slab:
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        if self.w > self.h:
            self.image = pygame.image.load("Images/wall_horizontal.png").convert_alpha()
        else:
            self.image = pygame.image.load("Images/wall_vertical.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.w, self.h))

        self.color = color

    def draw(self):
        display.blit(self.image, (self.x, self.y))

    