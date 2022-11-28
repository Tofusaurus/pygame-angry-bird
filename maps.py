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

class Maps:
    def __init__(self):
        self.level = 1
        self.max_level = 15
        self.color = {'background': (0,128,128)}
        self.score = 0

    def wait_level(self):
        time = 0
        while time < 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
            time += 1
            clock.tick(1)

        return

    def check_win(self, pigs, birds):
        if pigs == []:
            print("WON!")
            return True
        if (not pigs == []) and birds == []:
            print("LOST!")
            return False

    def pause(self):
        pause_text = interface.Label(700, 200, 400, 200, None, self.color['background'])
        pause_text.add_text("GAME PAUSED", 70, "Fonts/SEASRN.ttf", (236, 240, 241))

        replay = interface.Button(350, 500, 300, 100, self.draw_map, (244, 208, 63), (247, 220, 111))
        replay.add_text("RESTART", 60, "Fonts/Amatic-Bold.ttf", self.color['background'])

        resume = interface.Button(750, 500, 300, 100, None, (88, 214, 141), (171, 235, 198))
        resume.add_text("RESUME", 60, "Fonts/Amatic-Bold.ttf", self.color['background'])

        exit = interface.Button(1150, 500, 300, 100, close, (241, 148, 138), (245, 183, 177))
        exit.add_text("QUIT", 60, "Fonts/Amatic-Bold.ttf", self.color['background'])

    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_p:
                        return
                    if event.key == pygame.K_ESCAPE:
                        return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if replay.isActive():
                        replay.action()
                    if resume.isActive():
                        return
                    if exit.isActive():
                        exit.action()

            replay.draw()
            resume.draw()
            exit.draw()
            pause_text.draw()
          

            pygame.display.update()
            clock.tick(60)

   