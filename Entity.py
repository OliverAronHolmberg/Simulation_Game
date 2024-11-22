import pygame
import random

class Entity:
    def __init__(self, screen, game, type, state, x, y):
        self.screen = screen
        self.game = game
        self.type = type
        self.state = state
        self.x = x
        self.y = y
        self.entity_image = pygame.image.load("Images\Entities\Cow.png")
        self.rect = self.entity_image.get_rect()
        

        self.boundry_x = self.game.screen_width
        self.boundry_y = self.game.screen_height

        self.timer = 0

        self.move_speed = 2
        self.move_duration = random.randint(100, 300)
        self.moving = False

    def move(self):
        self.timer += 1
        if self.timer >= self.move_duration:
            self.current_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
            self.moving = random.choice([False, True])
            self.move_duration = random.randint(100, 300)
            self.timer = 0

        

        if self.moving:
            new_x = self.x + self.current_direction[0] * self.move_speed
            new_y = self. y + self.current_direction[1] * self.move_speed

            self.x = max(0, min(self.boundry_x-50, new_x))
            self.y = max(0, min(self.boundry_y-50, new_y))
        


    def Main_Entity(self):
        self.move()
        