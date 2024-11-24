import pygame

class UI:
    def __init__(self, game, screen, x, y, image):
        self.game = game
        self.screen = screen
        self.x = x
        self.y = y
        self.open = False
        

        self.image = image
        
        
        self.original_width= self.image.get_width()
        self.original_height= self.image.get_height()

        self.scaled_image = pygame.transform.scale(self.image, (int(self.original_width*3), int(self.original_height*4)))
        self.rect = self.scaled_image.get_rect()

  
        
            
            
    