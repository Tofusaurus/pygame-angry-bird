import pygame
import sys

import physics_engine
import objects
import interface

pygame.init()
height = None
width = None
display = None
clock = pygame.time.Clock()

ground = 50

d_velocity = 2.0

def init(screen):
    global width, height, display
    display = screen
    (width, height) = display.get_rect().size
    height -= ground
    interface.init(display)

def all_rest(pigs, birds, blocks):
    threshold = 0.15
    for pig in pigs:
        if pig.velocity.magnitude >= threshold:
            return False

    for bird in birds:
        if bird.velocity.magnitude >= threshold:
            return False

    for block in blocks:
        if block.velocity.magnitude >= threshold:
            return False

    return True

def close():
    pygame.quit()
    sys.exit()

