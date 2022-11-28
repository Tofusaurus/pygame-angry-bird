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

class Pig:
    def __init__(self, x, y, r, v=None, type="PIG", loaded = False, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.r = r
        if v == None:
            self.velocity = Vector()
        else:
            self.velocity = v

        self.pigimage1 = pygame.image.load("Images/pig1.png").convert_alpha()
        self.pigimage2 = pygame.image.load("Images/pig3.png").convert_alpha()

        self.deadpig = pygame.image.load("Images/pig_damaged.png").convert_alpha()

        self.birdimage = pygame.image.load("Images/bird.png").convert_alpha()

        if type == "PIG":
            self.image = random.choice([self.pigimage1, self.pigimage2])
        else:
            self.image = self.birdimage

        self.type = type
        self.color = color
        self.loaded = loaded
        self.path = []
        self.count = 0
        self.count_animated = 0
        self.isDead = False

    def draw(self):
        self.count_animated += 1

        if self.type == "BIRD" and not self.loaded:
            for point in self.path:
                pygame.draw.ellipse(display, self.color, (point[0], point[1], 3, 3), 1)

        if (self.type == "PIG") and (not self.count_animated%20) and (not self.isDead):
            self.image = random.choice([self.pigimage1, self.pigimage2])

        display.blit(self.image, (self.x - self.r, self.y - self.r))


    def dead(self):
        self.isDead = True
        self.image = self.deadpig

    def move(self):
        self.velocity = add_vectors(self.velocity, gravity)

        self.x += self.velocity.magnitude*sin(self.velocity.angle)
        self.y -= self.velocity.magnitude*cos(self.velocity.angle)

        self.velocity.magnitude *= inverse_friction

        if self.x > width - self.r:
            self.x = 2*(width - self.r) - self.x
            self.velocity.angle *= -1
            self.velocity.magnitude *= elasticity
        elif self.x < self.r:
            self.x = 2*self.r - self.x
            self.velocity.angle *= -1
            self.velocity.magnitude *= elasticity

        if self.y > height - self.r:
            self.y = 2*(height - self.r) - self.y
            self.velocity.angle = pi - self.velocity.angle
            self.velocity.magnitude *= elasticity
        elif self.y < self.r:
            self.y = 2*self.r - self.y
            self.velocity.angle = pi - self.velocity.angle
            self.velocity.magnitude *= elasticity

        self.count += 1
        if self.count%1 == 0:
            self.path.append((self.x, self.y))

class Bird(Pig):
    def load(self, slingshot):
        self.x = slingshot.x
        self.y = slingshot.y
        self.loaded = True

    def mouse_selected(self):
        pos = pygame.mouse.get_pos()
        disx = pos[0] - self.x
        disy = pos[1] - self.y
        dist = hypot(disy, disx)
        if dist < self.r:
            return True

        return False

    def reposition(self, slingshot, mouse_click):
        pos = pygame.mouse.get_pos()
        if self.mouse_selected():
            self.x = pos[0]
            self.y = pos[1]

            disx = slingshot.x - self.x
            disy = slingshot.y - self.y
            self.velocity.magnitude = int(hypot(disx, disy)/2)
            if self.velocity.magnitude > 80:
                self.velocity.magnitude = 80
            self.velocity.angle = pi/2 + atan2(disy, disx)

    def unload(self):
        self.loaded = False

    def project_path(self):
        if self.loaded:
            path = []
            ball = Pig(self.x, self.y, self.r, self.velocity, self.type)
            for i in range(30):
                ball.move()
                if i%5 == 0:
                    path.append((ball.x, ball.y))

            for point in path:
                pygame.draw.ellipse(display, self.color, (point[0], point[1], 2, 2))


