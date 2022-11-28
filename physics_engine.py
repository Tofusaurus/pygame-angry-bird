import pygame
import sys
from math import *
import random

pygame.init()
width = None
height = None
display = None
ground = 50
clock = pygame.time.Clock()

def init(screen):
    global width, height, display
    display = screen
    (width, height) = display.get_rect().size
    height -= ground

class Vector:
    def __init__(self, magnitude=0, angle=radians(0)):
        self.magnitude = magnitude
        self.angle = angle

def add_vectors(vector1, vector2):
    x = sin(vector1.angle)*vector1.magnitude + sin(vector2.angle)*vector2.magnitude
    y = cos(vector1.angle)*vector1.magnitude + cos(vector2.angle)*vector2.magnitude

    new_angle = 0.5*pi - atan2(y, x)
    new_magnitude = hypot(x, y)

    new_vector = Vector(new_magnitude, new_angle)
    return new_vector

gravity = Vector(0.2, pi)
inverse_friction = 0.99
elasticity = 0.8
block_elasticity = 0.7

