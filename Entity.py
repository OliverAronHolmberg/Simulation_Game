import pygame


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

    def move(self):
        pass


    def Main_Entity(self):
        self.move()