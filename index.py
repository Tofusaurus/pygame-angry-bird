import pygame
import sys
import random
from math import *
import physics_engine
import objects
import maps
import interface

pygame.init()
pygame.display.set_caption('Angry Bird')
width = 1500
height = 700
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

physics_engine.init(display)
objects.init(display)
maps.init(display)
interface.init(display)

background = (234, 221, 202)

def close():
    pygame.quit()
    sys.exit()

def start_game(map):
    map.draw_map()

def GAME():
    pass
GAME()
