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
    map = maps.Maps()

    welcome = interface.Label(700, 100, 400, 200, None, background)
    welcome.add_text("ANGRY BIRD GAME", 80, "Fonts/Amatic-Bold.ttf", (236, 240, 241))

    start = interface.Button(500, 400, 300, 100, start_game, (0,0,0), (50,205,50))
    start.add_text("START GAME", 60, "Fonts/Amatic-Bold.ttf", background)

    exit = interface.Button(1000, 400, 300, 100, close, (255, 174, 66), (255,0,0))
    exit.add_text("QUIT", 60, "Fonts/Amatic-Bold.ttf", background)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.isActive():
                    exit.action()
                if start.isActive():
                    start_game(map)

        display.fill(background)

        start.draw()
        exit.draw()
        welcome.draw()

        pygame.display.update()
        clock.tick(60)

GAME()
