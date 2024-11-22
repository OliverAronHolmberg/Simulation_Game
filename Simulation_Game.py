import pygame
import os
import sys
import random


from Entity import Entity

class Game:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))


        self.entities = []

        for entity in range(10):
            entity = Entity(self.screen, self, "Cow", "Friendly", random.randint(0, self.screen_width),random.randint(0, self.screen_height))
            self.entities.append(entity)


    def exit(self):
        pygame.quit()
        sys.exit()


    def Main_loop(self):
        while True:
            events = pygame.event.get()
            self.screen.fill((0,0,0))

            for event in events:
                if event.type == pygame.QUIT:
                    self.exit()
            for entity in self.entities:
                self.screen.blit(entity.entity_image, (entity.x, entity.y))
                entity.Main_Entity()


            pygame.display.flip()
                





Game().Main_loop()