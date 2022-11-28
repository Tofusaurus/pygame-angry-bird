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

    def draw_map(self):
        birds = []
        pigs = []
        blocks = []
        walls = []
        self.score = 0

        if self.level == 1:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1100, height - 40, 20))
            pigs.append(physics_engine.Pig(1500, height - 40, 20))

            blocks.append(physics_engine.Block(1300, height - 60, 60))

        elif self.level == 2:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1000, height - 40, 20))
            pigs.append(physics_engine.Pig(1400, height - 40, 20))

            blocks.append(physics_engine.Block(1200, height - 60, 60))
            blocks.append(physics_engine.Block(1200, height - 2*35, 60))
            blocks.append(physics_engine.Block(1500, height - 60, 60))

        elif self.level == 3:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1200, height - 60, 30))
            pigs.append(physics_engine.Pig(1300, height - 60, 30))

            blocks.append(physics_engine.Block(900, height - 100, 100))

            walls.append(objects.Slab(900, 400, 500, 40))


        elif self.level == 4:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1200, 500 - 60, 30))
            pigs.append(physics_engine.Pig(1300, height - 60, 30))

            walls.append(objects.Slab(1000, 450, 500, 20))

            blocks.append(physics_engine.Block(1100, height - 100, 100))

        elif self.level == 5:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1300, 500 - 60, 25))
            pigs.append(physics_engine.Pig(1300, height - 60, 25))

            walls.append(objects.Slab(500, 400, 100, height - 400))
            walls.append(objects.Slab(1000, 450, 500, 30))

            blocks.append(physics_engine.Block(1150, 500 - 100, 100))
            blocks.append(physics_engine.Block(1100, height - 100, 100))

        elif self.level == 6:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1300, 500 - 60, 25))
            pigs.append(physics_engine.Pig(1300, height - 60, 25))

            walls.append(objects.Slab(1000, 0, 30, 450))
            walls.append(objects.Slab(1000, 450, 500, 30))

            blocks.append(physics_engine.Block(1150, 500 - 100, 100))
            blocks.append(physics_engine.Block(1100, height - 100, 100))

        elif self.level == 7:
            for i in range(4):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1100, 500 - 60, 25))
            pigs.append(physics_engine.Pig(1300, 500 - 60, 25))
            pigs.append(physics_engine.Pig(1200, height - 60, 25))

            walls.append(objects.Slab(1200, 250, 30, 200))
            walls.append(objects.Slab(1000, 450, 500, 30))

        elif self.level == 8:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1100, height - 60, 25))
            pigs.append(physics_engine.Pig(1200, height - 60, 25))

            walls.append(objects.Slab(700, 250, 30, height - 250))

        elif self.level == 9:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1100, height - 60, 25))
            pigs.append(physics_engine.Pig(1450, height - 60, 25))


            blocks.append(physics_engine.Block(1250, height - 100, 100))
            blocks.append(physics_engine.Block(1250, height - 2*60, 100))

            walls.append(objects.Slab(700, 400, 30, height - 400))

        elif self.level == 10:
            for i in range(3):
                new_bird = physics_engine.Bird(40*i + 5*i, height - 40, 20, None, "BIRD")
                birds.append(new_bird)

            pigs.append(physics_engine.Pig(1100, height - 60, 25))
            pigs.append(physics_engine.Pig(1450, height - 60, 25))

            blocks.append(physics_engine.Block(1250, height - 100, 100))
            blocks.append(physics_engine.Block(1250, height - 2*60, 100))
            blocks.append(physics_engine.Block(900, height - 100, 100))

            walls.append(objects.Slab(900, 400, 500, 30))

        self.start_level(birds, pigs, blocks, walls)

    